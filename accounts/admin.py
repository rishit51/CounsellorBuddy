from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(CounsellorProfile)
admin.site.register(AccessPurchase)