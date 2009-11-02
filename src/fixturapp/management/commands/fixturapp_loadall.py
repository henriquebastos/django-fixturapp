from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from fixture import DjangoFixture
from fixture.style import NamedDataStyle

from fixturapp.management.commands import find_datasets, fill_database


class Command(NoArgsCommand):
    help = "Load every dataset fixtures from INSTALLED_APPS into database"

    def handle_noargs(self, **options):
        # Discover datasets in apps
        fixtures = find_datasets(settings.INSTALLED_APPS)
        if not len(fixtures):
            raise CommandError('No datasets fixtures found.')

        fill_database(fixtures, int(options.get('verbosity', 1)))
