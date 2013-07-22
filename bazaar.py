import random


class Bazaar():
    def __init__(self):
        self.bid_book = []
        self.ask_book = []

    def register_ask(self, ask):
        self.bid_book.append(ask)

    def register_bid(self, bid):
        self.ask_book.append(bid)

    def resolve_offers(self):
        random.shuffle(self.bid_book)
        random.shuffle(self.ask_book)

        sorted_bid_book = sorted(self.bid_book, key=lambda bid: bid['price'])
        sorted_ask_book = sorted(self.ask_book, key=lambda ask: ask['price'])

        for bid in sorted_bid_book:
            if bid['price'] >= sorted_ask_book.pop()['price']:

        #TODO: finish this function