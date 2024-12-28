from django.contrib import admin
from .models import RecipeModel, IngredientModel

admin.site.register(RecipeModel)
admin.site.register(IngredientModel)