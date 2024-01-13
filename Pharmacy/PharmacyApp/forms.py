# PharmacyApp/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Supplier, Product
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    #address = forms.CharField(widget=forms.Textarea, required=True)
    #role = forms.CharField(max_length=20, required=True)
    #date_of_birth = forms.DateField(required=True)
    gender = forms.CharField(max_length=10, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'full_name',
                  'phone_number', 'gender')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        #user.address = self.cleaned_data['address']
        #user.role = self.cleaned_data['role']
        #user.date_of_birth = self.cleaned_data['date_of_birth']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()

        return user


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'contact_person', 'email', 'phone_number']

    labels = {
        'supplier_name': 'Supplier Name',
        'contact_person': 'Contact Person',
        'email': 'Email',
        'phone_number': 'Phone Number',
    }

    widgets = {
        'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
    }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'quantity_in_stock',
                  'manufacturer', 'generic_name', 'dosage_form', 'strength',
                  'storage_conditions', 'expiry_date', 'supplier']

    help_texts = {
        'expiry_date': 'Enter the expiry date of the product.',
    }


class ManagerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'full_name', 'phone_number', 'address', 'date_of_birth', 'gender']
