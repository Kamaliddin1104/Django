from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    """Create products in the database."""
    
    def handle(self, *args, **options):
        self.stdout.write("Creating products...")
        
        products = [
            {"product_name": "Laptop", "price": 999.99, "discount": 10},
            {"product_name": "Smartphone", "price": 499.99, "discount": 5},
            {"product_name": "Smartwatch", "price": 199.99, "discount": 15},
            {"product_name": "Headphones", "price": 99.99, "discount": 20},
            {"product_name": "Charger", "price": 19.99, "discount": 0},
            {"product_name": "Mouse", "price": 29.99, "discount": 5},
        ]
        
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(f"Product '{product.name}' created!")
            else:
                self.stdout.write(f"Product '{product.name}' already exists.")
        
        self.stdout.write(self.style.SUCCESS("Products created successfully!"))
