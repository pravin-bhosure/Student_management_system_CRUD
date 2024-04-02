from django.db import models

# Create your models here.

class subject(models.Model):
    subject_name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.subject_name}'
    
class Student(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)
    Class = models.IntegerField()
    subject_name =models.ForeignKey(subject,on_delete=models.CASCADE,blank=True,null=True)
    
    
    
    def __str__(self):
        return f'{self.fname} {self.lname}'
    
    def __str__(self):
        return f'{self.subject}'
        