from rest_framework import serializers
from .models import SourMilkDrinks

class SourMilkDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourMilkDrinks
        fields = ['id', 'name', 'description']