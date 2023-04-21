from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    generoSeleccion = (
    ('rock','Rock'),
    ('pop', 'Pop'),
    ('clasica','Clasica'),
    ('punk','Punk'),
    ('trap','Trap'),
    ('reggaeton','Reggaeton'),
    ('cumbia','Cumbia'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=15, choices=generoSeleccion, default='Rock')
    descripcion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagenBlog = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey(Blog, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)