from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_manager(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_manager', True)
        extra_fields.setdefault('is_client', False)
        return self.create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)



class User(AbstractUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    is_manager = models.BooleanField('Manager', default=False)
    is_client = models.BooleanField('Client', default=True)

    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    account_status = models.CharField(max_length=20, default='active')
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    generic_name = models.CharField(max_length=100, blank=True, null=True)
    dosage_form = models.CharField(max_length=50, blank=True, null=True)
    strength = models.CharField(max_length=50, blank=True, null=True)
    storage_conditions = models.TextField(blank=True, null=True)
    expiry_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    prescription_id = models.IntegerField(blank=True, null=True)