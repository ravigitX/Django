from django.shortcuts import render
from .models import Booking

def home(request):
    return render(request, 'home.html')

def sample(request):
    return render(request, 'samp.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        booking_type = request.POST.get('booking_type')

        # Calculate amount based on booking type
        amount_map = {
            'Economy': 3000000,
            'Luxury': 5000000,
            'Deluxe': 7500000,
            'Single': 8000000,
            'Duplex': 10000000,
        }
        amount = amount_map.get(booking_type)

        # Save booking details
        booking = Booking(name=name, mobile_number=mobile_number, email=email,
                          booking_type=booking_type, amount=amount)
        booking.save()

        # Redirect to receipt page
        return render(request, 'receipt.html', {'booking': booking})

    return render(request, 'register.html')

def view_booking(request):
    bookings = Booking.objects.all()
    return render(request, 'view_booking.html', {'bookings': bookings})
