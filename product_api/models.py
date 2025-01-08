from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model
class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Add related_name to avoid conflict for groups field
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='product_api_users',  # Unique related_name for groups
        blank=True
    )

    # Add related_name to avoid conflict for user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='product_api_users_permissions',  # Unique related_name for user_permissions
        blank=True
    )

# Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

