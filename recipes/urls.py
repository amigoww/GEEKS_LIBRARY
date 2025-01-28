from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:recipe_id>/add-ingredient/', views.ingredient_create, name='ingredient_create'),
    path('delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),
]