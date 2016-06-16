from django.conf import settings as django_conf_settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from taggit.managers import TaggableManager
import markdown


class Idea(models.Model):
    slug_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=256, blank=True)
    text = models.TextField(blank=True)
    author = models.ForeignKey(django_conf_settings.AUTH_USER_MODEL,
                               related_name='authored_ideas',
                               null=True)
    upvoters = models.ManyToManyField(django_conf_settings.AUTH_USER_MODEL,
                                      related_name='upvoted_ideas',
                                      blank=True)
    comment_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    site = models.ForeignKey(Site, null=True)
    tags = TaggableManager()
    archived = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Idea[#%s, title: %s]' % (self.pk, self.title)

    def get_absolute_url(self):
        return '/ideas/%s/%s' % (self.slug_id, slugify(self.title))

    def get_rendered_text(self):
        return markdown.markdown(
            self.text,
            output_format='html5',
            safe_mode='escape')

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.id:
            self.created_at = self.created_at or now
            self.slug_id = get_random_string(length=4)
        self.updated_at = self.updated_at or now
        return super(Idea, self).save(*args, **kwargs)

    def get_notify_target_name(self):
        return 'idea'
