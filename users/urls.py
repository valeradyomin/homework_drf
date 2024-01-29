from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('payment_list/', PaymentListAPIView.as_view(), name='payment_list'),
] + router.urls
