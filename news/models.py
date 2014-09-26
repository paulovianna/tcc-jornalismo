# -*-coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from thumbs import ImageWithThumbsField
from redactor.fields import RedactorField


class Noticia(models.Model):
    
    titulo = models.CharField('Título', max_length=128)
    conteudo = RedactorField(verbose_name=u'Conteúdo',allow_file_upload=False,allow_image_upload=False)
    data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = _('Noticia')
        verbose_name_plural = _('Noticias')
        ordering = ['-id']

    def __unicode__(self):
        return self.titulo


class Imagem(models.Model):
    
    descricao = models.TextField('Descrição')
    imagem = ImageWithThumbsField(upload_to='imagens', sizes=((125,125),(800,600)))
    noticia = models.ForeignKey(Noticia)

    class Meta:
        verbose_name = _('Imagem')
        verbose_name_plural = _('Imagens')

    def __unicode__(self):
        return self.imagem.name
    