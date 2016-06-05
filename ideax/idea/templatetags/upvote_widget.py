from django import template

register = template.Library()


@register.inclusion_tag('idea/upvote_widget.html')
def upvote_widget(idea):
    return {
        'idea': idea,
    }
