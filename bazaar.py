import random


class Bazaar():
    def __init__(self):
        self.bid_book = []
        self.ask_book = []

    def register_ask(self, ask):
        self.bid_book.append(ask)

    def register_bid(self, bid):
        self.ask_book.append(bid)

    def update(self):
        self.resolve_offers()

    def resolve_offers(self):
        random.shuffle(self.bid_book)
        random.shuffle(self.ask_book)

        self.bid_book.sort(key=lambda bid: bid['price'])
        self.ask_book.sort(key=lambda ask: ask['price'], reverse=True)
        
        while self.bid_book and self.ask_book:
            bid = self.bid_book.pop()
            ask = self.ask_book.pop()
            
            if bid['price'] >= ask['price']:
                remaining_bid, remaining_ask = self.resolve_offer(bid, ask)

                if remaining_ask:
                    self.ask_book.append(remaining_ask)
                if remaining_bid:
                    self.bid_book.append(remaining_bid)
            else:
                break

    def resolve_offer(self, bid, ask):
        buyer = bid['buyer']
        seller = ask['seller']
        
        trade_price = (bid['price'] + ask['price']) / 2.0
        trade_amount = min(bid['amount'], ask['amount'])
        
        seller.trade(buyer, bid['commodity'], trade_amount)
        buyer.pay(seller, trade_amount*trade_price)

        if bid['amount'] == trade_amount:
            bid = None
        else:
            bid['amount'] -= trade_amount

        if ask['amount'] == trade_amount:
            ask = None
        else:
            ask['amount'] -= trade_amount

        return bid, ask