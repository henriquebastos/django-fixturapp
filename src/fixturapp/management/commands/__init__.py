from django.utils.importlib import import_module
from fixture import DjangoFixture
from fixture.style import NamedDataStyle


def get_datasets(app, package='.datasets', sufix='Data'):
    """
    Get list of dataset classes ending with ``sufix`` from ``package``
    submodule on ``app``.

    It's expected to raise any error out loud.
    """
    fixtures = []

    module = import_module(package, app)
    # add classes ending with 'Data' to the fixtures list
    for i in dir(module):
        if i.endswith(sufix):
            fixtures.append(getattr(module, i))
    return fixtures


def find_datasets(apps):
    """
    Return a list of DataSet classes found on the received list of ``apps``.

    Since it's a search, ImportErrors are ignored.
    """
    fixtures = []
    for app in apps:
        try:
            fixtures.extend(get_datasets(app))
        except ImportError:
            pass
    return fixtures


def fill_database(fixtures, verbosity=1):
    """
    Fill all datasets listed in ``fixtures`` into database.
    """
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
