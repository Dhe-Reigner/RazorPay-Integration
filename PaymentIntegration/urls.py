from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='my_home'),
    path('success/', views.success,name='my_success'),
]