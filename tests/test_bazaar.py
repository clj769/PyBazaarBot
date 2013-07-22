import json
import unittest
from unittest.mock import Mock, MagicMock
from Agent import Agent
from Bazaar import Bazaar


class TestBazaar(unittest.TestCase):
    def test_new_bazaar(self):
        b = Bazaar()
        self.assertIsNotNone(b)

    def test_register_ask(self):
        b = Bazaar()
        b.register_ask({'price': 4, 'quantity_to_buy': 4, 'commodity': 'Food'})
        self.assertEqual(len(b.bid_book), 1)

    def test_register_bid(self):
        b = Bazaar()
        b.register_bid({'price': 4, 'quantity_to_sell': 4, 'commodity': 'Food'})
        self.assertEqual(len(b.ask_book), 1)

    def test_resolve_offers(self):
        b = Bazaar()
        b.register_ask({'price': 4, 'quantity_to_buy': 4, 'commodity': 'Food'})
        b.register_bid({'price': 4, 'quantity_to_sell': 4, 'commodity': 'Food'})
        self.assertEqual(len(b.bid_book), 1)
        self.assertEqual(len(b.ask_book), 1)
        b.resolve_offers()
        self.assertEqual(len(b.bid_book), 0)
        self.assertEqual(len(b.ask_book), 0)
