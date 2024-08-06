from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
