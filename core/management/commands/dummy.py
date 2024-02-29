from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from importlib import import_module


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("model", type=str, help="example : core.User, blog.Post")
        parser.add_argument("--count", type=int)

    def handle(self, *args, **options):
        pkg_name, model_name = options['model'].split(".")
        count = options["count"] or 1

        # get model:
        model = getattr(import_module(f"{pkg_name}.models"), model_name)

        # run mixer:
        mixer.cycle(count).blend(model)

        # print status
        self.stdout.write(self.style.SUCCESS('Successful :)'))
