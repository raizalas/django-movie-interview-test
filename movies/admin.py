from django.contrib import admin
from .models import Movie, MPAARating, Genre

# Register your models here.
admin.site.register(Movie)
admin.site.register(MPAARating)
admin.site.register(Genre)
