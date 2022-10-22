from django.urls import path
from .views import RecipeApiList, RecipeApiDetail


urlpatterns = [
    path('recipes/', RecipeApiList, name='recipe_list'),
    path('recipes/<int:pk>/', RecipeApiDetail, name='recipe_detail'),
]
