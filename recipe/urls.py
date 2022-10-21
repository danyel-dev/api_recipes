from django.urls import path
from .views import RecipeApiList


urlpatterns = [
    path('', RecipeApiList, name='recipe_list'),
]
