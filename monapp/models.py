from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    height = models.FloatField()
    weight = models.FloatField()
    diet = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Recipe(models.Model):
    description = models.TextField()
    ingredients = models.TextField()  
    instructions = models.TextField()
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()
    source = models.CharField(max_length=255)
    img = models.ImageField(upload_to='recipes/')
    category = models.CharField(max_length=50)  
    created_at = models.DateTimeField(auto_now_add=True)

class SavedRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='saved_by_users')
    created_at = models.DateTimeField(auto_now_add=True)


class ScrapedRecipe(Recipe):
    website_source = models.CharField(max_length=255)


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nutrients = models.TextField()
    quantity = models.FloatField()

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_recipes')


class Alergie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alergies')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='alergies')
    type = models.CharField(max_length=100)