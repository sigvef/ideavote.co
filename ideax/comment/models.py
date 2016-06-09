from django.db import models
from django.utils import timezone
from ideax.idea.models import Idea
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class Comment(MPTTModel):
    author = models.CharField(null=False, max_length=256)
    idea = models.ForeignKey(Idea, null=True, blank=True)
    parent = TreeForeignKey(
        'self', related_name='children', null=True, db_index=True, blank=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def get_reply_form(self):
        from ideax.comment.forms import CommentForm
        form = CommentForm({
            'parent': self,
            'idea': self.idea,
        })
        return form

    def __unicode__(self):
        return 'Comment[#%s]' % self.id

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.id:
            self.created_at = self.created_at or now
        self.updated_at = self.updated_at or now
        return super(Comment, self).save(*args, **kwargs)
