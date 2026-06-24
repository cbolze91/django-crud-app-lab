from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'recipe_id': self.id})


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name