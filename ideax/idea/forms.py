from django import forms
from ideax.idea.models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'text')


class IdeaTagForm(forms.Form):
    tags = forms.CharField()
