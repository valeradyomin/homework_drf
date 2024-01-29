from django.shortcuts import render
from rest_framework import viewsets, generics

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
