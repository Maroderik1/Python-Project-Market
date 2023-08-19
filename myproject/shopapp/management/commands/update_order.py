from django.core.management import BaseCommand
from shopapp.models import Order, Product
from django.contrib.auth.models import User


class Command(BaseCommand):
    """
    Update order
    """
    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write('Not order found')
            return
        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(f'Successfully added product {order.products.all()} to order {order}')