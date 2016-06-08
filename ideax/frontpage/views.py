from django.views.generic import View
from ideax.idea.views import HotIdeaListView


class FrontpageView(View):
    def get(self, request):
        return HotIdeaListView().get(request, page=1)
