# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,  DeviceViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'devices', DeviceViewSet, basename='device')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


#toke login curl : curl -X POST http://127.0.0.1:8000/api/token/ -d "username=spider&password=vinayak"
