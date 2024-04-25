from typing import Any
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
import os
from random import choice

from website.models import Banner_Images, ContactForm, ContactInfo, PageContent


class Command(BaseCommand):
    help = "Populate database with fake data for website appl"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # BANNER IMAGESS
        for _ in range(10):
            banner = fake.random_element(
                elements=[choice[0] for choice in Banner_Images.BANNER_TYPE])
            title = fake.text(max_nb_chars=50)
            description = fake.text(max_nb_chars=200)
            image = os.path.join('uploads', 'banners',
                                 fake.file_name(category='image'))
            Banner_Images.objects.create(
                Banner=banner, Title=title, Description=description, Image=image)

        # Contact Form
        for _ in range(20):
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            subject = fake.catch_phrase()
            message = fake.paragraph(nb_sentences=3)
            ContactForm.objects.create(
                Name=name, Email=email, Phone=phone, Subject=subject, Message=message)

        # ContactInfo
        for _ in range(1):
            email = fake.email()
            phone = fake.phone_number()
            address = fake.address()
            latitude_longitude = f'{fake.latitude()}, {fake.longitude()}'
            facebook_link = fake.url()
            instagram_link = fake.url()
            x_link = fake.url()
            youtube_link = fake.url()
            linkedin_link = fake.url()
            ContactInfo.objects.create(Email=email, Phone=phone, Address=address, Latitude_Logitude=latitude_longitude,
                                       Facebook_link=facebook_link, Instagram_link=instagram_link,
                                       X_link=x_link, Youtube_link=youtube_link, Linkedin_link=linkedin_link)

        # PageContent
        page_types = [choice[0] for choice in PageContent.Page_type]
        for _ in range(4):
            page_type = fake.random_element(elements=page_types)
            page_title = fake.sentence()
            page_content = fake.paragraphs(nb=3)
            image = os.path.join('uploads', 'pages',
                                 fake.file_name(category='image'))
            PageContent.objects.create(Page_Type=page_type, Page_Title=page_title, Page_Content=page_content,
                                       image=image)

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with fake data'))
