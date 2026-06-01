from django import forms
from django.contrib.auth.models import User
from .models import Task


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
    )


class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Your full name'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
    )

    class Meta:
        model = User
        fields = ['email']

    field_order = ['name', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'due_date']


class ProfileForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Your full name'}),
    )
    current_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
    )
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
    )
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        current = cleaned_data.get('current_password')
        new = cleaned_data.get('new_password')
        confirm = cleaned_data.get('confirm_password')

        any_filled = any([current, new, confirm])
        if any_filled:
            if not current:
                self.add_error('current_password', 'Enter your current password.')
            if not new:
                self.add_error('new_password', 'Enter a new password.')
            if not confirm:
                self.add_error('confirm_password', 'Confirm your new password.')
            if current and self.user and not self.user.check_password(current):
                self.add_error('current_password', 'Current password is incorrect.')
            if new and confirm and new != confirm:
                self.add_error('confirm_password', 'New passwords do not match.')

        return cleaned_data
