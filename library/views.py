from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Book

def about_me(request):
    return HttpResponse("This is Amir's page!")

def my_pet(request):
    return render(request, 'my_pet.html')

def current_time(request):
    return HttpResponse(datetime.datetime.now())

def book_list_view(request):
    if request.method == 'GET':
        book_list = Book.objects.all()
        return render(request, 'books/book.html', {'books_list': book_list})

def book_detail_view(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_detail.html', {'book': book})



