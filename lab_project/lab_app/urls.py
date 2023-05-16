from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('guidelines', views.guidelines, name='guidelines'),
    path('book', views.book, name='book'),
    path('bookings', views.bookings, name='bookings'),
    path('register', views.register, name='register'),
    path('', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login')
]
