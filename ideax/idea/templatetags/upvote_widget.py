from django import template

register = template.Library()


@register.inclusion_tag('idea/upvote_widget.html')
def upvote_widget(idea, user):
    upvoted = (idea.upvoters.filter(id=user.id).exists()
               if user.is_authenticated
               else False)
    return {
        'upvoted': upvoted,
        'idea': idea,
    }
