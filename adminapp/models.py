from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class course(models.Model):
    course_name=models.CharField(max_length=255)
    course_fee=models.IntegerField()



class student(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=200)
    student_address=models.CharField(max_length=200)
    student_age=models.IntegerField()
    join_date=models.DateField()



class usermember(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    user_address=models.CharField(max_length=255)
    user_gender=models.CharField(max_length=255)
    user_mobile=models.CharField(max_length=255)
    user_photo=models.ImageField(upload_to="image/",null=True)
    
