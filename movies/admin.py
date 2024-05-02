from django.contrib import admin
from .models import Movie, MPAARating, Genre


class MovieInline(admin.StackedInline):
    model = Movie
    extra = 0

@admin.register(MPAARating)
class MPAARating(admin.ModelAdmin):
    inlines = [MovieInline,]

admin.site.register(Genre)