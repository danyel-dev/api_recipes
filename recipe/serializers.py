from collections import defaultdict
from .models import Recipe
from rest_framework import serializers
from django.contrib.auth.models import User


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'public', 'preparation', 'category', 'category_name', 'author']

    public = serializers.BooleanField(source='is_published', read_only=True)
    preparation = serializers.SerializerMethodField(method_name='any_method_name')
    category_name = serializers.StringRelatedField(
        source='category'
    )
    # author = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    # )

    def any_method_name(self, Recipe):
        return f'{Recipe.preparation_time} {Recipe.preparation_time_unit}'
    

    def validate(self, attrs):
        fields = attrs
        my_erros = defaultdict(list)

        title = fields.get('title')
        description = fields.get('description')
        
        if title == description:
            my_erros['title'].append('Title não pode ser igual ao description')
            my_erros['description'].append('description não pode ser igual ao Title')

        if my_erros:
            raise serializers.ValidationError(my_erros)

        return super().validate(attrs)


    # def validate_title(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError('Title muito curto')
        
    #     return value + 'oiiiii'
