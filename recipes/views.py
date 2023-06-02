from django.shortcuts import render
import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Recipe
from .forms import RecipeSearchForm
from .utils import get_chart

# Create your views here.

def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

@login_required
def search(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    chart = None

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        chart_type = request.POST.get('chart_type')

        qs = Recipe.objects.filter(name=recipe_name)
        
        if qs:
            recipes_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)
            recipes_df = recipes_df.to_html()

    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart
    }

    return render(request, 'recipes/search.html', context)