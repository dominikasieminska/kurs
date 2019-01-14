from unittest import TestCase
from Lista2.lista2_7 import zbuduj_zdania, NotListError

class TestZbuduj_zdania(TestCase):
    def test_zbuduj_zdania(self):
        lista = [["łódź", "się", "obudziła"],["ogary", "poszły", "w", "las"]]
        self.assertEqual(zbuduj_zdania(lista), "Łódź się obudziła. Ogary poszły w las. ")

    def test_badargument(self):
        with self.assertRaises(NotListError):
            zbuduj_zdania(2)

