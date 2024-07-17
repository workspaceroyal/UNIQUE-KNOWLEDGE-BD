from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"ইউজার নেম"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"ই-মেইল"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"পাসওয়ার্ড"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"কনফার্ম পাসওয়ার্ড"}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"পুরা নাম"}))
    bio = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"বায়ো"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"ফোন"}))

    class Meta:
        model = Profile
        fields = ['full_name', 'image', 'bio', 'phone']