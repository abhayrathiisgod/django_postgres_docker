from django.urls import path
from .views import ContactFormView, ContactInfoView, PageContentView, Banner_ImagesView

urlpatterns = [
    path('contact-form/', ContactFormView.as_view()),
    path('contact-infos/', ContactInfoView.as_view()),
    path('page-contents/', PageContentView.as_view()),
    path('banner-images/', Banner_ImagesView.as_view()),
]
