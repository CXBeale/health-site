from django import forms
from .models import FoodEntry

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ["eaten_at", "name", "calories", "protein_g", "carbs_g", "fat_g", "serving_size"]
        widgets = {
            "eaten_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }