from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView,View
from django.urls import reverse_lazy

from .forms import LibroForm
from django.http import HttpResponseRedirect
from django.shortcuts import reverse,render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib.auth import authenticate, login

#class home(TemplateView):
    #template_name = 'index.html'
    
class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Manejar el caso en el que la autenticación falla, por ejemplo, mostrar un mensaje de error.
            return render(self.request, self.template_name, {'form': form, 'error_message': 'Invalid login credentials'})

            
class LogoutView(LogoutView):
    next_page = 'login'
    

