from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Address

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    profile_picture = forms.ImageField(required=False)
    line1 = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    pincode = forms.CharField(max_length=20, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'profile_picture', 'line1', 'city', 'state', 'pincode')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        address = Address.objects.create(
            line1=self.cleaned_data['line1'],
            city=self.cleaned_data['city'],
            state=self.cleaned_data['state'],
            pincode=self.cleaned_data['pincode']
        )
        user.address = address
        if self.cleaned_data['profile_picture']:
            user.profile_picture = self.cleaned_data['profile_picture']
        if commit:
            user.save()
        return user

