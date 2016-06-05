from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ideas/', include('ideax.idea.urls')),
    url(r'', include('ideax.frontpage.urls')),
]
