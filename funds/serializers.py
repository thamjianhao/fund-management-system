from rest_framework import serializers
from .models import Fund

# Serializer class to convert Fund model instances to JSON and vice versa
class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = [
            'fund_id',
            'fund_name',
            'fund_manager_name',
            'fund_description',
            'fund_nav',
            'date_of_creation',
            'fund_performance'
        ]
