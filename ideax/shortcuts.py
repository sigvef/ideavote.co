from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import (
    get_current_site as original_get_current_site)
from django.http import Http404


def get_current_site(request):
    try:
        current_site = original_get_current_site(request)
    except Site.DoesNotExist:
        raise Http404
    return current_site
