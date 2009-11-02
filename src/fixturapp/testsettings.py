DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/fixturapp.db'
INSTALLED_APPS = (
    'fixturapp',
    'fixturapp.tests.dummyapp',
    'fixturapp.tests.emptyapp',
    'fixturapp.tests.incompleteapp',
    )
ROOT_URLCONF = ['fixturapp.urls']
