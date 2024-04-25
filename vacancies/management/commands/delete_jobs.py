from django.core.management.base import BaseCommand
from vacancies.models import Jobs, Candidates


class Command(BaseCommand):
    help = "Bulk delete all items created by you"

    def handle(self, *args, **kwargs):

        Jobs_to_delete = Jobs.objects.all()
        # Candidates_to_delete = Candidates.objects.all()

        num_jobs_deleted, _ = Jobs_to_delete.delete()
        # num_candidates_deleted, _ = Candidates_to_delete.delete()

        self.stdout.write(self.style.SUCCESS(
            f'Successfully deleted {num_jobs_deleted} jobs created by you'))
