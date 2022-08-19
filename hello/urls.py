
from django.urls import path,include
from django.conf import settings
from hello import views
urlpatterns = [
    
    path('', views.hello,name='hello'),
    path('contact', views.contact,name='contact')
]