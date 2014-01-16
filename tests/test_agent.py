import json
import unittest
from unittest.mock import Mock, MagicMock
from agent import Agent
from bazaar import Bazaar


class TestAgent(unittest.TestCase):
    def test_price_of(self):
        agent = Agent()
        agent.price_beliefs['Food'] = {'low': 0, 'high': 10}
        price = agent.price_of('Food')
        low = agent.price_beliefs['Food']['low']
        high = agent.price_beliefs['Food']['high']
        self.assertGreaterEqual(price, low)
        self.assertLessEqual(price, high)

    def test_create_bid(self):
        agent = Agent()
        agent.determine_purchase_quantity = MagicMock(return_value=10)
        bid = agent.create_bid('Food', 10)
        self.assertIsNotNone(bid)

    def test_create_ask(self):
        agent = Agent()
        agent.determine_sale_quantity = MagicMock(return_value=10)
        bid = agent.create_ask('Food', 10)
        self.assertIsNotNone(bid)

    def test_determine_purchase_quantity(self):
        b = Bazaar()
        agent = Agent(bazaar=b, inventory_space=100)
        agent.inventory['Wood'] = 10

        agent.bazaar.get_mean_price_of = MagicMock(return_value=5)
        agent.observed_trading_range = MagicMock(return_value=(0, 10))
        agent.favorability = MagicMock(return_value=0.25)
        quantity = agent.determine_purchase_quantity('Food')
        self.assertEqual(quantity, 0.75*90)

    def test_observed_trading_range(self):
        agent = Agent()
        agent.observed_trades['Food'] = [10, 12, 11, 10, 9]
        low, high = agent.observed_trading_range('Food')
        self.assertEqual(low, 9)
        self.assertEqual(high, 12)

    def test_determine_favorability(self):
        agent = Agent()
        result = agent.favorability(5, 0, 10)
        self.assertEqual(result, 0.5)
        result2 = agent.favorability(5, 2.5, 12.5)
        self.assertEqual(result2, 0.25)

    def test_available_inventory_space(self):
        agent = Agent(inventory_space=100)
        agent.inventory['Wood'] = 10
        result = agent.available_inventory_space
        self.assertEqual(result, 90)

    def test_determine_sale_quantity(self):
        b = Bazaar()
        agent = Agent(bazaar=b)

        agent.bazaar.get_mean_price_of = MagicMock(return_value=5)
        agent.observed_trading_range = MagicMock(return_value=(0,100))
        agent.favorability = MagicMock(return_value=0.25)
        agent.excess_inventory = MagicMock(return_value=10)
        quantity = agent.determine_sale_quantity('Food')
        self.assertEqual(quantity, 0.25*10)

    def test_excess_inventory(self):
        agent = Agent()
        agent.inventory['Food'] = 5
        agent.minimum_amounts['Food'] = 2
        result = agent.excess_inventory('Food')
        self.assertEqual(result, 5-2)
        
    def test_zero_bid_results_in_no_bid(self):
        agent = Agent()
        result = agent.create_bid('Food', 0)
        self.assertIsNone(result)

    def test_create_farmer(self):
        agent = Agent(occupation='farmer')
        self.assertIsNotNone(agent, "Farmer was not created")
        self.assertEqual(agent.occupation, "farmer")

    def test_create_miner(self):
        agent = Agent(occupation='miner')
        self.assertIsNotNone(agent, "Miner was not created")
        self.assertEqual(agent.occupation, "miner")

    def test_create_woodcutter(self):
        agent = Agent(occupation='woodcutter')
        self.assertIsNotNone(agent, "Woodcutter was not created")
        self.assertEqual(agent.occupation, "woodcutter")

    def test_create_blacksmith(self):
        agent = Agent(occupation='blacksmith')
        self.assertIsNotNone(agent, "Blacksmith was not created")
        self.assertEqual(agent.occupation, "blacksmith")

    def test_create_refiner(self):
        agent = Agent(occupation='refiner')
        self.assertIsNotNone(agent, "Refiner was not created")
        self.assertEqual(agent.occupation, "refiner")

    def test_price_beliefs(self):
        price_beliefs = {'Food': {'low': 0, 'high': 10} }
        agent = Agent(price_beliefs=price_beliefs)
        self.assertIsNotNone(agent)

    def test_negative_buy_orders(self):
        b = Bazaar()
        agent = Agent(b)
        agent.determine_sale_quantity = MagicMock(return_value=-1)
        ask = agent.create_ask('Food', 10)
        self.assertIsNone(ask)

    def test_negative_sale_orders(self):
        b = Bazaar()
        agent = Agent(b)
        agent.determine_purchase_quantity = MagicMock(return_value=-1)
        ask = agent.create_bid('Food', 10)
        self.assertIsNone(ask)

    def test_observed_trading_ranges(self):
        agent = Agent()
        low, high = agent.observed_trading_range('Food')
        self.assertEqual(low, 0)
        self.assertEqual(high, 100)

    def test_inventory(self):
        agent = Agent()
        agent.inventory['Food'] = 10
        self.assertEqual(agent.inventory['Food'], 10)

    def test_add_to_inventory(self):
        agent = Agent()
        agent.inventory['Wood'] = 0
        agent.inventory['Wood'] += 5
        self.assertEqual(agent.inventory['Wood'], 5)

    def test_empty_inventory(self):
        agent = Agent()
        self.assertEqual(agent.inventory.get('Wood', 0), 0)

    def test_remove_from_inventory(self):
        agent = Agent()
        agent.inventory['Ore'] = 3
        agent.inventory['Ore'] -= 3
        self.assertEqual(agent.inventory['Ore'], 0)