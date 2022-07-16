from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import render
from .models import Category, Photo

# Criando as views que visualização as paginas do startapp photos

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos}  
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    return render(request, 'photos/add.html')

