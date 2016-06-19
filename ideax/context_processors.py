from ideax import settings


def google_analytics(request):
    return {
        'GOOGLE_ANALYTICS_KEY': settings.GOOGLE_ANALYTICS_KEY
    }


def site_permissions(request):
    context = {
        'IS_MODERATOR': False,
        'IS_OWNER': False,
    }
    if not request.user.is_authenticated():
        return context

    if request.user.owned_sites.filter(
            id=request.site.settings.id).count():
        context['IS_OWNER'] = True

    if request.user.moderator_sites.filter(
            id=request.site.settings.id).count():
        context['IS_MODERATOR'] = True

    return context
