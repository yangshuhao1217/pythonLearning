from django.shortcuts import render

def index(request):
    """The home page for meal_plan."""
    return render(request, 'meal_plans/index.html')
