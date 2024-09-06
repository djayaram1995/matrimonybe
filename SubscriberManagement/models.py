from django.db import models
import uuid

# Create your models here.

class Subscriber(models.Model):
    class Genders(models.TextChoices):
        MALE='MALE'
        FEMALE='FEMALE'
    id= models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable= False)
    alpha_num_id = models.CharField(unique=True,null=False, max_length=10)
    caste= models.CharField(null=False, max_length=100)
    sub_caste= models.CharField(max_length=100)
    name= models.CharField(null=False, max_length=100)
    father_name= models.CharField(max_length=100)
    mother_name= models.CharField(max_length=100)
    siblings_count=models.IntegerField(default=0)
    date_of_birth=models.DateField(null=False)
    time_of_birth=models.TimeField(null=False)
    gender=models.CharField(null=False, choices=Genders.choices)
    height= models.IntegerField(null=False)
    weight= models.IntegerField(null=False)
    education= models.CharField(null=False, max_length=500)
    hobbies= models.CharField(max_length=100)
    profession= models.CharField(null=False, max_length=100)
    salary=models.IntegerField(null=False)
    special_request=models.TextField(max_length=2000)
    description=models.TextField(max_length=2000)
    address=models.TextField(null=False, max_length=2000)
    city=models.CharField(null=False, max_length=50)
    primary_mobile_no= models.CharField(unique=True, null=False, max_length=20, default="")
    primary_email_id= models.CharField(unique=True, null=False, max_length=100, default="")
    secondary_mobile_no= models.CharField(max_length=20, default="")
    secondary_email_id= models.CharField(max_length=100, default="")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)