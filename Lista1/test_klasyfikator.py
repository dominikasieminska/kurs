from unittest import TestCase
from Lista1.lista1_7 import klasyfikator, NotStringError

class TestKlasyfikator(TestCase):
    def test_klasyfikator(self):
        self.assertEqual(klasyfikator(""), 1)
        self.assertEqual(silnia(1), 1)
        self.assertEqual(silnia(3), 6)

    def test_badargument(self):
        with self.assertRaises(NotIntError):
            silnia("dwa")
