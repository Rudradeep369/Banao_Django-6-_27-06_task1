from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import ValidationError

class Address(models.Model):
    line1 = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    city = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    state = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    pincode = models.CharField(max_length=20, validators=[MinLengthValidator(5), MaxLengthValidator(20)])

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.state} - {self.pincode}"

    def clean(self):
        if not self.line1 or not self.city or not self.state:
            raise ValidationError("Line1, City, and State are required fields.")

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)

    # Define unique related_name for group and user_permissions
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    @property
    def full_address(self):
        if self.address:
            return f"{self.address.line1}, {self.address.city}, {self.address.state} - {self.address.pincode}"
        return ""

    def __str__(self):
        return self.username
