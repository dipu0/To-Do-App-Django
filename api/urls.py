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

#login
# CMD: curl -X POST http://127.0.0.1:8000/api/token/ -d "username=dipu&password=dipu"
#windows poweshell: Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api/token/ -Body "username=dipu&password=dipu"

#get task

#curl -i -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NDcwMDU4LCJpYXQiOjE3MDg0NjgyNTgsImp0aSI6IjVjYzBmZDRkMmM0MzQxYmViZmJlOTQ3NTc2NWU5ZWFhIiwidXNlcl9pZCI6MX0.AfhSt5aKNrU_1WLhqUyg5voNzoITAHB-koH5bnTIHBs" http://127.0.0.1:8000/api/tasks/