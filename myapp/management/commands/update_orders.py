from django.core.management.base import BaseCommand
from myapp.models import Product, Orders


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Orders.objects.first()
        if not order:
            self.stdout.write(self.style.ERROR('No orders found.'))
            return
        
        products = Product.objects.all()
        
        for product in products:
            order.products.add(product)
            
        order.save()