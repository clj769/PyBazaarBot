import json
import unittest
from unittest.mock import Mock, MagicMock
from agent import Agent


class TestAgent(unittest.TestCase):
    def setUp(self):
        data = [{
            "occupation": "Farmer",
            "price_beliefs": {
                "Food": {"low": 0, "high": 100},
                "Tools": {"low": 50, "high": 75}},
            "inventory": {
                "Food": {"amount": 5, "minimal": 2},
                "Tools": {"amount": 5, "minimal": 1}}
        }]
        self.agents = []
        Bazaar = Mock()
        for e in data:
            self.agents.append(Agent(Bazaar(), **e))

    def test_price_of(self):
        agent = self.agents[0]
        price = agent.price_of('Food')
        low = agent.price_beliefs['Food']['low']
        high = agent.price_beliefs['Food']['high']
        self.assertGreaterEqual(price, low)
        self.assertLessEqual(price, high)

    def test_create_bid(self):
        agent = self.agents[0]
        agent.determine_purchase_quantity = MagicMock(return_value=10)
        bid = agent.create_bid('Food', 10)
        self.assertIsNotNone(bid)

    def test_create_ask(self):
        agent = self.agents[0]
        agent.determine_sale_quantity = MagicMock(return_value=10)
        bid = agent.create_ask('Food', 10)
        self.assertIsNotNone(bid)

    def test_determine_purchase_quantity(self):
        agent = self.agents[0]
        agent.bazaar.get_mean_price_of = MagicMock(return_value=5)
        agent.observed_trading_range = MagicMock(return_value=(0,100))
        agent.favorability = MagicMock(return_value=0.25)
        quantity = agent.determine_purchase_quantity('Food')
        self.assertEqual(quantity, 0.75*90)

    def test_observed_trading_range(self):
        agent = self.agents[0]
        agent.observed_trades['Food'] = [10, 12, 11, 10, 9]
        low, high = agent.observed_trading_range('Food')
        self.assertEqual(low, 9)
        self.assertEqual(high, 12)

    def test_determine_favorability(self):
        agent = self.agents[0]
        result = agent.favorability(5, 0, 10)
        self.assertEqual(result, 0.5)
        result2 = agent.favorability(5, 2.5, 12.5)
        self.assertEqual(result2, 0.25)

    def test_available_inventory_space(self):
        agent = self.agents[0]
        result = agent.available_inventory_space
        self.assertEqual(result, 100-10)

    def test_determine_sale_quantity(self):
        agent = self.agents[0]
        agent.bazaar.get_mean_price_of = MagicMock(return_value=5)
        agent.observed_trading_range = MagicMock(return_value=(0,100))
        agent.favorability = MagicMock(return_value=0.25)
        agent.excess_inventory = MagicMock(return_value=10)
        quantity = agent.determine_sale_quantity('Food')
        self.assertEqual(quantity, 0.25*10)

    def test_excess_inventory(self):
        agent = self.agents[0]
        result = agent.excess_inventory('Food')
        self.assertEqual(result, 5-2)
        
    def test_zero_bid_results_in_no_bid(self):
        agent = self.agents[0]
        result = agent.create_bid('Food', 0)
        self.assertIsNone(result)