from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import department,role,employe

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	
	
	class Meta:
		model = User
		fields = ('id','username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)
	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
	    self.fields['username'].label = ''
	    
	    self.fields['password1'].widget.attrs['class'] = 'form-control'
	    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
	    self.fields['password1'].label = ''
	    
	    self.fields['password2'].widget.attrs['class'] = 'form-control'
	    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
	    self.fields['password2'].label = ''



class d_form(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Department Name'}))
	location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}))
	class Meta:
		model = department
		fields = '__all__'


class r_form(forms.ModelForm):
	r_name = forms.CharField(widget=forms.TextInput(attrs={'form':'form-control','placeholder':'Role Name'}))
	class Meta:
		model = role
		fields = '__all__'


class e_form(forms.ModelForm):
	fname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your First Name'}))
	lname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Last Name'}))
	salary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'}))
	bonus = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Bonus'}))
	phone = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Phone Number'}))
	hired_date = forms.DateField(label='DATE')
	class Meta:
		model = employe
		fields = '__all__'

	