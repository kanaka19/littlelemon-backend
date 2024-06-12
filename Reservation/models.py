
from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField(db_index=True)
    booking_date = models.DateField(db_index=True)

    def __str__(self) -> str:
        return f'{self.name} : {str(self.no_of_guests)} guests'
    
    