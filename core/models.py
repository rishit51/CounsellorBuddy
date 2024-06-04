from django.db import models

# Create your models here.
class College(models.Model):
    name=models.CharField(max_length=100)
    address = models.TextField()
    rating=models.DecimalField(max_digits=2, decimal_places=1)
    history=models.TextField()
    def __str__(self):
        return self.name
    

class CollegeReviews(models.Model):
    user=models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    college=models.ForeignKey(College,on_delete=models.CASCADE,related_name='reviews')
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    body=models.TextField()
    helpful=models.IntegerField(default=0)
    

    

    def __str__(self):
        return self.user.username
    

    



class Branch(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    colleges=models.ManyToManyField(College)
    class Meta:
        ordering=['name']
    def __str__(self):
        return self.name


class CollegeImage(models.Model):
    college=models.ForeignKey(College, on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to="college/images")
