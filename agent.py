import logging, sys, random, types
from bazaar import Bazaar
from strategies import farming, mining, woodcutting, blacksmithing, refining
from strategies import farmer_trading, woodcutter_trading


class Agent(object):
    weights = {
        'Tools': 1,
        'Coins': 0,
        'Food': 1,
        'Wood': 1
    }

    def __init__(self, bazaar=None, name=None, occupation=None, price_beliefs=None, minimum_amounts=None,
                 inventory=None, inventory_space=100):
        #TODO: update price beliefs
        #TODO: update observed trades
        if name is not None:
            self.name = name
        else:
            self.name = repr(self)

        if inventory:
            self.inventory = inventory
        else:
            self.inventory = {}

        if occupation == 'farmer':
            self.perform_production = types.MethodType(farming, self)
            self.generate_offers = types.MethodType(farmer_trading, self)
            self.minimum_amounts = {'Wood': 2, 'Coins': 0, 'Food': 0}
        elif occupation == 'miner':
            self.perform_production = types.MethodType(mining, self)
        elif occupation == 'woodcutter':
            self.perform_production = types.MethodType(woodcutting, self)
            self.generate_offers = types.MethodType(woodcutter_trading, self)
            self.minimum_amounts = {'Wood': 0, 'Coins': 0, 'Food': 4}
        elif occupation == 'blacksmith':
            self.perform_production = types.MethodType(blacksmithing, self)
        elif occupation == 'refiner':
            self.perform_production = types.MethodType(refining, self)

        self.occupation = occupation

        if price_beliefs:
            self.price_beliefs = price_beliefs
        else:
            self.price_beliefs = {}

        if minimum_amounts:
            self.minimum_amounts = minimum_amounts
        else:
            self.minimum_amounts = {}

        self.observed_trades = {}
        self.bazaar = bazaar
        self.inventory_space = inventory_space

    def __str__(self):
        return self.name

    @property
    def available_inventory_space(self):
        occupied_space = 0
        for name, properties in self.inventory.items():
            occupied_space += properties['amount'] * self.weights[name]

        return self.inventory_space - occupied_space

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
               'amount': min(ideal, limit),
               'commodity': commodity,
               'seller': self}

        if ask['amount'] > 0:
            return ask

        return None

    def price_of(self, commodity):
        belief = self.price_beliefs.get(commodity, {'low': 0, 'high': 100})
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
        if self.observed_trades:
            observed_trades = self.observed_trades.get(commodity, None)
        else:
            observed_trades = None

        if observed_trades:
            low = min(observed_trades)
            high = max(observed_trades)
        else:
            low = 0
            high = 100

        return low, high

    def favorability(self, mean, trading_low, trading_high):
        mean -= trading_low
        trading_high -= trading_low
        return mean / trading_high

    def excess_inventory(self, commodity):
        current = self.inventory.get(commodity, {'amount': 0})['amount']
        needed = self.minimum_amounts[commodity]
        return current - needed
        
    def trade(self, other_agent, commodity, amount):
        self.inventory[commodity]['amount'] -= amount
        current_amount = other_agent.inventory.get(commodity, {}).get('amount',0)
        other_agent.inventory[commodity] = {'amount': current_amount + amount}
        #TODO: register observed trades and prices
        
    def pay(self, other_agent, amount):
        self.inventory['Coins']['amount'] -= amount
        current_amount = other_agent.inventory.get('Coins', {}).get('amount', 0)
        other_agent.inventory['Coins'] = {'amount': current_amount + amount}

    def update(self):
        self.perform_production()
        self.generate_offers()

    def perform_production(self):
        raise NotImplementedError('Production strategy must be bound at __init__')

    def generate_offers(self):
        raise NotImplementedError('Trading strategy must be bound at __init__')

if __name__ == "__main__":  # pragma: no cover
    logging.basicConfig(level=logging.DEBUG)

    b = Bazaar()
    agents = []
    for i in range(1):
        agents.append(Agent(bazaar=b, occupation='farmer', name='farmer#'+str(i)))
        agent = agents[-1]
        agent.inventory['Wood'] = {'amount': 5}
        agent.inventory['Coins'] = {'amount': 10}
        agent.inventory['Food'] = {'amount': 0}
        agent.price_beliefs['Food'] = {'low': 2, 'high': 14}
        agent.price_beliefs['Wood'] = {'low': 1, 'high': 8}

    for i in range(1):
        agents.append(Agent(bazaar=b, occupation='woodcutter', name='woodcutter#'+str(i)))
        agent = agents[-1]
        agent.inventory['Wood'] = {'amount': 0}
        agent.inventory['Coins'] = {'amount': 10}
        agent.inventory['Food'] = {'amount': 8}
        agent.price_beliefs['Food'] = {'low': 2, 'high': 14}
        agent.price_beliefs['Wood'] = {'low': 1, 'high': 8}

    for i in range(11):
        for agent in agents:
            agent.update()
            logging.debug(agent.name + str(agent.inventory))
        logging.debug("Ask book: {}".format(b.ask_book))
        logging.debug("Bid book: {}".format(b.bid_book))
        b.update()
        logging.debug("---")