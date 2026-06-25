from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, Ingredient


def home(request):
    return render(request, 'home.html')


def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})


def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe-index')

        error_message = 'Invalid sign up - try again'

    form = UserCreationForm()

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'registration/signup.html', context)


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'cuisine', 'description', 'cook_time']


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['name', 'cuisine', 'description', 'cook_time']


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe-index')


class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name', 'amount', 'recipe']
    success_url = reverse_lazy('recipe-index')


class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = ['name', 'amount', 'recipe']
    success_url = reverse_lazy('recipe-index')


class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy('recipe-index')