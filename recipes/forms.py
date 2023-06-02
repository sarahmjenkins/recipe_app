from django import forms

SEARCH_CHOICES = (
    ('1', 'Search by recipe name.'),
    ('2', 'Search by ingredient.')
)

class RecipeSearchForm(forms.Form):
    recipe_title = forms.CharField(max_length=50)
    recipe_ingredient = forms.CharField(max_length=50)
    search_type = forms.ChoiceField(choices=SEARCH_CHOICES)