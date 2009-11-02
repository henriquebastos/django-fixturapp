from django.utils.importlib import import_module
from fixture import DjangoFixture
from fixture.style import NamedDataStyle


def get_datasets(app, package='.datasets', sufix='Data'):
    fixtures = []

    module = import_module(package, app)
    # add classes ending with 'Data' to the fixtures list
    for i in dir(module):
        if i.endswith(sufix):
            fixtures.append(getattr(module, i))
    return fixtures


def find_datasets(apps):
    fixtures = []
    try:
        for app in apps:
            fixtures.extend(get_datasets(app))
    except ImportError:
        pass
    return fixtures


def fill_database(fixtures, verbosity=1):
    """Given a list of fixture Data, fill all the data into database"""
    if not isinstance(fixtures, list):
        raise TypeError("Argument fixtures should be of type list.")
    if not len(fixtures):
        raise ValueError("Argument fixtures is empyt.")

    def echo(msg):
        if verbosity:
            print msg

    echo("Datasets: %s" % fixtures.sort())
    loader = DjangoFixture(style=NamedDataStyle())
    data = loader.data(*fixtures)
    echo("Installing datasets...")
    data.setup()
    echo("Done.")
