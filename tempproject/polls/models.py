from django.db import models
class Signin(models.Model):
    name=models.CharField(max_length=200,null="True")
    email= models.EmailField(max_length=25,null='True')
    password = models.CharField(max_length=200)


class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Testlogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)






# Create your models here
