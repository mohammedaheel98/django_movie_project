from django.shortcuts import render
from testapp import forms 
from testapp.models import Movie
# Create your views here.
def home_page(request):
    return render(request,"testapp/index.html")

def add_movie_page(request):
    form = forms.MovieForm()
    if request.method == "POST":
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return home_page(request)
    return render(request,"testapp/addmovies.html",{"form":form})

def list_movies(request):
    movies_list = Movie.objects.all().order_by("Rating")
    return render(request,"testapp/listmovies.html",{"movies_list":movies_list})