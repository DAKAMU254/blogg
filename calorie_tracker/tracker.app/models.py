from django.db import models

class FoodEntry(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
