from django import forms
from homepage.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password', 'email','first_name') #,'last_name')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		# exclude = ('user',)
		fields = ()

class LoginForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	username = forms.CharField(label='Username', required=True)
	password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput())