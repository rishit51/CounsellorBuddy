from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('profile/',profile),
    path('college/',colleges,name='colleges'),
    path('college/<str:id>',college,name='college'),
    
]
