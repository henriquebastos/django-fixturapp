from django.test import TestCase
from django.core.management import load_command_class
from django.core.management.base import BaseCommand
from fixturapp.management.commands import get_datasets, find_datasets
from fixturapp.management.commands import fixturapp_loadall

dummyapp = 'fixturapp.tests.dummyapp'
emptyapp = 'fixturapp.tests.emptyapp'

def create_command():
    return load_command_class('fixturapp', 'fixturapp_loadall')

class FixturappLoadAllTests(TestCase):
    def test_environment(self):
        """Just make sure everything is set up correctly."""
        self.assert_(True)

    def test_get_datasets_for_dummyapp(self):
        """Sucessfully get datasets dummyapp"""
        from dummyapp.datasets import DummyData
        self.assertEquals(get_datasets(dummyapp), [DummyData])

    def test_raise_when_cant_get_datasets_for_emptyapp(self):
        """Raises ImportError when app does not have datasets package"""
        self.assertRaises(ImportError, lambda: get_datasets(emptyapp))

    def test_find_fixture_for_many_apps(self):
        """Sucessfully get datasets for a list of apps ignoring ImportErrors"""
        from dummyapp.datasets import DummyData
        self.assertEquals(find_datasets([dummyapp, emptyapp]), [DummyData])

    def test_find_fixture_for_installed_apps(self):
        """Sucessfully get datasets for INSTALLED_APPS defined in testsettings ignoring ImportErrors"""
        from django.conf import settings
        self.assertEquals(find_datasets(settings.INSTALLED_APPS), [DummyData])

    def test_load_command_loadall(self):
        """Sucessfully load the command fixturapp_loadall from django project"""
        self.failUnless(isinstance(create_command(), fixturapp_loadall.Command))

    def test_command_is_valid_django_command(self):
        """Asserts that fixturapp_loadall command is a valid Django command"""
        self.failUnless(isinstance(create_command(), BaseCommand))

#    def test_fixture_was_loaded_by_calling_command(self):
