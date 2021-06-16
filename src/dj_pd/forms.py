from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=220, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=220, label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        data = self.cleaned_data

        username = data.get('username')
        password = data.get('password')

        # lógica opcional para personalizar validación

        return data