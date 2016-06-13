from django.conf.urls import url
from ideax.notify.views import NotificationListView
from ideax.notify.views import NotificationView


urlpatterns = [
    url(r'^$', NotificationListView.as_view()),
    url(r'/(?P<notification_id>\d+)$', NotificationView.as_view()),
]
