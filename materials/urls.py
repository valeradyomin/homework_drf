from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView, SubscriptionCreateAPIView, SubscriptionListAPIView, \
    SubscriptionDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscription/create/<int:pk>/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
] + router.urls
