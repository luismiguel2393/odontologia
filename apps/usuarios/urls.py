
from django.urls import path
#from .views import RegistroView, CustomLoginView
from django.contrib.auth.views import * 
#from . import views



app_name = 'usuarios'

urlpatterns = [
    #path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    #path('logout/', views.logout_view, name='logout'),
    

]


