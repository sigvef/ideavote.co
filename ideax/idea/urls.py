from django.conf.urls import url
from ideax.idea.views import IdeaView


urlpatterns = [
    url(r'(?P<slug_id>[a-zA-Z0-9]+)/.*$', IdeaView.as_view()),
    url(r'(?P<slug_id>[a-zA-Z0-9]+)$', IdeaView.as_view()),
]
