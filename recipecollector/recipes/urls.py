from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_index, name='recipe-index'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe-delete'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredient-create'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredient-delete'),
    path(
    'ingredients/<int:pk>/update/',
    views.IngredientUpdate.as_view(),
    name='ingredient-update'
),
    path('accounts/signup/', views.signup, name='signup'),
]