from django.shortcuts import render
from Musicapp.models import Blog, Comentario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordChangeView

from .forms import *

#MIXINS (Permiso para leer clases)
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'Musicapp/inicio.html')

#-------- BLOGS ------------------------------------------------------------
class BlogLista(LoginRequiredMixin, ListView):
    queryset = Blog.objects.all()
    template_name = 'Musicapp/Blogs/lista-blogs.html'

class BlogDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'Musicapp/Blogs/detalle-blog.html'

class BlogNuevo(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = FormularioNuevoBlog
    success_url = reverse_lazy('lista-blogs')
    template_name = 'Musicapp/Blogs/nuevo-blog.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogNuevo, self).form_valid(form)

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = FormularioActualizacionBlog
    success_url = reverse_lazy('lista-blogs')
    template_name = 'Musicapp/Blogs/editar-blog.html'

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('lista-blogs')
    template_name = 'Musicapp/Blogs/eliminar-blog.html'

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'Musicapp/Blogs/comentario.html'
    success_url = reverse_lazy('lista-blogs')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

#-------- USUARIOS ---------------------------------------------------------
class LoginPagina(LoginView):
    template_name = 'Musicapp/Users/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('lista-blogs')

    def get_success_url(self):
        return reverse_lazy('lista-blogs')

class RegistroPagina(FormView):
    template_name = 'Musicapp/Users/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'Musicapp/Users/editar-perfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'Musicapp/Users/password-cambiar.html'
    success_url = reverse_lazy('password-exitoso')

def password_exitoso(request):
    return render(request, 'Musicapp/Users/password-exitoso.html', {})

# ACERCA DE MI

def about(request):
    return render(request, 'Musicapp/about.html', {})

# PAGE NOT FOUND

def page_not_found_view(request, exception):
    return render(request, 'Musicapp/404.html')