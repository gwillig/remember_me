from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    Interests = models.TextField(blank=True, null=True)
    hobbies = models.CharField(max_length=200,blank=True, null=True)
    jungs_type = models.CharField(max_length=20,blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    first_meeting = models.TextField(blank=True, null=True)
    employer = models.CharField(max_length=200,blank=True, null=True)
    relationship = models.CharField(max_length=200,blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    misc_1= models.CharField(max_length=200,blank=True, null=True)
    misc_2 = models.CharField(max_length=200,blank=True, null=True)
    misc_3 = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return (f"{self.last_name} , {self.first_name}")