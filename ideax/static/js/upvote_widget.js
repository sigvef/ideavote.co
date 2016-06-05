$(function() {
  'use strict';

  console.log($('.upvote-widget .star').click(function(e) {
    e.preventDefault();
    $(this.parentElement).toggleClass('upvoted');
  }));
});
