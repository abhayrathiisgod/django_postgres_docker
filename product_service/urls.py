from django.urls import path
# from django.conf.urls import url, include
from .views import ProductView, ServiceView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('services/', ServiceView.as_view()),
]
