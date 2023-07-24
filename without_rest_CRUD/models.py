from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eadd = models.CharField(max_length=255)

    def __str__(self):
        return self.ename
    class Meta:
        db_table='employee'
