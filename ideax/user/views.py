from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import View
from ideax.idea.models import Idea
from ideax.shortcuts import get_current_site


class ProfileView(View):

    def get(self, request, username=None):
        user = get_object_or_404(get_user_model(), username=username)
        ideas = Idea.objects.filter(
            author=user,
            site=get_current_site(request)).order_by('-created_at')
        return render(request, 'user/profile.html', {
            'user': user,
            'ideas': ideas,
            'paging_url_prefix': '/users/%s/ideas/' % user.username,
        })
