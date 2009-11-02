from django.test import TestCase
from django.core.management import load_command_class, call_command
from django.core.management.base import BaseCommand

from fixturapp.management.commands import fixturapp_load
from fixturapp.tests.dummyapp.models import Dummy
from fixturapp.tests.dummyapp.datasets import DummyData


def create_command():
    return load_command_class('fixturapp', 'fixturapp_load')


def call_load(*args):
    return call_command('fixturapp_load', *args, verbosity=0)


class TestLoad(TestCase):

    def test_load_command_load(self):
        """Sucessfully load the command fixturapp_load from django project"""
        self.failUnless(isinstance(create_command(), fixturapp_load.Command))

    def test_command_is_valid_django_command(self):
        """Asserts that fixturapp_loadall command is a valid Django command"""
        self.failUnless(isinstance(create_command(), BaseCommand))

    def test_fixture_was_loaded_by_calling_command_for_one_app(self):
        """
        Check fixturapp_load command has loaded Dummy fixtures into database
        """
        call_load('fixturapp.tests.dummyapp')
        obj = Dummy.objects.get(name='Buster')
        self.assertEquals(obj.name, DummyData.buster.name)

    def test_raises_when_cant_find_datasets_package_for_app(self):
        """Raises when loading from specific app without datasets package"""
        self.assertRaises(ImportError,
                          lambda: call_load('fixturapp.tests.emptyapp'))

    def test_raises_when_app_have_empty_datasets_package(self):
        """
        Raises when loading from a specific app with an empty datasets package
        """
        self.assertRaises(LookupError,
                          lambda: call_load('fixturapp.tests.incompleteapp'))

    def test_raises_when_some_app_does_not_have_data(self):
        """
        ``fixturapp_load app1 app2`` should succeed only if all apps have data
        """
        self.assertRaises(LookupError,
                          lambda: call_load('fixturapp.tests.dummyapp',
                                            'fixturapp.tests.incompleteapp'))
        self.assertRaises(ImportError,
                          lambda: call_load('fixturapp.tests.dummyapp',
                                            'fixturapp.tests.emptyapp'))

    def test_fixture_was_loaded_by_calling_fixturapp_load(self):
        """Check that fixturapp_load loaded DummyData to the database"""
        call_load('fixturapp.tests.dummyapp')
        obj = Dummy.objects.get(name='Buster')
        self.assertEquals(obj.name, DummyData.buster.name)
