from django.contrib import admin
from .models import FoodEntry

@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    list_display = ("eaten_at", "name", "calories", "protein_g", "carbs_g", "fat_g", "user")
    list_filter = ("user",)
    search_fields = ("name",)
    ordering = ("-eaten_at",)