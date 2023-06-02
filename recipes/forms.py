from django import forms

SEARCH_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

class RecipeSearchForm(forms.Form):
    chart_type = forms.ChoiceField(choices=SEARCH_CHOICES)
    recipe_name = forms.CharField(max_length=50)
    