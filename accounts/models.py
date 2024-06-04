from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from allauth.account.signals import user_signed_up
from core.models import Branch, College
import uuid
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='ADMIN','Admin'
        STUDENT="STUDENT",'Student'
        COUNSELLOR='COUNSELLOR','Counsellor'

    base_role=Role.ADMIN

    role=models.CharField(max_length=50,choices=Role.choices)

    def save(self,*args, **kwargs) :
               return super().save( *args, **kwargs)
class StudentManager(BaseUserManager):
     def get_queryset(self,*args,**kwargs):
          results=super.get_queryset( *args, **kwargs).filter(role=User.Role.STUDENT)
          return results
     
class Student(User):
     base_role=User.Role.STUDENT
     student=StudentManager()

     class Meta:
          proxy=True

class CounsellorManager(BaseUserManager):
     def get_queryset(self,*args,**kwargs):
          results=super.get_queryset( *args, **kwargs).filter(role=User.Role.COUNSELLOR)
          return results
     
class Counsellor(User):
     base_role=User.Role.COUNSELLOR
     student=CounsellorManager()
     class Meta:
          proxy=True

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',editable=False)
    student_id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    counselors = models.ManyToManyField('CounsellorProfile', through='AccessPurchase')
    def __str__(self):
        return self.user.username
@receiver(user_signed_up)
def create_student_profile(sender,request,user,**kwargs):
     if user.role=="STUDENT":
          StudentProfile.objects.create(user=user)   

year_choices=[(1,'1st Year',),( 2,'2nd Year' ),(3,'3rd Year'),(4,'4th Year',), ]

class CounsellorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='counsellor_profile')
    name = models.CharField(max_length=60)
    year = models.IntegerField(choices=year_choices, default=1)
    college = models.ForeignKey(College, related_name='counsellors', on_delete=models.CASCADE, default=None)
    counsellor_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=200)
    image = models.ImageField(upload_to='counsellors', blank=True, null=True, default='college/images/default/defaultistockphoto-1495088043-612x612.jpg')

    class Meta:
          verbose_name_plural = "Counsellor Profiles"
    def __str__(self):
        return self.user.username

def get_default_college():
    return College.objects.first()  # Return the first college instance, or None if there are no colleges.


@receiver(user_signed_up)
def create_counsellor_profile(sender, request, user, **kwargs):
    if user.role == "COUNSELLOR":
        CounsellorProfile.objects.create(user=user, branch=Branch.objects.first(), college=get_default_college())

class AccessPurchase(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    counselor = models.ForeignKey('CounsellorProfile', on_delete=models.CASCADE)
    purchase_timestamp = models.DateTimeField(auto_now_add=True)
    room_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
