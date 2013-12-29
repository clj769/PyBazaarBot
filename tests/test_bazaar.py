import json
import unittest
from unittest.mock import Mock, MagicMock
from agent import Agent
from bazaar import Bazaar


class TestBazaar(unittest.TestCase):
    def test_new_bazaar(self):
        b = Bazaar()
        self.assertIsNotNone(b)

    def test_register_ask(self):
        b = Bazaar()
        b.register_ask({'price': 4, 'amount': 4, 'commodity': 'Food'})
        self.assertEqual(len(b.ask_book), 1)

    def test_register_bid(self):
        b = Bazaar()
        b.register_bid({'price': 4, 'amount': 4, 'commodity': 'Food'})
        self.assertEqual(len(b.bid_book), 1)

    def test_resolve_offer(self):
        b = Bazaar()
        buyer = Agent(b, inventory={'Coins': {'amount': 16}})
        seller = Agent(b, inventory={'Food': {'amount': 4}})
        ask = {'price': 4, 'amount': 4, 'commodity': 'Food', 'seller': seller}
        bid = {'price': 4, 'amount': 4, 'commodity': 'Food', 'buyer': buyer}
        remaining_bid, remaining_ask = b.resolve_offer(bid, ask)
        self.assertIsNone(remaining_ask)
        self.assertIsNone(remaining_bid)
        self.assertEqual(buyer.inventory['Coins']['amount'], 0.0)
        self.assertEqual(buyer.inventory['Food']['amount'], 4)
        self.assertEqual(seller.inventory['Coins']['amount'], 16.0)
        self.assertEqual(seller.inventory['Food']['amount'], 0)

    def test_resolve_offers(self):
        b = Bazaar()
        buyer = Agent(b, inventory={'Coins': {'amount': 16}})
        seller = Agent(b, inventory={'Food': {'amount': 4}})
        b.register_ask({'price': 4, 'amount': 4, 'commodity': 'Food', 'seller': seller})
        b.register_bid({'price': 4, 'amount': 4, 'commodity': 'Food', 'buyer': buyer})
        self.assertEqual(len(b.bid_book), 1)
        self.assertEqual(len(b.ask_book), 1)
        b.update()
        self.assertEqual(len(b.bid_book), 0)
        self.assertEqual(len(b.ask_book), 0)