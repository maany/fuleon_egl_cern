from django.core.management import BaseCommand
from fuleon_egl.api.fetch_data import fetch_data

class Command(BaseCommand):
    help = 'Fetch data from egl_server'

    def handle(self, *args, **options):
        fetch_data()
        self.stdout.write(self.style.SUCCESS("Completed"))
