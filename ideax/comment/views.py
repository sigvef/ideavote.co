from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ideax.comment.forms import CommentForm


@login_required
def post_comment(request):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save()
        comment.author = request.user.username
        comment.save()
        return HttpResponseRedirect(comment.idea.get_absolute_url())
    return HttpResponse(form.errors)
