from django.urls import path 
from .views import home, RecipeListView, RecipeDetailView, search, about

app_name = 'recipes'

urlpatterns = [
    path('/', home),
    path('about/', about, name='about'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', search, name='search')
]