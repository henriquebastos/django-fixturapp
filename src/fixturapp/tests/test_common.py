from django.test import TestCase
from fixturapp.management.commands import get_datasets, find_datasets
from dummyapp.datasets import DummyData

dummyapp = 'fixturapp.tests.dummyapp'
emptyapp = 'fixturapp.tests.emptyapp'

class FixturappCommon(TestCase):
    def test_environment(self):
        """Just make sure everything is set up correctly."""
        self.assert_(True)

    def test_get_datasets_for_dummyapp(self):
        """Sucessfully get datasets dummyapp"""
        self.assertEquals(get_datasets(dummyapp), [DummyData])

    def test_raise_when_cant_get_datasets_for_emptyapp(self):
        """Raises ImportError when app does not have datasets package"""
        self.assertRaises(ImportError, lambda: get_datasets(emptyapp))

    def test_find_fixture_for_many_apps(self):
        """Sucessfully get datasets for a list of apps ignoring ImportErrors"""
        self.assertEquals(find_datasets([dummyapp, emptyapp]), [DummyData])

    def test_find_fixture_for_installed_apps(self):
        """Sucessfully get datasets for INSTALLED_APPS defined in testsettings ignoring ImportErrors"""
        from django.conf import settings
        self.assertEquals(find_datasets(settings.INSTALLED_APPS), [DummyData])
