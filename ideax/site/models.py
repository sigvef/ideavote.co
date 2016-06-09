from django.contrib.sites.models import Site
from django.db import models


class SiteSettings(models.Model):
    banner_image = models.ImageField(null=True)
    site = models.ForeignKey(Site, related_name='settings')

    def __unicode__(self):
        return 'SiteSettings[#%s, %s]' % (self.id, self.site.domain)
