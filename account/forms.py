from django.forms import ModelForm
from account.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'age', 'email', 'phone', 'school']
