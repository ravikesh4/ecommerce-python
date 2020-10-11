from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "fullname", "name": "fullname", "placeholder": "Full Name"
            }))
    email = forms.EmailField(widget=forms.EmailInput(
            attrs={"class": "form-control", "id": "email", "name": "email", "placeholder": "Email"
            }))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "id": "content", "name": "content", "placeholder": "content"
            })
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            return forms.ValidationError("Email has to be gmail")
        return email

    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username",)
    email = forms.EmailField(label="Email",)
    password = forms.CharField(label="Your Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_username(self): 
        username = self.cleaned_data.get('username')
        # email = self.cleaned_data.get('email')

        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self): 
        email = self.cleaned_data.get('email')
        # email = self.cleaned_data.get('email')

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self): 
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password must match.")
        return data