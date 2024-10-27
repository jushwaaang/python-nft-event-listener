from rest_framework import serializers
from transfer.models import TransferEvent


class TransferEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferEvent
        fields = [
            'token_id',
            'from_address',
            'to_address',
            'transaction_hash',
            'block_number'
        ]
