# -*-coding: utf-8 -*-
from django.shortcuts import render
from models import *

def home(request):
    
    noticias = Noticia.objects.all()

    for n in noticias:
        if(n.categoria == 'politicas-publicas'):
            n.categoria = 'Políticas Públicas'
        if(n.categoria == 'sociedade'):
            n.categoria = 'Sociedade'
        if(n.categoria == 'seus-deveres'):
            n.categoria = 'Seus Deveres'
        if(n.categoria == 'poderes'):
            n.categoria = 'Poderes'
        if(n.categoria == 'atualidades'):
            n.categoria = 'Atualidades'

    return render(request,"home.html",{'noticias':noticias})

def noticia(request,id):
    
    noticia = Noticia.objects.filter(id = id).get()
    imagens = Imagem.objects.filter(noticia = id)
    return render(request,"noticia.html",{'noticia':noticia, 'imagens':imagens})

def noticias_categoria(request,categoria):

    noticias = Noticia.objects.filter(categoria = categoria)
    
    cat = 'Sem Categoria'

    if(categoria == 'politicas-publicas'):
        cat = 'Políticas Públicas'
    if(categoria == 'sociedade'):
        cat = 'Sociedade'
    if(categoria == 'seus-deveres'):
        cat = 'Seus Deveres'
    if(categoria == 'poderes'):
        cat = 'Poderes'
    if(categoria == 'atualidades'):
        cat = 'Atualidades'

    return render(request,"noticias-categoria.html",{'noticias':noticias, 'cat':cat})
