from django.db import models


# User model to store user information
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)  # Ensure to hash passwords using Django's authentication system

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


# Location model to store unique locations
class Location(models.Model):
    address = models.CharField(max_length=255, unique=True)  # Unique address

    def __str__(self):
        return self.address


# Alwakf model to store information about endowments
class Alwakf(models.Model):
    name = models.CharField(max_length=255)  # Name of the endowment
    description = models.TextField()         # Description of the purpose or activities
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name="wakfs")  # Foreign key to Location
    established_date = models.DateField()    # Date of establishment
    contact_info = models.CharField(max_length=255, blank=True, null=True)  # Contact information
    funds_available = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)  # Available funds
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wakfs")  # Foreign key to User

    def __str__(self):
        return self.name


# BusinessType model for standardized business categories
class BusinessType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique business type name
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name


# Enterprise model to store business information for Zakat calculation
class Enterprise(models.Model):
    name = models.CharField(max_length=255)  # Business name
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enterprises")  # Foreign key to User
    email = models.EmailField(blank=True, null=True)  # Optional email contact
    business_type = models.ForeignKey(BusinessType, on_delete=models.SET_NULL, null=True, related_name="enterprises")  # Foreign key to BusinessType
    annual_revenue = models.DecimalField(max_digits=15, decimal_places=2)  # Annual revenue for Zakat calculation
    zakat_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)  # Calculated Zakat amount
    registered_date = models.DateField(auto_now_add=True)  # Date the business was registered in the system

    def __str__(self):
        return self.name
