from distutils.command.register import register
from . import views
from django.urls import path, include

urlpatterns = [
    path('register/', views.RegisterView(), name="register"),
    path('login/', views.LoginAPIView(), name="login"),
    path('confirm/', views.SMSCodeSerializer(), name="logout"),

]