"""Blog_con_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.index, name="index"),
    path('detalle-entrada/<int:entrada_id>', mainapp.views.detalle_entrada, name="detalle_entrada"),
    path('registro/', mainapp.views.registro_usuario, name="registro_usuario"),
]

#Ruta para imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
