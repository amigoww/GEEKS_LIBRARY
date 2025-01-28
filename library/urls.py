from django.urls import path
from . import views

urlpatterns =[
    path('about_me/', views.about_me, name='about_me'),
    path('my_pet/', views.my_pet, name='my_pet'),
    path('current_time/', views.current_time, name='current_time'),

    path('books/', views.book_list_view, name='book_list_view'),
    path('books/<int:id>/', views.book_detail_view, name='book_detail_view'),
]