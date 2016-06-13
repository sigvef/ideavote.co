from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^notifications', include('ideax.notify.urls')),
    url(r'^users/', include('ideax.user.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^comments/', include('ideax.comment.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ideas/', include('ideax.idea.urls')),
    url(r'', include('ideax.frontpage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
