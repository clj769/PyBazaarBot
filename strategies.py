import logging


class Strategy(object):
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
            self.fine_agent()

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
        logging.debug("{} has {} Ore and {} Food".format(self, ore_amount, food_amount))
        if food_amount and self.inventory.get('Tools', 0):
            logging.warning("{} creates ore with tools".format(self))
            self.inventory['Food'] = food_amount - 1
            self.inventory['Ore'] = ore_amount + 4
        elif food_amount:
            logging.debug("{} creates ore without Tools".format(self))
            self.inventory['Food'] = food_amount - 1
            self.inventory['Ore'] = ore_amount + 2
        else:
            self.fine_agent()

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
            self.fine_agent()

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
            self.fine_agent()

    def refining(self):
        ore_amount = self.inventory.get('Ore', 0)
        metal_amount = self.inventory.get('Metal', 0)
        food_amount = self.inventory.get('Food', 0)
        if ore_amount and food_amount:
            self.inventory['Ore'] = 0
            self.inventory['Metal'] = metal_amount + ore_amount
            self.inventory['Food'] = food_amount - 1
        else:
            self.fine_agent()

    def nothing(self):
        pass

    @staticmethod
    def get_strategy(occupation):
        if occupation == 'farmer':
            minimum_amounts = {'Tools': 1, 'Wood': 5}
            return Strategy.farming, Strategy.farmer_trading, minimum_amounts
        elif occupation == 'woodcutter':
            minimum_amounts = {'Tools': 1, 'Food': 5}
            return Strategy.woodcutting, Strategy.woodcutter_trading, minimum_amounts
        elif occupation == 'miner':
            logging.debug("Creating a miner without a trading strategy or minimum amounts")
            return Strategy.mining, Strategy.nothing, {}
        elif occupation == 'blacksmith':
            logging.debug("Creating a blacksmith without a trading strategy or minimum amounts")
            return Strategy.blacksmithing, Strategy.nothing, {}
        elif occupation == 'refiner':
            logging.debug("Creating a refiner without a trading strategy or minimum amounts")
            return Strategy.refining, Strategy.nothing, {}
        else:
            return Strategy.nothing, Strategy.nothing, {}