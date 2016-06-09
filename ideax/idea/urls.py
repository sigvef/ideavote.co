from django.conf.urls import url
from ideax.idea.views import IdeaView
from ideax.idea.views import post_idea


urlpatterns = [
    url(r'^$', post_idea),
    url(r'(?P<slug_id>[a-zA-Z0-9]+)/.*$', IdeaView.as_view()),
    url(r'(?P<slug_id>[a-zA-Z0-9]+)$', IdeaView.as_view()),
]
