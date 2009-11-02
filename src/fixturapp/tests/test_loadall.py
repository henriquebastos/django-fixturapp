from django.test import TestCase
from django.core.management import load_command_class, call_command
from django.core.management.base import NoArgsCommand

from fixturapp.management.commands import fixturapp_loadall
from fixturapp.tests.dummyapp.models import Dummy
from fixturapp.tests.dummyapp.datasets import DummyData


def create_command():
    return load_command_class('fixturapp', 'fixturapp_loadall')


class FixturappLoadAllTests(TestCase):

    def test_load_command_loadall(self):
        """
        Sucessfully load the command fixturapp_loadall from django project
        """
        self.assertTrue(isinstance(create_command(),
                                   fixturapp_loadall.Command))

    def test_command_is_valid_django_command(self):
        """Asserts that fixturapp_loadall command is a valid Django command"""
        self.assertTrue(isinstance(create_command(), NoArgsCommand))

    def test_fixture_was_loaded_by_calling_command(self):
        """Check if Dummy fixtures were loaded to the database"""
        call_command('fixturapp_loadall', verbosity=0)
        obj = Dummy.objects.get(name='Buster')
        self.assertEquals(obj.name, DummyData.buster.name)
