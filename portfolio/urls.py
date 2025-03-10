from django.urls import path
from .views import *

urlpatterns = [
    path('', main ,name="home" ),
    path('contact/', contact_view, name='contact'),
   
]
