from django.db import models
from django.conf import settings

# Create your models here.
class FoodEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    eaten_at = models.DateTimeField()
    name = models.CharField(max_length=200)
    calories = models.FloatField()
    protein_g = models.FloatField(default=0)
    carbs_g = models.FloatField(default=0)
    fat_g = models.FloatField(default=0)
    serving_size = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["-eaten_at"]

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"