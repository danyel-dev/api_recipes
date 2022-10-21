from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Recipe
from .serializers import RecipeSerializer


@api_view()
def RecipeApiList(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view()
def RecipeApiDetail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # recipe = Recipe.objects.filter(pk=pk).first()
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)
