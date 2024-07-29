from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
    
    def validate_ingredients(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("At least one ingredient must be provided")
        return value
    
    def validate_instructions(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("At least one instruction must be provided")
        return value
    
    def validate_time_to_cook(self, value):
        if value < 1:
            raise serializers.ValidationError("Time to cook must be a positive integer")
        return value
    
    def validate_difficulty_level(self, value):
        if value not in ['easy', 'medium', 'hard']:
            raise serializers.ValidationError("Difficulty level must be one of 'easy', 'medium', or 'hard'")
        return value
    
    def validate_user_full_name(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("User full name must be provided")
        return value
    
    def validate(self, data):
        user_email = data.get('user_email')
        if not user_email:
            raise serializers.ValidationError("User email must be provided")
        if Recipe.objects.filter(user_email=user_email, name=data.get('name')).exists():
            raise serializers.ValidationError("Recipe with the same name and user email already exists")
        # For update operation, exclude the current instance
        if self.instance and Recipe.objects.filter(user_email=user_email, name=data.get('name')).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("Another recipe with the same name and user email already exists")
        if not data.get('image') and not data.get('image_url'):
            raise serializers.ValidationError('Either image or image_url must be provided.')
    
        return data
    