from django.urls import path
from paymentSystemApp import views

app_name = 'paymentSystemApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout-session/', views.checkout_session, name='checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]


