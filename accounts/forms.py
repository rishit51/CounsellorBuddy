from allauth.account.forms import SignupForm
from django import forms
from .models import User, StudentProfile,CounsellorProfile
from django.urls import reverse
import PIL.Image as Image
class CustomSignupForm(SignupForm):
    role = forms.ChoiceField(choices=User.Role.choices,required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter choices to include only STUDENT and COUNSELLOR
        self.fields['role'].choices = [
            (choice, label) for choice, label in self.fields['role'].choices
            if choice in [User.Role.STUDENT, User.Role.COUNSELLOR]
        ]
    def custom_signup(self, request, user):
        user.role=self.cleaned_data['role']
        user.save()
        return super().custom_signup(request, user) 
  

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        
        exclude=('counsellors',)
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }
        def save(self, *args, **kwargs):
            super().save()

            img = Image.open(self.image.path)

            if img.height > 100 or img.width > 100:
                new_img = (100, 100)
                img.thumbnail(new_img)
                img.save(self.image.path)

class CounsellorProfileForm(forms.ModelForm):

    class Meta:
        model=CounsellorProfile
        fields="__all__"
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }
        labels={'image':'Profile Image'}
        def save(self, *args, **kwargs):
            super().save()

            img = Image.open(self.image.path)

            if img.height > 100 or img.width > 100:
                new_img = (100, 100)
                img.thumbnail(new_img)
                img.save(self.image.path)