from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput
from django.forms import ModelForm

from student.models import Profile


class SignupForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['phone_number']

    def signup(self, request, user):
        user.profile.phone_number = self.cleaned_data['phone_number']
        user.profile.save()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['full_name','email','phone','password1']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']


