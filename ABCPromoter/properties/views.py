from django.shortcuts import render, redirect
from .models import Property, Customer
from .forms import RegistrationForm

def home(request):
    properties = Property.objects.all()
    return render(request, 'properties/home.html', {'properties': properties})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('receipt', pk=booking.pk)
    else:
        form = RegistrationForm()
    return render(request, 'properties/register.html', {'form': form})

def receipt(request, pk):
    booking = Customer.objects.get(pk=pk)
    return render(request, 'properties/receipt.html', {'booking': booking})

def view_booking(request):
    bookings = Customer.objects.all()
    return render(request, 'properties/view_booking.html', {'bookings': bookings})
