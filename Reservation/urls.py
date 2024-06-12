
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

booking_router = DefaultRouter(trailing_slash=False)
booking_router.register('booking', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', include(booking_router.urls)),
    path('in-app-token-endpoint', obtain_auth_token),
    
]

