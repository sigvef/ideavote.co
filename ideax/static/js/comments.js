$(function() {
  'use strict';

  $('.reply-form-container a').click(function(e) {
    e.preventDefault();
    var replyFormContainer = $(this.parentElement.parentElement);
    replyFormContainer.find('.reply-form').show();
    $(this).hide();
  });
});
