from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user = (
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
        (4, 'PARENT'),
    )

    user_type = models.CharField(choices=user , max_length=50 , default = 1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Course(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length = 100)
    session_end = models.CharField(max_length = 100)

    def __str__(self):
        return self.session_start + " to " + self.session_end
    
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length= 100)
    course_id = models.ForeignKey(Course , on_delete = models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year , on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.admin.username
    
class Subject(models.Model):
    