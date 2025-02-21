from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import EmployeeViewSet, ClientViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
