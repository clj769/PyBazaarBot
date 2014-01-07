import logging


def farming(self):
    wood_amount = self.inventory.get('Wood', 0)
    food_amount = self.inventory.get('Food', 0)
    if wood_amount and self.inventory.get('Tools', 0):
        logging.info("{} is creating Food with tools".format(self.name))
        self.inventory['Wood'] = wood_amount - 1
        self.inventory['Food'] = food_amount + 4
    elif wood_amount:
        logging.info("{} is creating Food without tools".format(self.name))
        self.inventory['Wood'] = wood_amount - 1
        self.inventory['Food'] = food_amount + 2
    else:
        fine_agent(self)


def farmer_trading(self):
    wood_amount = self.inventory.get('Wood', 0)
    food_amount = self.inventory.get('Food', 0)
    if wood_amount < 2:
        self.bazaar.register_bid(self.create_bid('Wood', 10))
    if food_amount > 2:
        self.bazaar.register_ask(self.create_ask('Food', food_amount-2))


def mining(self):
    ore_amount = self.inventory.get('Ore', 0)
    food_amount = self.inventory.get('Food', 0)
    if food_amount and self.inventory.get('Tools', 0):
        self.inventory['Food'] = food_amount - 1
        self.inventory['Ore'] = ore_amount + 4
    elif food_amount:
        self.inventory['Food'] = food_amount - 1
        self.inventory['Ore'] = ore_amount + 2
    else:
        fine_agent(self)


def woodcutting(self):
    food_amount = self.inventory.get('Food', 0)
    wood_amount = self.inventory.get('Wood', 0)
    if food_amount and self.inventory.get('Tools', 0):
        self.inventory['Food'] = food_amount - 1
        self.inventory['Wood'] = wood_amount + 2
    elif food_amount:
        self.inventory['Food'] = food_amount - 1
        self.inventory['Wood'] = wood_amount + 1
    else:
        fine_agent(self)


def woodcutter_trading(self):
    wood_amount = self.inventory.get('Wood', 0)
    food_amount = self.inventory.get('Food', 0)
    if food_amount < 2:
        self.bazaar.register_bid(self.create_bid('Food', 10))
    if wood_amount > 2:
        self.bazaar.register_ask(self.create_ask('Wood', wood_amount-2))


def blacksmithing(self):
    metal_amount = self.inventory.get('Metal', 0)
    tools_amount = self.inventory.get('Tools', 0)
    if metal_amount:
        self.inventory['Metal'] = 0
        self.inventory['Tools'] = metal_amount + tools_amount
    else:
        fine_agent(self)


def refining(self):
    ore_amount = self.inventory.get('Ore', 0)
    metal_amount = self.inventory.get('Metal', 0)
    food_amount = self.inventory.get('Food', 0)
    if ore_amount and food_amount:
        self.inventory['Ore'] = 0
        self.inventory['Metal'] = metal_amount + ore_amount
        self.inventory['Food'] = food_amount - 1
    else:
        fine_agent(self)


def fine_agent(self):
    coins = self.inventory.get('Coins', 0)
    self.inventory['Coins'] -= 2
