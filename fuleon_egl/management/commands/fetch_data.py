from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Fetch data from egl_server'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("hello"))
