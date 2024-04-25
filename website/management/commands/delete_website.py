from django.core.management.base import BaseCommand
from website.models import Banner_Images, ContactForm, ContactInfo, PageContent


class Command(BaseCommand):
    help = "Bulk delete all items created by you"

    def handle(self, *args, **kwargs):
        # Delete Banner_Images
        banner_images_to_delete = Banner_Images.objects.all()
        num_banner_images_deleted, _ = banner_images_to_delete.delete()

        # Delete ContactForm
        contact_forms_to_delete = ContactForm.objects.all()
        num_contact_forms_deleted, _ = contact_forms_to_delete.delete()

        # Delete ContactInfo
        contact_info_to_delete = ContactInfo.objects.all()
        num_contact_info_deleted, _ = contact_info_to_delete.delete()

        # Delete PageContent
        page_content_to_delete = PageContent.objects.all()
        num_page_content_deleted, _ = page_content_to_delete.delete()

        self.stdout.write(self.style.SUCCESS(
            f'Successfully deleted {num_banner_images_deleted} Banner_Images, '
            f'{num_contact_forms_deleted} ContactForms, '
            f'{num_contact_info_deleted} ContactInfos, and '
            f'{num_page_content_deleted} PageContents created by you'))
