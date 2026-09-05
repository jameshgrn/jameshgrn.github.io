/*
* Greedy Navigation
*
* http://codepen.io/lukejacksonn/pen/PwmwWV
*
*/

var $nav = $('#site-nav');
var $btn = $('#site-nav button');
var $vlinks = $('#site-nav .visible-links');
var $hlinks = $('#site-nav .hidden-links');

var breaks = [];

function updateNav() {

  var availableSpace = $btn.hasClass('hidden') ? $nav.width() : $nav.width() - $btn.width() - 30;

  // The visible list is overflowing the nav
  if($vlinks.width() > availableSpace) {

    // Move items to the hidden list until the visible list fits. The site
    // title is pinned to the visible list, so stop once it is all that is
    // left - otherwise a title wider than the nav loops forever.
    while($vlinks.width() > availableSpace) {

      var $overflow = $vlinks.children('*:not(.masthead__menu-item--lg)').last();

      if(!$overflow.length) {
        break;
      }

      // Record the width of the list
      breaks.push($vlinks.width());

      // Move item to the hidden list
      $overflow.prependTo($hlinks);

      // Show the dropdown btn
      if($btn.hasClass('hidden')) {
        $btn.removeClass('hidden');
      }

      // Showing the btn eats into the space available to the visible list
      availableSpace = $btn.hasClass('hidden') ? $nav.width() : $nav.width() - $btn.width() - 30;
    }

  // The visible list is not overflowing
  } else {

    // There is space for another item in the nav
    if(availableSpace > breaks[breaks.length-1]) {

      // Move the item to the visible list
      $hlinks.children().first().appendTo($vlinks);
      breaks.pop();
    }

    // Hide the dropdown btn if hidden list is empty
    if(breaks.length < 1) {
      $btn.addClass('hidden');
      $hlinks.addClass('hidden');
    }
  }

  // Keep counter updated
  $btn.attr("count", breaks.length);

}

// Window listeners

$(window).resize(function() {
  updateNav();
});

$btn.on('click', function() {
  $hlinks.toggleClass('hidden');
  $(this).toggleClass('close');
});

updateNav();