from django.db import models


class TransferEvent(models.Model):
    token_id = models.PositiveIntegerField()
    to_address = models.CharField(max_length=42)
    from_address = models.CharField(max_length=42)
    contract_address = models.CharField(max_length=42)
    transaction_hash = models.CharField(max_length=66, unique=True)
    block_number = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Transfer Event"
        verbose_name_plural = "Transfer Events"
        ordering = ['-block_number']
