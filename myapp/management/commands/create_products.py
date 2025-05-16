from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    """Create products in the database."""
    
    def handle(self, *args, **options):
        self.stdout.write("Creating products...")
        
        products = [
            {"name": "Laptop", "price": 999.99, "discount": 10},
            {"name": "Smartphone", "price": 499.99, "discount": 5},
            {"name": "Smartwatch", "price": 199.99, "discount": 15},
            {"name": "Headphones", "price": 99.99, "discount": 20},
            {"name": "Charger", "price": 19.99, "discount": 0},
            {"name": "Mouse", "price": 29.99, "discount": 5},
        ]
        
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Product '{product.name}' created!"))
            else:
                self.stdout.write(self.style.WARNING(f"Product '{product.name}' already exists."))
