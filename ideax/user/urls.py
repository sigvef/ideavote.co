from django.conf.urls import url
from ideax.user.views import ProfileView


urlpatterns = [
    url(r'(?P<username>[a-zA-Z0-9]+)$', ProfileView.as_view()),
]
