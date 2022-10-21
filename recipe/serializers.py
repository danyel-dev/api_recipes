from .models import Recipe, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField(method_name='any_method_name')
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    category_name = serializers.StringRelatedField(
        source='category'
    )
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )

    def any_method_name(self, Recipe):
        return f'{Recipe.preparation_time} {Recipe.preparation_time_unit}'
    