from fixturapp.utils.importlib import import_module

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