from django.db import models
from django.utils.text import slugify
from django.conf import settings as django_conf_settings


class Idea(models.Model):
    slug_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=256, blank=True)
    text = models.TextField(blank=True)
    author = models.ForeignKey(django_conf_settings.AUTH_USER_MODEL,
                               related_name='authored_ideas')
    upvoters = models.ManyToManyField(django_conf_settings.AUTH_USER_MODEL,
                                      related_name='upvoted_ideas',
                                      blank=True)

    def __unicode__(self):
        return 'Idea[#%s, title: %s]' % (self.pk, self.title)

    def get_absolute_url(self):
        return '/ideas/%s/%s' % (self.slug_id, slugify(self.title))
