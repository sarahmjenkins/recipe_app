from django.db import models
from django.shortcuts import reverse

# Create your models here.
rating_choices = (
    ('yum', 'Yum'),
    ('meh', 'Meh'),
    ('yuck', 'Yuck')
)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooking_time = models.FloatField()
    ingredients = models.CharField(max_length=255)
    rating = models.CharField(max_length=4, choices=rating_choices, default='na')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 30 and len(ingredients) < 10:
            difficulty = 'Easy'
        if self.cooking_time < 30 and len(ingredients) >= 10:
            difficulty = 'Medium'
        if self.cooking_time >= 30 and len(ingredients) < 10:
            difficulty = "Intermediate"
        if self.cooking_time >= 30 and len(ingredients) >= 10:
            difficulty = "Hard"
        return difficulty

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})