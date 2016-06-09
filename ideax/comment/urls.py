from django.conf.urls import url
from ideax.comment.views import post_comment


urlpatterns = [
    url(r'$', post_comment),
]
