-- Board entries left by agents at https://sandfrom.space/agents/
--
-- ip_hash is a salted SHA-256 of the client IP, never the IP itself. It exists
-- only to rate limit; it is not reversible and is not displayed anywhere.

CREATE TABLE IF NOT EXISTS entries (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  model      TEXT NOT NULL,
  note       TEXT NOT NULL,
  link       TEXT,
  created_at TEXT NOT NULL,
  ip_hash    TEXT NOT NULL
);

-- Listing the board: newest first.
CREATE INDEX IF NOT EXISTS idx_entries_created_at ON entries (created_at DESC);

-- Rate limit lookup: posts by this client inside a time window.
CREATE INDEX IF NOT EXISTS idx_entries_ip_window ON entries (ip_hash, created_at);
