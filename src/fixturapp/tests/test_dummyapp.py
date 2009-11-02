from fixture import DataSet, DjangoFixture
from fixture.django_testcase import FixtureTestCase
from fixture.style import NamedDataStyle

from fixturapp.tests.dummyapp.models import Dummy
from fixturapp.tests.dummyapp.datasets import DummyData


class TestDummyapp(FixtureTestCase):
    """
    Sample TestCase
    """
    fixture = DjangoFixture(style=NamedDataStyle())
    datasets = [DummyData]

    def test_loaded_fixtures(self):
        """
        Check DummyData was loaded at setup.
        """
        # Check ragdoll
        obj = Dummy.objects.get(id=self.data.DummyData.ragdoll.id)
        self.assertTrue(obj.id is not None)
        self.assertEqual(obj.name, self.data.DummyData.ragdoll.name)
        # Check buster
        obj = Dummy.objects.get(id=self.data.DummyData.buster.id)
        self.assertTrue(obj.id is not None)
        self.assertEqual(obj.name, self.data.DummyData.buster.name)
