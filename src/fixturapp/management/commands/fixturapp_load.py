from django.core.management.base import BaseCommand
from fixture import DjangoFixture
from fixture.style import NamedDataStyle

from fixturapp.management.commands import get_datasets, fill_database


class Command(BaseCommand):
    help = "Load datasets fixtures from Django apps into database"
    args = "[app1 app2 ...]"

    def handle(self, *apps, **options):
        fixtures = []

        for app in apps:
            datasets = get_datasets(app)
            if not len(datasets):
                raise LookupError('No dataset found for %s.' % app)
            fixtures.extend(datasets)

        fill_database(fixtures, int(options.get('verbosity', 1)))
