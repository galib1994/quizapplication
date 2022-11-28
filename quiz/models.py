from django.db import models

# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=40,help_text="name",null=True)
  gender=models.CharField(max_length=40,help_text="gender",null=True)
  discription = models.CharField(max_length=500,null=True)
  query_image = models.ImageField(upload_to='image/',null=True)
  timestamp = models.DateTimeField(auto_now=True)
  

  
  