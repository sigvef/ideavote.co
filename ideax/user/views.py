from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import View


class ProfileView(View):

    def get(self, request, username=None):
        user = get_object_or_404(get_user_model(), username=username)
        return render(request, 'user/profile.html', {
            'user': user,
        })
