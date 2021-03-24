from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Client, Credit

# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # ['url', 'username', 'email', 'is_staff']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'total_debt', 'punctuation']


class CreditSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False, read_only=True)
    ia_evaluation = serializers.IntegerField(source='get_ia_evaluation')

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('client')
        return queryset

    class Meta:
        model = Credit
        fields = ['id', 'amount', 'state', 'payment_state', 'client', 'ia_evaluation']
