DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/fixturapp.db'
# HACK: Don't forget to set fixturapp as the last app.
#       If it goes first, Django won't be able to import the test apps
INSTALLED_APPS = (
    'fixturapp.tests.dummyapp',
    'fixturapp.tests.emptyapp',
    'fixturapp',
    )
ROOT_URLCONF = ['fixturapp.urls']
