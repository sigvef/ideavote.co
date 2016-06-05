from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from ideax.idea.models import Idea


class IdeaView(View):
    def get(self, request, slug_id=None):
        idea = get_object_or_404(Idea, slug_id=slug_id)
        if request.path != idea.get_absolute_url():
            return HttpResponseRedirect(idea.get_absolute_url())
        return render(request, 'idea/idea.html', {
            "idea": idea
        })
