from typing import Any
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from random import choice

from vacancies.models import Jobs, Candidates


class Command(BaseCommand):
    help = "Populate database with fake command"

    def handle(self, *args, **kwargs):
        fake = Faker()

        ###############
        # jobs
        job_title = ['Full Stack Developer', 'Front End Developer',
                     'Backend Developer', 'UI/UX Designer']
        job_type = [
            'FULL_TIME', 'REMOTE', 'HYBRID', 'PARTIME'
        ]
        i = 0
        for _ in range(4):
            title = job_title[i]
            job_type = choice(job_type)
            about_role = fake.text()
            job_req = fake.text()
            open_date = fake.date_this_year()
            close_date = fake.date_between_dates(
                date_start=open_date, date_end=open_date.replace(year=open_date.year + 1))
            is_published = fake.boolean()
            Jobs.objects.create(
                Title=title,
                Job_Type=job_type,
                About_Role=about_role,
                Job_Requirement=job_req,
                Open_date=open_date,
                Close_date=close_date,
                is_published=is_published
            )
            i += 1

        ###############
        # candidates
        jobs_instances = Jobs.objects.all()

        for _ in range(50):
            name = fake.name()
            first_name, last_name = name.split(' ', 1)
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            phone = fake.phone_number()
            position = choice(jobs_instances)
            cv = fake.url()

            Candidates.objects.create(
                Name=name,
                Email=email,
                Phone=phone,
                Position=position,
                CV=cv
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with fake data for vacancies'))
