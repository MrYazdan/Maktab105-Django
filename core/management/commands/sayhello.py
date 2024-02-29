from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("name", type=str)

    def handle(self, *args, **options):
        print(f"Hi, {options['name']}")


