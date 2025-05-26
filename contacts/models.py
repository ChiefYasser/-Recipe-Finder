from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.name
