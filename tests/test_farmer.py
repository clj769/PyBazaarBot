import unittest
from agent import Agent


class TestWorkers(unittest.TestCase):
    def test_new_farmer(self):
        f = Agent(occupation='farmer')
        self.assertIsNotNone(f, "Farmer not created properly")

    def test_new_farmer_with_name(self):
        f = Agent(occupation='farmer', name="Joe")
        self.assertIsNotNone(f)

    def test_farmer_occupation(self):
        f = Agent(occupation='farmer')
        self.assertEqual(f.occupation, 'farmer')

    def test_production(self):
        f = Agent(occupation='farmer')
        f.inventory['Wood'] = {'amount': 1}
        f.perform_production(f)
        food_amount = f.inventory['Food']['amount']
        self.assertEqual(food_amount, 2)