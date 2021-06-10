from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Employee
from django.utils.translation import gettext ,gettext_lazy as _

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('eid', 'ename','econtact','epetition','eplastic')
        widgets = {
            'eid':forms.TextInput(attrs={'class':'form-control'}), 
            'ename':forms.TextInput(attrs={'class': 'form-control'}),
            'econtact':forms.TextInput(attrs={'class': 'form-control'}), 
            'epetition':forms.TextInput(attrs={'class': 'form-control'}), 
            'eplastic':forms.TextInput(attrs={'class': 'form-control'}), 
        }
        
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Parol', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'parolni kiriting...'}))
    password2 = forms.CharField(label='Parolni takrorlang', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'parolni qayta kiriting...'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username':'Login' ,'first_name':'Ism', 'last_name':'Familya', 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'loginni kiriting va eslab qoling!'}),                                 
                    'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'ismingizni kiriting...'}),    
                    'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'familyangizni kiriting...'}),    
                    'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'"epochta@email.uz"  ko\'rinishida kiriting...'})    
                    }

class LoginForm(AuthenticationForm):
    username = UsernameField(label=("Login"), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'loginni kiriting...', 'autofocus':True}))
    password = forms.CharField(label=("Parol"),strip=False, widget=forms.PasswordInput(attrs={'autofocus':'current-password','class':'form-control', 'placeholder':'parolni kiriting...'}))
    class Meta:
        model = login
        fields = "__all__"
        
class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']
        labels = {'first_name':'Ism', 'last_name':'Familya', 'email':'Email'}
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control'}),    
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),    
                    'email':forms.EmailInput(attrs={'class':'form-control'})    
                    }


class SubscribeForm(forms.Form):
    emial = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'email',
            'placeholder':'Emailni kiriting',
            'id':'emailtext',
            'required':'required',
            'name':'subscribe'
        })
    )