import json
import random
from bazaar import Bazaar
from strategies import farming, mining


class Agent(object):
    weights = {
        'Tools': 1,
        'Coins': 0,
        'Food': 1
    }

    def __init__(self, bazaar=None, name=None, occupation=None, price_beliefs=None,
                 observed_trades=None, inventory=None,
                 inventory_space=100):
        #TODO: update price beliefs
        #TODO: update observed trades
        if name is not None:
            self.name = name
        else:
            self.name = repr(self)

        if occupation == 'farmer':
            self.perform_production = farming
        elif occupation == 'miner':
            self.perform_production = mining
        else:
            self.perform_production = farming

        self.occupation = occupation
        self.price_beliefs = price_beliefs

        if observed_trades:
            self.observed_trades = observed_trades
        else:
            self.observed_trades = {}

        if inventory:
            self.inventory = inventory
        else:
            self.inventory = {}

        self.bazaar = bazaar
        self.inventory_space = inventory_space

    @property
    def available_inventory_space(self):
        occupied_space = 0
        for name, properties in self.inventory.items():
            occupied_space += properties['amount'] * self.weights[name]

        return self.inventory_space - occupied_space

    def perform_production(self):
        pass

    def create_bid(self, commodity, limit):
        if limit <= 0:
            return None

        ideal = self.determine_purchase_quantity(commodity)

        bid = {'price': self.price_of(commodity),
               'amount': min(ideal, limit),
               'commodity': commodity,
               'buyer': self}

        if bid['amount'] > 0:
            return bid

        return None

    def create_ask(self, commodity, limit):
        ideal = self.determine_sale_quantity(commodity)

        ask = {'price': self.price_of(commodity),
               'amount': max(ideal, limit),
               'commodity': commodity,
               'seller': self}

        if ask['amount'] > 0:
            return ask

        return None

    def price_of(self, commodity):
        belief = self.price_beliefs[commodity]
        return random.randint(belief['low'], belief['high'])

    def determine_purchase_quantity(self, commodity):
        mean = self.bazaar.get_mean_price_of(commodity)
        trading_low, trading_high = self.observed_trading_range(commodity)

        #The lower the mean in the range, the more favorable it is
        favorability = 1 - self.favorability(mean, trading_low, trading_high)

        amount_to_buy = favorability * self.available_inventory_space
        return amount_to_buy

    def determine_sale_quantity(self, commodity):
        mean = self.bazaar.get_mean_price_of(commodity)
        trading_low, trading_high = self.observed_trading_range(commodity)

        favorability = self.favorability(mean, trading_low, trading_high)
        amount_to_sell = favorability * self.excess_inventory(commodity)
        return amount_to_sell

    def observed_trading_range(self, commodity):
        low = min(self.observed_trades.get(commodity, None))
        high = max(self.observed_trades.get(commodity, None))

        return low, high

    def favorability(self, mean, trading_low, trading_high):
        mean -= trading_low
        trading_high -= trading_low
        return mean / trading_high

    def excess_inventory(self, commodity):
        current = self.inventory[commodity]['amount']
        needed = self.inventory[commodity]['minimal']
        return current - needed
        
    def trade(self, other_agent, commodity, amount):
        self.inventory[commodity]['amount'] -= amount
        current_amount = other_agent.inventory.get(commodity, {}).get('amount',0)
        other_agent.inventory[commodity] = {'amount': current_amount + amount}
        #TODO: register observed trades and prices
        
    def pay(self, other_agent, amount):
        self.inventory['coins']['amount'] -= amount
        current_amount = other_agent.inventory.get('coins', {}).get('amount', 0)
        other_agent.inventory['coins'] = {'amount': current_amount + amount}

    def update(self):
        self.perform_production(self)


if __name__ == "__main__":
    with open('agents.json', 'r') as file:
        data = json.loads(file.read())
        paris = Bazaar()
        agents = []
        for element in data:
            agents.append(Agent(paris, **element))