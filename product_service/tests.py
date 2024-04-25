from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Product, SERVICE


class ProductAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.prdouct1 = Product.objects.create(
            NAME='PRODUCT 1',
            SLUG='PRODUCT-1',
            SHORT_DESCRIPTION='short description for product 1'
        )

        self.product2 = Product.objects.create(
            NAME='PRODUCT 2',
            SLUG='PRODUCT-2',
            SHORT_DESCRIPTION='short decritption for product 2'
        )

    def test_get_product_list(self):
        url = reverse('api/v1/products-services/products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
