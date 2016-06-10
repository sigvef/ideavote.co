from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Count
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View
from ideax.comment.models import Comment
from ideax.idea.forms import IdeaForm
from ideax.idea.models import Idea
from ideax.idea.ranking_functions import hot
from ideax.shortcuts import get_current_site
import random


class IdeaView(View):
    def get(self, request, slug_id=None):
        idea = get_object_or_404(Idea, slug_id=slug_id)
        if request.path != idea.get_absolute_url():
            return HttpResponseRedirect(idea.get_absolute_url())
        comments = Comment.objects.filter(idea__id=idea.id)
        return render(request, 'idea/idea.html', {
            "idea": idea,
            'comments': comments,
        })

    def post(self, request, slug_id=None):
        idea = get_object_or_404(Idea, slug_id=slug_id)
        if idea.upvoters.filter(id=request.user.id).exists():
            idea.upvoters.remove(request.user)
            return HttpResponse('Unstarred')
        else:
            idea.upvoters.add(request.user)
            return HttpResponse('Starred')


class IdeaListView(View):

    ordering = ''

    def get_idea_queryset(self, request):
        return Idea.objects.filter(site=get_current_site(request),
                                   archived=False)

    def get(self, request, page=1):
        paginator = Paginator(self.get_idea_queryset(request), 15)
        ideas_page = paginator.page(page)
        return render(request, 'idea/idealist.html', {
            "ideas_page": ideas_page,
            "ordering": self.ordering,
        })


class HotIdeaListView(IdeaListView):
    ordering = 'hot'

    def get_idea_queryset(self, request):
        now = timezone.now()
        return sorted(Idea.objects.filter(site=get_current_site(request),
                                          archived=False),
                      key=lambda idea: -hot(idea, now))


class NewIdeaListView(IdeaListView):
    ordering = 'new'

    def get_idea_queryset(self, request):
        return Idea.objects.filter(
            site=get_current_site(request),
            archived=False).order_by('-created_at')


class TopIdeaListView(IdeaListView):
    ordering = 'top'

    def get_idea_queryset(self, request):
        return Idea.objects.filter(
            site=get_current_site(request),
            archived=False).annotate(
                score=Count('upvoters')).order_by('-score')


@login_required
@transaction.atomic
def post_idea(request):
    if request.method == 'POST':
        form = IdeaForm(data=request.POST)
        if form.is_valid():
            idea = form.save()
            idea.author = request.user
            idea.site = get_current_site(request)
            idea.slug_id = random.randint(0, 99999999)
            idea.save()
            return HttpResponseRedirect(idea.get_absolute_url())
        return HttpResponse(form.errors)
