from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        total_price = (check_out - check_in).days * room.room_price
        Booking.objects.create(user=request.user, room=room, check_in=check_in, check_out=check_out, total_price=total_price)
        return redirect('my_bookings')
    return render(request, 'book_room.html', {'room': room})

