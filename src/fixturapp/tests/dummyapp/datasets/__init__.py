from fixture import DataSet

class DummyData(DataSet):
    class Meta:
        django_app_label = 'dummy'
    class ragdoll:
        name = "Boneca de Meia"
        origin = "Olinda"
    class buster:
        name = "Buster"
        origin = "Myth Buster"

