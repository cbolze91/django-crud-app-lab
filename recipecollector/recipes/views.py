from django.shortcuts import render
from .models import Recipe

def home(request):
    return render(request, 'home.html')

def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})