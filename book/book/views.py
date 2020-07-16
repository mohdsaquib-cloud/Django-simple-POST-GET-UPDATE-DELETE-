from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from .models import Books


def home(request):
    return render(request, 'home.html')


def books(request):
    context = {
        "books": Books.objects.all()
    }
    return render(request, 'books.html', context)


def update(request):
    if request.method == "POST":
        id = request.POST.get("id")
        bookName = request.POST.get("bookName")
        id = int(id)
        b = Books.objects.get(pk=id)
        b.name = bookName
        b.save()
        context = {
            "books": Books.objects.all()
        }
        return render(request, 'books.html', context)
    else:
        return render(request, 'update.html')


def delete(request):
    if request.method == "POST":
        id = int(request.POST.get("id"))
        b = Books.objects.get(pk=id)
        b.delete()
        return redirect('/books')
    else:
        return render(request, 'delete.html')


def addBook(request):
    if request.method == "POST":
        bookName = request.POST.get("bookName")
        Books(name=bookName).save()
        return redirect('/books')
    else:
        return render(request, 'addBook.html')


def book(request, id):
    if request.method == 'POST':
        return HttpResponse({"id": 1})
    else:
        b = Books.objects.get(pk=id)
        context = {
            "question_id": id,
            "name": b.name
        }
        return render(request, 'book.html', context)
    return HttpResponse("Not Found")
