from django.urls import path, include
from rest_framework.routers import DefaultRouter

from measurement.views import SensorListCreateAPIView, MeasurementListAPIView, SensorRetrieveUpdateAPIView, \
    MeasurementCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementListAPIView.as_view(), name='measurement-list'),
    path('measurements/create/', MeasurementCreateAPIView.as_view(), name='measurement-create'),
]
