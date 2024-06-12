
from django.test import TestCase
from datetime import date
from ...Reservation.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item_as_string = str(item)
        self.assertEqual(item_as_string, "IceCream : 80")


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="BookingForTheJohnFamily", no_of_guests=4, booking_date=date.today())
        item_as_string = str(item)
        self.assertEqual(item_as_string, "BookingForTheJohnFamily : 4 guests")