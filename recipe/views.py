from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Recipe
from .serializers import RecipeSerializer


@api_view(http_method_names=['get', 'post'])
def RecipeApiList(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        
        return Response(serializer.data)
    else:
        serializer = RecipeSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view()
def RecipeApiDetail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # recipe = Recipe.objects.filter(pk=pk).first()
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)
