from django.db import models

class cardidate(models.Model):
    cardidate_name = models.CharField(max_length=100)
    cardidate_image = models.ImageField(upload_to='profiles/')
    cardidate_party = models.CharField(max_length=100)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.cardidate_name
    
class voter(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    idname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
class codes(models.Model):
    code = models.CharField(max_length=7, unique=True) 

    def __str__(self):
        return self.code