from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FoodEntryForm
from .models import FoodEntry

# Create your views here.
def home(request):
    return render(request, 'tracker/home.html')

@login_required
def food_list(request):
    entries = FoodEntry.objects.filter(user=request.user).order_by("-eaten_at")
    return render(request, "tracker/food_list.html", {"entries": entries})

@login_required
def food_create(request):
    if request.method == "POST":
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("food_list")
    else:
        form = FoodEntryForm()
    return render(request, "tracker/food_form.html", {"form": form})