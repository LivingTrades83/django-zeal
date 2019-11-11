from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/data/', views.get_data, name='api-data' ),
]