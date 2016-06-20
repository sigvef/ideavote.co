from django.conf.urls import url
from ideax.idea.views import IdeaCreateView
from ideax.idea.views import IdeaEditView
from ideax.idea.views import IdeaPreviewView
from ideax.idea.views import IdeaTagView
from ideax.idea.views import IdeaView


urlpatterns = [
    url(r'^new$', IdeaCreateView.as_view()),
    url(r'^preview$', IdeaPreviewView.as_view()),
    url(r'(?P<slug_id>[a-zA-Z0-9]+)/edit$', IdeaEditView.as_view()),
    url(r'(?P<slug_id>[a-zA-Z0-9]+)/tags$', IdeaTagView.as_view()),
    url(r'(?P<slug_id>[a-zA-Z0-9]+)/.*$', IdeaView.as_view()),
    url(r'(?P<slug_id>[a-zA-Z0-9]+)$', IdeaView.as_view()),
]
