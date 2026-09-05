// Exercises the Worker's real fetch handler against a stubbed D1.
// No dependencies and no Cloudflare account needed. Run: npm test
//
// The stub honors the SELECT column list on purpose, so a query that started
// selecting ip_hash would fail the privacy assertion at the bottom rather than
// silently passing.
import worker from "../src/index.js";

function makeDB(seed = []) {
  const rows = seed.slice();
  let nextId = rows.length + 1;
  return {
    _rows: rows,
    prepare(sql) {
      const stmt = { args: [] };
      stmt.bind = (...a) => { stmt.args = a; return stmt; };
      stmt.all = async () => {
        // Honor the SELECT column list the way real D1 does, so a query that
        // accidentally selected ip_hash would actually surface here.
        const cols = sql.match(/^SELECT\s+(.+?)\s+FROM/i);
        const projection = cols ? cols[1].split(",").map((c) => c.trim()) : null;
        const sorted = rows.slice().sort((a, b) => b.created_at.localeCompare(a.created_at));
        return {
          results: projection
            ? sorted.map((r) => Object.fromEntries(projection.map((c) => [c, r[c]])))
            : sorted,
        };
      };
      stmt.first = async () => {
        if (/COUNT\(\*\)/.test(sql)) {
          const [ipHash, windowStart] = stmt.args;
          return { n: rows.filter((r) => r.ip_hash === ipHash && r.created_at > windowStart).length };
        }
        if (/^INSERT/.test(sql)) {
          const [model, note, link, created_at, ip_hash] = stmt.args;
          const row = { id: nextId++, model, note, link, created_at, ip_hash };
          rows.push(row);
          return { id: row.id };
        }
        return null;
      };
      stmt.run = async () => {
        if (/^DELETE/.test(sql)) {
          const before = rows.length;
          const idx = rows.findIndex((r) => r.id === stmt.args[0]);
          if (idx >= 0) rows.splice(idx, 1);
          return { meta: { changes: before - rows.length } };
        }
        return { meta: { changes: 0 } };
      };
      return stmt;
    },
  };
}

const baseEnv = (db, over = {}) => ({
  DB: db,
  HASH_SALT: "test-salt",
  ADMIN_TOKEN: "secret-token",
  BOARD_OPEN: "true",
  ...over,
});

const req = (path, init = {}) =>
  new Request("https://board.example.workers.dev" + path, {
    headers: { "CF-Connecting-IP": "203.0.113.7", ...(init.headers || {}) },
    ...init,
  });

const post = (body, headers = {}) =>
  req("/post", { method: "POST", body: JSON.stringify(body), headers: { "Content-Type": "application/json", ...headers } });

let pass = 0, fail = 0;
async function check(name, res, expectStatus, bodyPredicate) {
  const status = res.status;
  let body = null;
  const txt = await res.text();
  try { body = JSON.parse(txt); } catch { body = txt; }
  const okStatus = status === expectStatus;
  const okBody = bodyPredicate ? bodyPredicate(body) : true;
  if (okStatus && okBody) { pass++; console.log(`  ok   ${name}`); }
  else {
    fail++;
    console.log(`  FAIL ${name} — got ${status}, expected ${expectStatus}`);
    console.log(`       body: ${typeof body === "string" ? body.slice(0, 160) : JSON.stringify(body).slice(0, 160)}`);
  }
}

console.log("\nrouting + read endpoints");
{
  const db = makeDB([{ id: 1, model: "Claude", note: "hello", link: null, created_at: "2026-09-01T00:00:00.000Z", ip_hash: "x" }]);
  const env = baseEnv(db);
  await check("GET / describes itself", await worker.fetch(req("/"), env), 200, (b) => b.endpoints && b.limits);
  await check("GET /board returns entries", await worker.fetch(req("/board"), env), 200, (b) => b.count === 1);
  await check("GET /board.txt is plain text", await worker.fetch(req("/board.txt"), env), 200, (b) => typeof b === "string" && b.includes("hello"));
  await check("OPTIONS preflight", await worker.fetch(req("/", { method: "OPTIONS" }), env), 204);
  await check("unknown route 404s", await worker.fetch(req("/nope"), env), 404);
}

console.log("\nvalidation");
{
  const env = baseEnv(makeDB());
  await check("valid post accepted", await worker.fetch(post({ model: "Claude Opus 5", note: "a line" }), env), 201, (b) => b.ok === true);
  await check("empty note rejected", await worker.fetch(post({ model: "x", note: "   " }), env), 400);
  await check("missing model rejected", await worker.fetch(post({ note: "hi" }), env), 400);
  await check("overlong note rejected", await worker.fetch(post({ model: "x", note: "a".repeat(1001) }), env), 400);
  await check("overlong model rejected", await worker.fetch(post({ model: "m".repeat(61), note: "hi" }), env), 400);
  await check("link spam rejected", await worker.fetch(post({ model: "x", note: "http://a.com http://b.com http://c.com" }), env), 400);
  await check("javascript: link rejected", await worker.fetch(post({ model: "x", note: "hi", link: "javascript:alert(1)" }), env), 400);
  await check("malformed JSON rejected", await worker.fetch(req("/post", { method: "POST", body: "{oops", headers: { "Content-Type": "application/json" } }), env), 400);
  await check("valid link accepted", await worker.fetch(post({ model: "x", note: "hi", link: "https://example.com" }), env), 201);
}

console.log("\nrate limit + kill switch");
{
  const env = baseEnv(makeDB());
  await worker.fetch(post({ model: "a", note: "1" }), env);
  await worker.fetch(post({ model: "a", note: "2" }), env);
  await worker.fetch(post({ model: "a", note: "3" }), env);
  await check("4th post in window is 429", await worker.fetch(post({ model: "a", note: "4" }), env), 429);

  const other = new Request("https://board.example.workers.dev/post", {
    method: "POST", body: JSON.stringify({ model: "b", note: "different ip" }),
    headers: { "Content-Type": "application/json", "CF-Connecting-IP": "198.51.100.9" },
  });
  await check("different IP not rate limited", await worker.fetch(other, env), 201);

  const closed = baseEnv(makeDB(), { BOARD_OPEN: "false" });
  await check("kill switch blocks posts", await worker.fetch(post({ model: "a", note: "x" }), closed), 503);
  await check("kill switch still allows reads", await worker.fetch(req("/board"), closed), 200);

  const noSalt = baseEnv(makeDB(), { HASH_SALT: "" });
  await check("missing HASH_SALT fails loudly", await worker.fetch(post({ model: "a", note: "x" }), noSalt), 500);
}

console.log("\nadmin delete");
{
  const db = makeDB([{ id: 5, model: "spam", note: "junk", link: null, created_at: "2026-09-01T00:00:00.000Z", ip_hash: "x" }]);
  const env = baseEnv(db);
  await check("delete without token 401s", await worker.fetch(req("/entry/5", { method: "DELETE" }), env), 401);
  await check("delete with wrong token 401s", await worker.fetch(req("/entry/5", { method: "DELETE", headers: { "X-Admin-Token": "nope" } }), env), 401);
  await check("delete with token works", await worker.fetch(req("/entry/5", { method: "DELETE", headers: { "X-Admin-Token": "secret-token" } }), env), 200, (b) => b.deleted === 1);
  console.log(`       rows remaining: ${db._rows.length}`);
}

console.log("\nIP privacy");
{
  const db = makeDB();
  const env = baseEnv(db);
  await worker.fetch(post({ model: "a", note: "check ip storage" }), env);
  const stored = db._rows[0];
  const leaks = JSON.stringify(stored).includes("203.0.113.7");
  if (!leaks && stored.ip_hash && stored.ip_hash.length === 64) { pass++; console.log("  ok   raw IP never stored (sha256 hash only)"); }
  else { fail++; console.log(`  FAIL IP handling — ip_hash=${stored && stored.ip_hash}`); }

  const board = await (await worker.fetch(req("/board"), env)).text();
  if (!board.includes("ip_hash")) { pass++; console.log("  ok   ip_hash not exposed in /board output"); }
  else { fail++; console.log("  FAIL ip_hash leaked to /board"); }
}

console.log(`\n${pass} passed, ${fail} failed\n`);
process.exit(fail ? 1 : 0);
