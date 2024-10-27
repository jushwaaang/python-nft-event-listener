from django.core.management.base import BaseCommand
from transfer.tasks import listen_for_live_transfer_events


class Command(BaseCommand):
    help = 'Fetch and save Live BAYC transfer events from Ethereum blockchain'

    def handle(self, *args, **kwargs):
        listen_for_live_transfer_events()

