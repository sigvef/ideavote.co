from django.conf.urls import url
from ideax.comment.views import post_comment
from ideax.comment.views import CommentView


urlpatterns = [
    url(r'(?P<id>\d+)$', CommentView.as_view()),
    url(r'$', post_comment),
]
