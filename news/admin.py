# -*-coding: utf-8 -*-
from models import *
from django.contrib import admin
from models import Noticia, Imagem

class ImagemInline(admin.TabularInline):
    model = Imagem

class NoticiaAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]
    list_display = ('titulo', 'categoria')

admin.site.register(Noticia,NoticiaAdmin)