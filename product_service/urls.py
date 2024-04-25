from django.urls import path
# from django.conf.urls import url, include
from .views import ProductView, ServiceView

urlpatterns = [
    path('products/', ProductView.as_view(), name='productsss'),
    path('services/', ServiceView.as_view(), name='servicess'),
]
