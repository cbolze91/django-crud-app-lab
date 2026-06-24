from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Recipe

def home(request):
    return render(request, 'home.html')

def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(
        request,
        'recipes/detail.html',
        {'recipe': recipe}
    )

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'cuisine', 'description', 'cook_time']