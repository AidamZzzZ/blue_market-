from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Formulario para crear usuario
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number")

# Formulario de edicion de usuarios
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number")
