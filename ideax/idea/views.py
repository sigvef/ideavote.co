from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View
from ideax.comment.models import Comment
from ideax.idea.models import Idea
from ideax.idea.ranking_functions import hot


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

    def get_idea_queryset(self):
        return Idea.objects.all()

    def get(self, request, page=1):
        paginator = Paginator(self.get_idea_queryset(), 15)
        ideas_page = paginator.page(page)
        return render(request, 'idea/idealist.html', {
            "ideas_page": ideas_page,
            "ordering": self.ordering,
        })


class HotIdeaListView(IdeaListView):
    ordering = 'hot'

    def get_idea_queryset(self):
        now = timezone.now()
        return sorted(Idea.objects.all(), key=lambda idea: -hot(idea, now))


class NewIdeaListView(IdeaListView):
    ordering = 'new'

    def get_idea_queryset(self):
        return Idea.objects.all().order_by('-created_at')


class TopIdeaListView(IdeaListView):
    ordering = 'top'

    def get_idea_queryset(self):
        return Idea.objects.all().annotate(
            score=Count('upvoters')).order_by('-score')
