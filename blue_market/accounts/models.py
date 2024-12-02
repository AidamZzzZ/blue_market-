from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from products.models import Product

# Creando modelo de usuario
class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.username
