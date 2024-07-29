from django.db import models
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    time_to_cook = models.IntegerField(help_text='Time to cook in minutes')
    difficulty_level = models.CharField(max_length=20, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    created_at = models.DateTimeField(default=timezone.now)
    user_email = models.EmailField()
    user_full_name = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    