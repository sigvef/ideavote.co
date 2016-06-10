from django.http import Http404
from ideax.shortcuts import get_current_site
from ideax.site.models import SiteSettings


class CurrentSiteMiddleware():
    def process_request(self, request):
        request.site = get_current_site(request)
        try:
            request.site_settings = SiteSettings.objects.get(
                site_id=request.site.id)
        except SiteSettings.DoesNotExist:
            raise Http404
