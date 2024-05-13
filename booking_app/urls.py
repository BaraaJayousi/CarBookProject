from django.urls import path
from . import views

app_name='booking_app'
urlpatterns = [ 
  path('', views.HomePage.as_view(), name="home_page"),
  path('cars/', views.CarsPage.as_view(), name="cars_page"),
  path('cars/<int:id>', views.CarDetailsPage.as_view(), name="car_details"),
  path('cars/book', views.CarBookPage.as_view(), name="car_book"),
  path('cars/book-car', views.CarBookPage.as_view(), name="car_book_confirm"),
  path('cars/my-bookings', views.MyBookings.as_view(), name="my_bookings")
]

