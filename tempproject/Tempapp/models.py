from django.db import models

# Create your models here.
class Departmentss(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Employeess(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    department=models.ForeignKey(Departmentss,on_delete=models.CASCADE)
