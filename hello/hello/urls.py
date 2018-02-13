from django.contrib import admin
from django.urls import path,include
from .import views
import re
from django.conf.urls.static import static
from django.conf import settings

app_name="hello"
urlpatterns = [
    path('',include('arti.urls')),
    path('admin/', admin.site.urls),
    path('about/',views.about,name='about'),
    path('main/',views.main,name='main'),
    path('accounts/',include('accounts.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
