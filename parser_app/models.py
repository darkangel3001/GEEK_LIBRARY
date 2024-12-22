from django.db import models

class ManasModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title