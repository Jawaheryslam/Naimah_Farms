from rest_framework import serializers
from .models import Goat


class GoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goat
        fields = '__all__'
