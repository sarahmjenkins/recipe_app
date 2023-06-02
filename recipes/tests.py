from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm

# Tests to run:
# name value and max length
# cooking_time value
# ingredients value and max length
# rating value, max length, and default
# __str__ function

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Hot Chocolate',
            cooking_time='5',
            ingredients='milk, hot chocolate mix, marshmallows',
            rating='yum'
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name, 'name')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(recipe_name_max_length, 50)
    
    def test_recipe_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cooking_time = recipe._meta.get_field('cooking_time').verbose_name
        self.assertEqual(recipe_cooking_time, 'cooking time') # tests failed if I used 'cooking_time' instead of 'cooking time' which doesn't totally make sense
    
    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(id=1)
        recipe_ingredients = recipe._meta.get_field('ingredients').verbose_name
        self.assertEqual(recipe_ingredients, 'ingredients')

    def test_recipe_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        recipe_ingredients_max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(recipe_ingredients_max_length, 255)
    
    def test_recipe_rating(self):
        recipe = Recipe.objects.get(id=1)
        recipe_rating = recipe._meta.get_field('rating').verbose_name
        self.assertEqual(recipe_rating, 'rating')

    def test_recipe_rating_max_length(self):
        recipe = Recipe.objects.get(id=1)
        recipe_rating_max_length = recipe._meta.get_field('rating').max_length
        self.assertEqual(recipe_rating_max_length, 4)
    
    def test_recipe_rating_default(self):
        recipe = Recipe.objects.get(id=1)
        recipe_rating_default = recipe._meta.get_field('rating').default
        self.assertEqual(recipe_rating_default, 'na')
    
    def test_recipe_str(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.name)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')
    
class RecipeFormTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Hot Chocolate',
            cooking_time='5',
            ingredients='milk, hot chocolate mix, marshmallows',
            rating='yum'
        )

# Value of field
# Format of field
# Length of field
# protected view

    def test_form_input_value(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name = recipe._meta.get_field('name').verbose_name
        form = RecipeSearchForm()
        form_value = form.get(recipe_name)
        self.assertEqual(form_value, recipe_name)


    # def test_form_input_format:
    
    # def test_form_input_max_length:
    #     recipe = Recipe.objects.get(id=1)
    #     recipe_rating_max_length = recipe._meta.get_field('rating').max_length
    #     self.assertEqual(recipe_rating_max_l