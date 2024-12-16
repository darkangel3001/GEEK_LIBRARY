from django import forms
from Basket.models import BasketModel

class BasketForm(forms.ModelForm):
    class Meta:
        model = BasketModel
        fields = "__all__"