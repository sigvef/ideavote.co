from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ideax.comment.forms import CommentForm


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
        return HttpResponseRedirect(comment.idea.get_absolute_url())
    return HttpResponse(form.errors)
