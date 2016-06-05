from django.views.generic import View
from django.shortcuts import render
from ideax.idea.models import Idea


class FrontpageView(View):
    def get(self, request):
        ideas = Idea.objects.all()
        return render(request, 'frontpage/frontpage.html', {
            "ideas": ideas
        })
