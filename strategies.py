def farming(self):
    wood_amount = self.inventory.get('Wood', {}).get('amount', 0)
    food_amount = self.inventory.get('Food', {}).get('amount', 0)
    if wood_amount and self.inventory.get('Tools', {}).get('amount', 0):
        self.inventory['Wood'] = {'amount': wood_amount - 1}
        self.inventory['Food'] = {'amount': food_amount + 4}
    elif wood_amount:
        self.inventory['Wood'] = {'amount': wood_amount - 1}
        self.inventory['Food'] = {'amount': food_amount + 2}
    else:
        fine_agent(self)


def mining(self):
    ore_amount = self.inventory.get('Ore', {}).get('amount', 0)
    food_amount = self.inventory.get('Food', {}).get('amount', 0)
    if food_amount and self.inventory.get('Tools', {}).get('amount', 0):
        self.inventory['Food'] = {'amount': food_amount - 1}
        self.inventory['Ore'] = {'amount': ore_amount + 4}
    elif food_amount:
        self.inventory['Food'] = {'amount': food_amount - 1}
        self.inventory['Ore'] = {'amount': ore_amount + 2}
    else:
        fine_agent(self)


def woodcutting(self):
    food_amount = self.inventory.get('Food', {}).get('amount', 0)
    wood_amount = self.inventory.get('Wood', {}).get('amount', 0)
    if food_amount and self.inventory.get('Tools', {}).get('amount', 0):
        self.inventory['Food'] = {'amount': food_amount - 1}
        self.inventory['Wood'] = {'amount': wood_amount + 2}
    elif food_amount:
        self.inventory['Food'] = {'amount': food_amount - 1}
        self.inventory['Wood'] = {'amount': wood_amount + 1}
    else:
        fine_agent(self)


def blacksmithing(self):
    metal_amount = self.inventory.get('Metal', {}).get('amount', 0)
    tools_amount = self.inventory.get('Tools', {}).get('amount', 0)
    if metal_amount:
        self.inventory['Metal'] = {'amount': 0}
        self.inventory['Tools'] = {'amount': metal_amount + tools_amount}
    else:
        fine_agent(self)


def refining(self):
    ore_amount = self.inventory.get('Ore', {}).get('amount', 0)
    metal_amount = self.inventory.get('Metal', {}).get('amount', 0)
    food_amount = self.inventory.get('Food', {}).get('amount', 0)
    if ore_amount and food_amount:
        self.inventory['Ore'] = {'amount': 0}
        self.inventory['Metal'] = {'amount': metal_amount + ore_amount}
        self.inventory['Food'] = {'amount': food_amount - 1}
    else:
        fine_agent(self)


def nothing(self):
    pass


def fine_agent(self):
    coins = self.inventory.get('Coins', {}).get('amount', 0)
    self.inventory['Coins']['amount'] = coins - 2