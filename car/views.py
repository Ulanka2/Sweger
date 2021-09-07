from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from car.models import Car, CarDocument
from car.serializers import CarSerializer, CarDocumentSerializer
from car.permissions import DiversePermission

class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('-id')
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, DiversePermission, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class CarDocumentView(viewsets.ModelViewSet):
    queryset = CarDocument.objects.all().order_by('-id')
    serializer_class = CarDocumentSerializer
    permission_classes = [IsAuthenticated, ]



