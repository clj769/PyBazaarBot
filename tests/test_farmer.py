import unittest
from agent import Farmer


class TestFarmer(unittest.TestCase):
    def test_new_farmer(self):
        f = Farmer(None)
        self.assertIsNotNone(f, "Farmer not created properly")

    def test_new_farmer_with_name(self):
        f = Farmer(bazaar=None, name="Joe")
        self.assertIsNotNone(f)

    def test_farmer_occupation(self):
        f = Farmer(bazaar=None)
        self.assertEqual(f.occupation, 'Farmer')

    def test_production(self):
        f = Farmer(bazaar=None)
        f.inventory['Wood'] = {'amount': 1}
        f.perform_production()
        food_amount = f.inventory['Food']['amount']
        self.assertEqual(food_amount, 2)