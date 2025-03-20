from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

    password = forms.CharField(max_length=50,widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ("username","email","password")
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        model = self.Meta.model 
        if model.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("A user with the Username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        model = self.Meta.model 
        if model.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with the Email already exists.")
        return email 

    def clean_password(self,*args,**kwargs):
        password = self.cleaned_data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch !")
        return password 

    def save(self, commit=True,*args,**kwargs):
        user = self.instance 
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user 

class ChangePasswordForm(forms.Form):
    def __init__(self,*args,user,**kwargs):
        self.user = user
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

    current_password = forms.CharField(max_length=50,widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=50,widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=50,widget=forms.PasswordInput)

    def clean_current_password(self,*args,**kwargs):
        current_password = self.cleaned_data.get('current_password')
        if not self.user.check_password(current_password):
            raise forms.ValidationError("Incorrect Password !")
        return current_password 

    def clean_new_password(self,*args,**kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError("Password mismatch !")
        return new_password1
