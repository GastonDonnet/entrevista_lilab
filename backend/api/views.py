from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import response, viewsets, views
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .serializers import ClientSerializer, CreditSerializer, UserSerializer
from .models import Client, Credit


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
        'amount': ['gte', 'lte']
    }

    def get_queryset(self):
        qs = super().get_queryset()
        qs = self.get_serializer_class().setup_eager_loading(qs)
        return qs
