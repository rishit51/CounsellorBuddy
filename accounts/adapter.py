from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from .models import User
from django.urls import reverse

class MyAccountAdapter(DefaultAccountAdapter):

    def get_signup_redirect_url(self, request):
        user=request.user
        role=user.role
        if role == User.Role.STUDENT:
            return reverse('student_profile_creation')  # Replace with your URL name for student profile creation
        elif role == User.Role.COUNSELLOR:
            return reverse('counsellor_profile_creation')
        