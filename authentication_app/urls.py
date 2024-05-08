from django.urls import path
from . import views

app_name='auth_app'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login_form'),
    path('register/', views.Register.as_view(), name='register_form')
]
