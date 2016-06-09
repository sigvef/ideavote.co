from django import forms
from ideax.comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('parent', 'idea', 'text')

    def is_valid(self, *args, **kwargs):
        super_is_valid = super(CommentForm, self).is_valid(*args, **kwargs)
        idea_or_parent_is_present = (self.fields['idea'] or
                                     self.fields['parent'])
        return idea_or_parent_is_present and super_is_valid
