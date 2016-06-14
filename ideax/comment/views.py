from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import View
from ideax.comment.forms import CommentForm
from ideax.comment.models import Comment
from notifications.signals import notify


@login_required
@transaction.atomic
def post_comment(request):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save()
        if comment.parent:
            comment.idea = comment.parent.idea
        comment.author = request.user.username
        comment.save()
        idea = comment.idea
        idea.comment_count = F('comment_count') + 1
        idea.save()
        if comment.parent:
            parent_author = get_user_model().objects.filter(
                username=comment.parent.author)
            target = comment.parent
        elif comment.idea:
            parent_author = [idea.author]
            target = idea
        if len(parent_author) == 1:
            notify.send(request.user,
                        recipient=parent_author[0],
                        verb='replied',
                        action_object=comment,
                        description=comment.text,
                        target=target)
        return HttpResponseRedirect(comment.idea.get_absolute_url())
    return HttpResponse(form.errors)


class CommentView(View):
    def get(self, request, id=None):
        comment = get_object_or_404(Comment, id=id)
        comments = [comment.parent] if comment.parent else []
        comments += [comment] + list(comment.children.all())
        return render(request, 'comment/comment.html', {
            'comments': comments,
            'hilight_id': comment.id,
        })
