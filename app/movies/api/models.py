from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    bio = models.TextField()
    dob = models.DateField()
    Gender = models.CharField(max_length=10)
    Dir_Movies = models.ManyToManyField('Movie',blank=True)
    
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    Act_Movies = models.ManyToManyField('Movie',blank=True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor,blank=True)
    Movie_Director = models.ForeignKey(Director, on_delete=models.CASCADE,blank=True)
    
    def __str__(self):
        return self.title