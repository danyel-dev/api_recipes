from django.urls import path
from .views import RecipeApiList, RecipeApiDetail


urlpatterns = [
    path('', RecipeApiList, name='recipe_list'),
    path('<int:pk>/', RecipeApiDetail, name='recipe_detail'),
]
