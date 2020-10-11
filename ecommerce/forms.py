from django import forms


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