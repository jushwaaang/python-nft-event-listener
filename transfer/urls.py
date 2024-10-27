from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transfer.views import TransferEventViewSet

router = DefaultRouter()
router.register(r'transfers', TransferEventViewSet, basename='transfer-event')

urlpatterns = [
    path('', include(router.urls)),
]
