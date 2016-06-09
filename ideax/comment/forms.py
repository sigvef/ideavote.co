from django import forms
from ideax.comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('parent', 'idea', 'text')
