from rest_framework import serializers
from .models import PreciosBtc

class PreciosBtcSerializer(serializers.ModelSerializer):
    class Meta:
        model=PreciosBtc
        fields=['id','fecha','precioMax','precioMin']
        
