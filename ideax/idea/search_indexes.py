from haystack import indexes
from ideax.idea.models import Idea


class IdeaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    site = indexes.CharField()
    author = indexes.CharField()
    archived = indexes.BooleanField()

    def get_model(self):
        return Idea

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
