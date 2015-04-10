from django.forms import ModelForm, Form
from account.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'phone', 'gender', 'school', 'age']