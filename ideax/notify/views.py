from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from notifications.models import Notification


class NotificationListView(View):
    @method_decorator(login_required)
    def get(self, request):
        notifications = request.user.notifications.unread()
        return render(request, 'notify/notification_list.html', {
            'notifications': notifications,
        })


class NotificationView(View):
    @method_decorator(login_required)
    def post(self, request, notification_id=None):
        notification = get_object_or_404(Notification, id=notification_id)
        if request.user != notification.recipient:
            raise Http404
        notification.mark_as_read()
        return HttpResponseRedirect(
            notification.action_object.get_absolute_url())
