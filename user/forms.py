from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User

class SignUp_form(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1','password2')