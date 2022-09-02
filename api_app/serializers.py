from rest_framework import serializers
from .models import CartItems, CricketTeamSheet

class CartItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default = 1)
    
    class Meta:
        model = CartItems
        fields = ('__all__')    
        

class CricketTeamListSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(max_length=255)
    lastName = serializers.CharField(max_length=255)
    cricketTeam = serializers.CharField(max_length=255)
    role = serializers.CharField(max_length=255)
    
    class Meta:
        model = CricketTeamSheet
        fields = ('__all__')    
    
        