from django.contrib import admin
from django.urls import path
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios', include("apps.usuarios.urls"), name="usuarios"),
]
