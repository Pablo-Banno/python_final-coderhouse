from django import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
        path('', inicio, name='inicio'),

        #Blogs
        path('lista-blogs/', BlogLista.as_view(), name='lista-blogs'),
        path('detalle-blog/<pk>', BlogDetalle.as_view(), name='detalle-blog'),
        path('nuevo-blog/', BlogNuevo.as_view(), name='nuevo-blog'),
        path('editar-blog/<int:pk>/', BlogUpdate.as_view(), name='editar-blog'),
        path('eliminar-blog/<int:pk>/', BlogDelete.as_view(), name='eliminar-blog'),

        #Comentario
        path('detalle-blog/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

        #Users
        path('login/', LoginPagina.as_view(), name='login'),
        path('logout/', LogoutView.as_view(template_name='Musicapp/Users/logout.html'), name='logout'),
        path('registro/', RegistroPagina.as_view(), name='registro'),
        path('editar-perfil/', UsuarioEdicion.as_view(), name='editar-perfil'),
        path('password-cambiar/', CambioPassword.as_view(), name='cambiar-password'),
        path('password-exitoso/' , views.password_exitoso, name='password-exitoso'),

        path('about/', views.about, name='about'),
        ]

handler404 = 'Musicapp.views.page_not_found_view'