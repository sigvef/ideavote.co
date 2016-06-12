from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ideax.comment.forms import CommentForm
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
        parent_author = get_user_model().objects.filter(
            username=comment.parent.author)
        if len(parent_author) == 1:
            notify.send(request.user,
                        recipient=parent_author[0],
                        verb='replied',
                        action_object=comment,
                        description=comment.text,
                        target=comment.parent)
        return HttpResponseRedirect(comment.idea.get_absolute_url())
    return HttpResponse(form.errors)
