from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Movie, Person
from movies.forms import MyUserCreationForm


def index(request):
    if 'title' in request.GET:
        objects = Movie.objects.filter(
            title__icontains=request.GET['title'])
    else:
        objects = Movie.objects.all()
    return render(request, 'index.html',
                  {'objects': objects})


def movie_detail(request, movie_id):
    return render(request, 'movie_detail.html',
                  {'object': Movie.objects.get(pk=movie_id)})


def actor_detail(request, actor_id):
    person = Person.objects.get(pk=actor_id)
    movies = Movie.objects.filter(characters__person=person)
    return render(request, 'actor_detail.html', {
        'object': person,
        'movies': movies
    })


def register_user(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, 'register.html', {
        "form": form
    })


def login_user(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')

    return render(request, 'login.html', {
        "form": form
    })


def logout_user(request):
    logout(request)
    return redirect('/')
