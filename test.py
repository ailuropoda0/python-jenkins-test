from unittest import TestCase
from sample import add


class UtilsTests(TestCase):
    def test_sample(self):
        self.assertEqual(add("13", "42"), 55)
