from django.db import models

# Create your models here.
class Myportfolio(models.Model):
    image = models.ImageField(upload_to='images/',blank='True')
    description = models.CharField(max_length=255,blank='True')

    def __str__(self):
        return self.description


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
