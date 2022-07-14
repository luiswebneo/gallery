from django.contrib import admin

# Registrando os modelos de bancos de dados  para o painel admin.

from .models import Photo, Category

admin.site.register(Category)
admin.site.register(Photo)

