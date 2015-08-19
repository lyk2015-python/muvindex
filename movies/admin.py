from django.contrib import admin
from .models import Movie, Person, Character, Genre

# Register your models here.

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Character)
admin.site.register(Genre)