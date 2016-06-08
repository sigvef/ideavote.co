from django.conf.urls import url
from ideax.frontpage.views import FrontpageView
from ideax.idea.views import NewIdeaListView
from ideax.idea.views import TopIdeaListView
from ideax.idea.views import HotIdeaListView


urlpatterns = [
    url(r'^$', FrontpageView.as_view()),
    url(r'^new$', NewIdeaListView.as_view()),
    url(r'^new/(?P<page>\d+)', NewIdeaListView.as_view()),
    url(r'^top$', TopIdeaListView.as_view()),
    url(r'^top/(?P<page>\d+)', TopIdeaListView.as_view()),
    url(r'^hot$', HotIdeaListView.as_view()),
    url(r'^hot/(?P<page>\d+)', HotIdeaListView.as_view()),
]
