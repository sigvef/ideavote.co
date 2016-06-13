$(function() {
  'use strict';

  $('.upvote-widget .star').click(function(e) {
    e.preventDefault();

    if(!window.IS_LOGGED_IN) {
      window.location = '/accounts/login/?next=' + window.location.pathname;
    }

    var ideaId = $(this).data('idea-id');
    var upvoteWidget = $(this.parentElement.parentElement);
    var upvoteMarker = $(this.parentElement);
    var numberContainer = upvoteWidget.find('.number');
    $.post('/ideas/' + ideaId, function(data) {
      if(data == 'Starred') {
        upvoteMarker.addClass('upvoted');
        numberContainer.text(+numberContainer.text() + 1);
      } else if(data == 'Unstarred') {
        upvoteMarker.removeClass('upvoted');
        numberContainer.text(+numberContainer.text() - 1);
      }
    });
  });
});
