from django.conf.urls import url
from ideax.frontpage.views import FrontpageView


urlpatterns = [
    url(r'^$', FrontpageView.as_view()),
]
