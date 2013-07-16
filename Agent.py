import json
import random


class Agent():
    def __init__(self, dict, bazaar):
        self.dict = dict
        self.price_beliefs = dict['price_beliefs']
        self.observed_trades = {}
        self.money = dict['money']
        self.inventory = dict['inventory']
        self.bazaar = bazaar
        self.inventory_space = 100

    def __repr__(self):
        return str(self.dict)

    @property
    def available_inventory_space(self):
        occupied_space = sum(x[1] for items in self.inventory.values()
                             for x in items.items() if x[0]=='amount' )
        return self.inventory_space - occupied_space

    def create_bid(self, commodity, limit):
        ideal = self.determine_purchase_quantity(commodity)

        bid = {'bid_price': self.price_of(commodity),
               'quantity_to_buy': min(ideal, limit)}

        if bid['quantity_to_buy'] > 0:
            return bid

        return None

    def create_ask(self, commodity, limit):
        ideal = self.determine_sale_quantity(commodity)

        bid = {'bid_price': self.price_of(commodity),
               'quantity_to_sell': max(ideal, limit)}

        if bid['quantity_to_sell'] > 0:
            return bid

        return None

    def price_of(self, commodity):
        belief = self.price_beliefs[commodity]
        return random.randint(belief['low'], belief['high'])

    def determine_purchase_quantity(self, commodity):
        mean = self.bazaar.get_mean_price_of(commodity)
        trading_low, trading_high = self.observed_trading_range(commodity)
        favorability = 1 - self.favorability(mean, trading_low, trading_high)
        #The lower the mean in the range, the more favorable it is
        amount_to_buy = favorability * self.available_inventory_space
        return amount_to_buy

    def determine_sale_quantity(self, commodity):
        mean = self.bazaar.get_mean_price_of(commodity)
        trading_low, trading_high = self.observed_trading_range(commodity)
        favorability = self.favorability(mean, trading_low, trading_high)
        amount_to_sell = favorability * self.excess_inventory(commodity)
        return amount_to_sell

    def observed_trading_range(self, commodity):
        low = min(self.observed_trades[commodity])
        high = max(self.observed_trades[commodity])

        return low, high

    def favorability(self, mean, trading_low, trading_high):
        mean -= trading_low
        trading_high -= trading_low
        return mean/trading_high

    def excess_inventory(self, commodity):
        current = self.inventory[commodity]['amount']
        needed = self.inventory[commodity]['minimal']
        return current - needed


if __name__ == "__main__":
    with open('agents.json', 'r') as file:
        data = json.loads(file.read())
        agents = []
        for e in data:
            agents.append(Agent(e))

        for a in agents:
            print(a)