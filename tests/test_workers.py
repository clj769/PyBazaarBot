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

    def test_farmer_production(self):
        f = Agent(occupation='farmer')
        f.inventory['Wood'] = 1
        f.perform_production()
        food_amount = f.inventory['Food']
        self.assertEqual(food_amount, 2)

    def test_miner_production(self):
        f = Agent(occupation='miner')
        f.inventory['Food'] = 1
        f.perform_production()
        ore_amount = f.inventory['Ore']
        self.assertEqual(ore_amount, 2)

    def test_woodcutter_production(self):
        f = Agent(occupation='woodcutter')
        f.inventory['Food'] = 1
        f.perform_production()
        wood_amount = f.inventory['Wood']
        self.assertEqual(wood_amount, 1)

    def test_blacksmith_production(self):
        f = Agent(occupation='blacksmith')
        f.inventory['Metal'] = 1
        f.perform_production()
        tools_amount = f.inventory['Tools']
        self.assertEqual(tools_amount, 1)

    def test_blacksmith_production_whole(self):
        f = Agent(occupation='blacksmith')
        f.inventory['Metal'] = 10
        f.perform_production()
        tools_amount = f.inventory['Tools']
        self.assertEqual(tools_amount, 10)