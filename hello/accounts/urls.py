from django.urls import path
from.import views

app_name='accounts'
urlpatterns = [
     path('signup/',views.signup,name='signup'),
     path('log/',views.log,name='log'),
     path('logout/',views.log2,name='log2')
]
