from django.test import TestCase
from fixturapp.management.commands import get_datasets, find_datasets, fill_database
from dummyapp.datasets import DummyData
from dummyapp.models import Dummy

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

    def test_fill_database_with_data_from_fixture(self):
        """Check if ``fill_database`` loaded DummyData to the database"""
        fill_database([DummyData])
        obj = Dummy.objects.get(name='Buster')
        self.assertEquals(obj.name, DummyData.buster.name)

    def test_raises_when_call_fill_database_with_empty_list(self):
        """Raises when calling ``fill_database`` passing no data"""
        self.assertRaises(ValueError, lambda: fill_database([]))
        self.assertRaises(TypeError, lambda: fill_database('None'))
        self.assertRaises(TypeError, lambda: fill_database(DummyData))