from typing import Any
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker

from product_service.models import Product, SERVICES


class Command(BaseCommand):
    help = "Populate database with fake command"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):
            name = fake.name()
            slug = slugify(name)
            short_description = fake.text()
            icon_url = fake.image_url(width=None, height=None)
            # icon_url += '.png'
            Product.objects.create(
                NAME=name,
                SLUG=slug,
                SHORT_DESCRIPTION=short_description,
                ICON=icon_url,
            )
        for _ in range(50):
            name = fake.name()
            slug = slugify(name)
            short_description = fake.text()
            image_url = fake.image_url(width=None, height=None)
            icon_url = fake.image_url(width=None, height=None)
            SERVICES.objects.create(
                NAME=name,
                SLUG=slug,
                SHORT_DESCRIPTION=short_description,
                ICON=icon_url,
                IMAGE=image_url,
            )
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with fake data for product and service'))
