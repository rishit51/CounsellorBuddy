from django.urls import path
from .views import *

urlpatterns = [
    path('onboard/',create_profile,name='onboard'),
    path('profile/',profile_view,name='profile')
]
