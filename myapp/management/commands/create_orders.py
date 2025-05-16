from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from myapp.models import Orders



class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Creating orders...")
        users = User.objects.get(username="kamal")
        order = Orders.objects.get_or_create(
            delivery_address = "123 Main St, Springfield, USA",
            promocode = "SUMMER2023",
            user = users,
        )
        self.stdout.write(self.style.SUCCESS(f"Created order: {order}"))