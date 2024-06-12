
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import views
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html', {})
   

@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    ordering_fields=['name', 'no_of_guests', 'booking_date']
    search_fields=['booking_date', 'name']


@permission_classes([IsAuthenticated])
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@permission_classes([IsAuthenticated])
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
