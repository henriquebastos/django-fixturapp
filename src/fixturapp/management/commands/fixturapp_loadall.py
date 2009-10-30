from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from fixturapp.management.commands import find_datasets, fill_database
from fixture import DjangoFixture
from fixture.style import NamedDataStyle

class Command(BaseCommand):
    help = "Load datasets fixtures from Django apps into database"

    def handle(self, **options):
        from django.conf import settings

        apps = settings.INSTALLED_APPS
        fixtures = find_datasets(apps) #Discover datasets in apps
        if not len(fixtures):
            raise CommandError('No fixture datasets found.')

        fill_database(fixtures)
