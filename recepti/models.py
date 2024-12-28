from django.db import models


class RecipeModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class IngredientModel(models.Model):
    UNIT_CHOICES = [
        ('g', 'Граммы'),
        ('kg', 'Килограммы'),
        ('ml', 'Миллилитры'),
        ('l', 'Литры'),
        ('pcs', 'Штуки'),
    ]

    name = models.CharField(max_length=300)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='ingredients')


    def __str__(self):
        return f'{self.UNIT_CHOICES}:{self.name}'

