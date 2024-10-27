from django.core.management.base import BaseCommand
from transfer.tasks import fetch_and_save_transfer_byc_events


class Command(BaseCommand):
    help = 'Fetch and save BAYC transfer events from Ethereum blockchain'

    def handle(self, *args, **kwargs):
        fetch_and_save_transfer_byc_events()
        self.stdout.write(self.style.SUCCESS(
            'Successfully fetched and saved BAYC transfer events.'))
