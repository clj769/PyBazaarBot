import unittest
from agent import Farmer


class TestFarmer(unittest.TestCase):
    def test_new_farmer(self):
        f = Farmer(None)
        self.assertIsNotNone(f, "Farmer not created properly")

    def test_new_farmer_with_args(self):
        f = Farmer(bazaar=None, occupation='Farmer', name="Joe")
        self.assertIsNotNone(f)