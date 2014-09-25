# -*-coding: utf-8 -*-
from django.shortcuts import render
from models import *

def home(request):
    
    noticias = Noticia.objects.all()
    return render(request,"home.html",{'noticias':noticias})

def noticia(request,id):
    
    noticia = Noticia.objects.filter(id = id).get()
    imagens = Imagem.objects.filter(noticia = id)
    return render(request,"noticia.html",{'noticia':noticia, 'imagens':imagens})
