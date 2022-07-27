from pyexpat import model
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from colorfield.fields import ColorField

choices = (
    ('Doctor', "Doctor"),
    ('Patient', 'Patient'),
)
Country = (
    ('India', 'India'),
)
state_choices = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
                 ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
                 ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"),
                 ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"),
                 ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"),
                 ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"),
                 ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"),
                 ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
                 ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
                 ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
                 ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
                 ("Lakshadweep", "Lakshadweep"),
                 ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
                 ("Puducherry", "Puducherry"))


class Users(models.Model):
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=20)
    line1=models.CharField(max_length=1000,null=True,blank=True)
    country=models.CharField(choices=Country,max_length=100,null=True,blank=True)
    state = models.CharField(choices=state_choices,max_length=255,null=True,blank=True)
    city=models.CharField(max_length=500,null=True,blank=True)
    pincode=models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    user_type = models.CharField(choices=choices, max_length=300)
    username = models.CharField( max_length=300,null=True,blank=True)


class Workers(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=300)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    service = models.CharField(max_length=100)
    # gender = models.enums{'male','female','others'}
    # charges = models.CharField(max_length=100)
    # rating = models.IntegerField()


class Appointment(models.Model):
    worker_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    Appointment_date = models.CharField(max_length=100)
    completed = models.IntegerField(default=0)


class Blog(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    category=models.CharField(max_length=100,null=True, blank=True,choices=(( 'Mental Health','Mental Health'),('Heart Disease','Heart Disease') ,('Covid19','Covid19'),('Immunization','Immunization')))
    summary = models.TextField(max_length=100,null=True, blank=True)
    content = models.TextField(max_length=1000, null=True, blank=True)