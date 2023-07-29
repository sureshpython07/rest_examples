from django.db import models

# Create your models here. for serializer
class Post(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    email=models.EmailField(default='')

    def __str__(self):
        return self.title
# create your model for ModelSerializer
class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=50)
    wclass=models.CharField(max_length=20) 
    def __str__(self):
        return self.name