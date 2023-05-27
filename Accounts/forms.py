from django.forms import ModelForm
from api.models import AppUser


class UserForm(ModelForm):
    class Meta:
        model = AppUser
        fields =('username','age','user_type','genre','gouvernorat','city','email','password')

            

