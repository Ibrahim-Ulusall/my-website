from django.db import models

# Create your models here.

class Contact(models.Model):
    firstName = models.CharField(max_length=50,null=True)
    lastName = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=15,null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True,editable=False)
    
    def __str__(self):
        return f'{self.firstName.capitalize()} {self.lastName.upper()}'
    