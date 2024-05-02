from django.urls import path
from .views import MovieListView, MovieDetailView


urlpatterns = [
    path('', MovieListView.as_view() , name='movies'),
    path('movies/<int:pk>',MovieDetailView.as_view(), name='movie-detail'),
]