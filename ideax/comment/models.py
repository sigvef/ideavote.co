from django.db import models
from ideax.idea.models import Idea
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class Comment(MPTTModel):
    author = models.CharField(null=False, max_length=256)
    idea = models.ForeignKey(Idea, null=True)
    parent = TreeForeignKey(
        'self', related_name='children', null=True, db_index=True)
    text = models.TextField(blank=True)
