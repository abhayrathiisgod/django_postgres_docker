from django.core.management.base import BaseCommand
from product_service.models import Product


class Command(BaseCommand):
    help = "Bulk delete all items created by you"

    def handle(self, *args, **kwargs):

        items_to_delete = Product.objects.all()

        num_deleted, _ = items_to_delete.delete()

        self.stdout.write(self.style.SUCCESS(
            f'Successfully deleted {num_deleted} items created by you'))
