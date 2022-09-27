from fixture import DjangoFixture
from fixture.style import NamedDataStyle


def get_datasets(app, package='.datasets', sufix='Data'):
    """
    Get list of dataset classes ending with ``sufix`` from ``package``
    submodule on ``app``.

    It's expected to raise any error out loud.
    """
    module = __import__(app + package, fromlist=[''])
    return [getattr(module, i) for i in dir(module) if i.endswith(sufix)]


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

    names = [c.__name__ for c in fixtures]

    echo("Datasets:\n\t%s" % "\n\t".join(names))
    loader = DjangoFixture(style=NamedDataStyle())
    data = loader.data(*fixtures)
    echo("Installing datasets...")
    data.setup()
    echo("Done.")
