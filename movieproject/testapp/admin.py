from django.contrib import admin
from testapp.models import Movie
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["Releasedate","Moviename","Hero","Heroine","Rating"]