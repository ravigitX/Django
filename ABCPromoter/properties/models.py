from django.db import models

class Property(models.Model):
    PROPERTY_CHOICES = [
        ('Economy Flat', 'Economy Flat - 30 lakh rupees'),
        ('Luxury Flat', 'Luxury Flat - 50 lakh rupees'),
        ('Deluxe Flat', 'Deluxe Flat - 75 lakh rupees'),
        ('Single House', 'Single House - 80 lakh rupees'),
        ('Duplex House', 'Duplex House - 1 crore rupees')
    ]
    
    property_type = models.CharField(max_length=50, choices=PROPERTY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.property_type} - {self.price}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.property.property_type}"
