from django import forms
from recepti.models import RecipeModel, IngredientModel

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = "__all__"

class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientModel
        fields = "__all__"
