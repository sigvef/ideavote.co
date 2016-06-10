$(function() {
  'use strict';

  $('.reply-form-container a.toggle-reply-form').click(function(e) {
    e.preventDefault();
    var replyFormContainer = $(this.parentElement.parentElement);
    replyFormContainer.find('.reply-form').show();
    $(this).hide();
  });

  $('.collapsible-container a.collapse-thread').click(function(e) {
    e.preventDefault();
    var container = $(this.parentElement);
    container.find('>.collapsible').toggle();
  });
});
