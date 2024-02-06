from django.shortcuts import render
from books.models import Book

from django.http import  HttpResponse

def home(request):
    return render(request,'home.html')
def addbooks(request):
    return render(request,'addbooks.html')
def viewbooks(request):
    k=Book.objects.all()
    return render(request,'viewbooks.html',{'b':k})