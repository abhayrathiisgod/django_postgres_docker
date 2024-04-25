from rest_framework import serializers
from .models import ContactForm, ContactInfo, PageContent, BannerImage


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['Name', 'Email', 'Subject', 'Message']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['Email', 'Phone', 'Address', 'Latitude_Logitude', 'Facebook_link',
                  'Instagram_link', 'X_link', 'Youtube_link', 'Linkedin_link']


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['Page_Type', 'Page_Title', 'Page_Content', 'image']


class Banner_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['Banner', 'Title', 'Description', 'Image']
