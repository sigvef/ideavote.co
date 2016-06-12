from django import template
from django.core.paginator import Paginator

register = template.Library()


@register.inclusion_tag('idea/idea_list.html')
def idea_list(ideas, page, user, paging_url_prefix=''):
    paginator = Paginator(ideas, 15)
    ideas_page = paginator.page(page)
    return {
        'ideas_page': ideas_page,
        'user': user,
        'paging_url_prefix': paging_url_prefix,
    }
