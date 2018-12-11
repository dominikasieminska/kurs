from unittest import TestCase

from silnia import silnia, NotIntError

class TestSilnia(TestCase):
    def test_silnia(self):
        self.assertEqual(silnia(0), 1)
        self.assertEqual(silnia(1), 1)
        self.assertEqual(silnia(3), 6)

    def test_badargument(self):
        with self.assertRaises(NotIntError):
            silnia("dwa")
