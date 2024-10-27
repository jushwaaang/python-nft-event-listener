# transfer/views.py

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from transfer.models import TransferEvent
from transfer.serializers import TransferEventSerializer
from transfer.filters import get_transfer_events_filter


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TransferEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TransferEvent.objects.all()
    serializer_class = TransferEventSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        filter_criteria = get_transfer_events_filter(self.request)
        return self.queryset.filter(**filter_criteria)
