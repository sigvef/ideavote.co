from ideax.shortcuts import get_current_site


class CurrentSiteMiddleware():
    def process_request(self, request):
        request.site = get_current_site(request)
