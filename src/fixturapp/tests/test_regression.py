from django.test import TestCase

from fixturapp.management.commands import find_datasets
from fixturapp.tests.dummyapp.datasets import DummyData


class TestRegression(TestCase):

    def test_find_fixture_for_every_listed_app(self):
        """
        Should find fixture for a second app, even when the first don't.
        """
        apps = ['fixturapp.tests.emptyapp',      # no dataset package
                'fixturapp.tests.incompletapp',  # has package, no Data
                'fixturapp.tests.dummyapp']      # DummyData
        self.assertEquals(find_datasets(apps), [DummyData])
