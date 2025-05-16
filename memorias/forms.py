from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate

class SignUpForm(forms.ModelForm):
    pin = forms.CharField(widget=forms.PasswordInput, label="PIN")

    class Meta:
        model = CustomUser
        fields = ['name', 'age', 'phone_number', 'pin']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['pin'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=9, label="Telefone")
    pin = forms.CharField(widget=forms.PasswordInput, label="PIN")

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        pin = self.cleaned_data.get('pin')
        user = authenticate(phone_number=phone_number, password=pin)
        if not user:
            raise forms.ValidationError("Número de telefone ou PIN incorretos.")
        self.user = user
        return self.cleaned_data