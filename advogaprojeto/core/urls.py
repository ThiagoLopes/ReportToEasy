"""advogaprojeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from core import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^registrar/$', views.registrar, name='registrar'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^gerar_documento$', views.gerar_documento, name='gerar_documento'),
    url(r'^cadastro$', views.cadastrar_documento, name='cadastrar_documento'),
    url(r'^documento/(?P<id_arquivo>\d+)$', views.documento, name='documento'),
    url(r'^delete/(?P<id_template>\d+)$', views.delete_template, name='delete')
]
