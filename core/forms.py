from django.forms import ModelForm
from .models import CollegeReviews
class ReviewForm(ModelForm):


    class Meta:
        model = CollegeReviews
        fields='__all__'
        exclude = ['user', 'college','helpful']

