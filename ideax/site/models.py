from django.contrib.sites.models import Site
from django.db import models
from django.conf import settings


class SiteSettings(models.Model):
    banner_image = models.ImageField(null=True)
    site = models.ForeignKey(Site, related_name='settings')
    moderators = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='moderator_sites')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='owned_sites',
                              null=True)

    def __unicode__(self):
        return 'SiteSettings[#%s, %s]' % (self.id, self.site.domain)
