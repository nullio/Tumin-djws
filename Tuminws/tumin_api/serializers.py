from rest_framework import serializers
from .models import TumnSerServicio, TumnCueCuenta

class SerServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TumnSerServicio
        fields = '__all__'
        #('ser_id','ser_nombre')
        #'__all__'

class CueCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=TumnCueCuenta
        fields='__all__'