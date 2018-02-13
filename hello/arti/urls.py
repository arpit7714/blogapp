#this is the second web app
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
app_name='arti'

urlpatterns=[
 path('arti/',views.arti,name="arti"),
 path('create/',views.create,name="create")
]
