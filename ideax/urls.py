from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^search/', include('haystack.urls')),
    url(r'^notifications', include('ideax.notify.urls')),
    url(r'^users/', include('ideax.user.urls')),
    url(r'^accounts/register/complete/', RedirectView.as_view(url='/')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^comments/', include('ideax.comment.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ideas/', include('ideax.idea.urls')),
    url(r'^social/', include('social.apps.django_app.urls',
                             namespace='social')),
    url(r'', include('ideax.frontpage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
