from rest_framework import viewsets
from . import models
from . import serializers

class SerServicioViewset(viewsets.ModelViewSet):
    queryset = models.TumnSerServicio.objects.all()
    serializer_class = serializers.SerServicioSerializer

class CueCuentaViewset(viewsets.ModelViewSet):
    queryset = models.TumnCueCuenta.objects.all()
    serializer_class = serializers.CueCuentaSerializer