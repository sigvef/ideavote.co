from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from ideax.comment.models import Comment
from ideax.idea.forms import IdeaForm
from ideax.idea.forms import IdeaTagForm
from ideax.idea.models import Idea
from ideax.idea.ranking_functions import hot
from ideax.shortcuts import get_current_site


class IdeaEditView(View):
    @method_decorator(login_required)
    def get(self, request, slug_id=None):
        idea = get_object_or_404(Idea, slug_id=slug_id)
        if request.user != idea.author:
            raise Http404
        return render(request, 'idea/idea_edit.html', {
            'form': IdeaForm(instance=idea),
        })

    @method_decorator(login_required)
    @method_decorator(transaction.atomic)
    def post(self, request, slug_id=None):
        idea = get_object_or_404(Idea, slug_id=slug_id)
        if request.user != idea.author:
            raise Http404
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            idea = form.save()
            return HttpResponseRedirect(idea.get_absolute_url())
        return HttpResponse(form.errors)


class IdeaTagView(View):
    @method_decorator(login_required)
    def post(self, request, slug_id=None):
        idea = get_object_or_404(Idea, slug_id=slug_id)
        if not request.user.moderator_sites.filter(
                id=idea.site.settings.id).exists():
            return HttpResponseNotFound()
        form = IdeaTagForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data['tags'].split(',')
            idea.tags.set(*tags)
            return HttpResponse('OK')
        return HttpResponse(form.errors)


class IdeaCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'idea/idea_edit.html', {
            'form': IdeaForm(),
        })

    @method_decorator(login_required)
    @method_decorator(transaction.atomic)
    def post(self, request):
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.site = get_current_site(request)
            idea.author = request.user
            idea.save()
            idea.upvoters.add(request.user)
            return HttpResponseRedirect(idea.get_absolute_url())
        return HttpResponse(form.errors)


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
        ideas = self.get_idea_queryset(request)
        return render(request, 'idea/idealist.html', {
            'ordering': self.ordering,
            'ideas': ideas,
            'page': page,
            'paging_url_prefix': '/%s/' % self.ordering,
        })


class HotIdeaListView(IdeaListView):
    ordering = 'hot'

    def get_idea_queryset(self, request):
        return sorted(Idea.objects.filter(site=get_current_site(request),
                                          archived=False),
                      key=hot, reverse=True)


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


class IdeaSearchView(SearchView):

    def __call__(self, request):
        self.searchqueryset = SearchQuerySet().filter(site=request.site.domain)
        return super(IdeaSearchView, self).__call__(request)
