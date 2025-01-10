from django.shortcuts import render, redirect
from .models import FoodEntry
from .forms import FoodEntryForm

def index(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FoodEntryForm()
    
    entries = FoodEntry.objects.all()
    total_calories = sum(entry.calories for entry in entries)
    return render(request, 'tracker/index.html', {
        'form': form,
        'entries': entries,
        'total_calories': total_calories,
    })
