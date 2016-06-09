from django.contrib.sites.shortcuts import (
    get_current_site as original_get_current_site)
from django.contrib.sites.models import Site


def get_current_site(request):
    try:
        current_site = original_get_current_site(request)
    except Site.DoesNotExist:
        current_site = Site.objects.all()[0]
    return current_site
