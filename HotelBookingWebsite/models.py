from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_no = models.IntegerField(unique=True)
    room_type = models.CharField(max_length=100)
    room_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_no} - {self.room_type}"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)


    def __str__(self):
        return f"Booking for {self.guest_name} ({self.room})"
    
