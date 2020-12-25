from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Entrada(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")


    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created_at']#para ordenar por fecha de creado
    

    def __str__(self):
        return self.title 
