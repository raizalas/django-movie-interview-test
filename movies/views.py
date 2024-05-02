from django.views import generic
from .models import Movie

# Create your views here.
class MovieListView(generic.ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "movie-list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(name__icontains=query)  # Adjust the search criteria as needed
        return queryset


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "movie-detail.html"