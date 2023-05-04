from django.db import models

class user(models.Model):
     username=models.CharField(max_length=50)
     password=models.CharField(default='ankush',max_length=50)
     first_name = models.CharField(max_length=200)
     second_name = models.CharField(max_length=200)
     email = models.EmailField(max_length=100)




