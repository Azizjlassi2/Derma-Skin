from django.db import models
from django.contrib import admin

from Accounts.models import AppUser
# Create your models here.

class Description(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question 
    
 
class QuestionQCM(models.Model):
    
    
    question = models.CharField(max_length=200)


    def __str__(self):
        return self.question 

    
class Response(models.Model):
    
    CHOISES = (("YES","YES"),("NO","NO"))
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionQCM,on_delete=models.CASCADE)

    response = models.CharField(max_length=10,choices=CHOISES)
    def __str__(self):
        return self.response 
 
class Result(models.Model):
    user = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    result = models.CharField(max_length=20)
    
    def __str__(self):
        return self.result
  
class DoctorRequest(models.Model):
    Genre = (
        ('Homme','Homme'),
        ('Femme','Femme')
    )

    doctor_name = models.CharField(max_length=50)
    doctor_email = models.EmailField()
    doctor_gouvernerat = models.CharField(max_length=50)
    doctor_city = models.CharField(max_length=50)
    doctor_genre = models.CharField(null=False,max_length=20, default="Homme", choices=Genre)
    doctor_age = models.IntegerField()
    doctor_password = models.CharField(max_length=50)
    doctor_phone = models.CharField(max_length=50)
    profil_image = models.ImageField(blank=True,null=True,upload_to='pics/')
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doctor_name
 



class ContactMessage(models.Model):

    user_id = models.CharField(max_length=30,blank=True)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    

    def __str__(self):
        return self.subject
    




class Test(models.Model):

    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='test/images/')
    result = models.CharField(max_length=50)
    tested_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user_name 
