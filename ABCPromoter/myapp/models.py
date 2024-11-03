from django.db import models 

class Booking(models.Model):
    FLAT_CHOICES = [
        ('Economy', 'Economy flat - 30 lakh rupees'),
        ('Luxury', 'Luxury flat - 50 lakh rupees'),
        ('Deluxe', 'Deluxe flat - 75 lakh rupees'),
        ('Single', 'Independent house - single house - 80 lakh rupees'),
        ('Duplex', 'Independent house - duplex house - 1 crore'),
    ]

    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    booking_type = models.CharField(max_length=10, choices=FLAT_CHOICES)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.booking_type}"
