from django.core.management.base import BaseCommand, CommandError
from students.models import Group


class Command(BaseCommand):
    help = 'Generate random students'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for _ in range(number):
            Group.generate_group()
