from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileForm(SignUpForm):
    class Meta:
        pass
        model = Profile
        fields = ('sport', 'location', 'birth_date')
