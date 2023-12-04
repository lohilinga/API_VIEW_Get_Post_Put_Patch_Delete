from rest_framework import serializers
from app.models import *
class productModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'
