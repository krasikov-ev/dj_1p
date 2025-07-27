# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView



from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer




class SensorView(ListCreateAPIView):
    """
    Обработчик для создания датчика и получения списка всех датчиков.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    """
    Обработчик для получения информации о датчике и его обновления.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(CreateAPIView):
    """
    Обработчик для добавления нового измерения температуры.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


