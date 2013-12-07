def farming(self):
    wood_amount = self.inventory.get('Wood', {}).get('amount', 0)
    food_amount = self.inventory.get('Food', {}).get('amount', 0)
    if wood_amount:
        self.inventory['Wood'] = {'amount': wood_amount - 1}
        self.inventory['Food'] = {'amount': food_amount + 2}


def mining(self):
    ore_amount = self.inventory.get('Ore', {}).get('amount', 0)
    food_amount = self.inventory.get('Food', {}).get('amount', 0)
    if food_amount:
        self.inventory['Ore'] = {'amount': ore_amount + 2}
        self.inventory['Food'] = {'amount': food_amount - 1}


def nothing(self):
    pass