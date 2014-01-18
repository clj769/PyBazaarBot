from unittest.mock import Mock
from agent import Agent
from bazaar import Bazaar
import logging


def before_all(context):
    if not context.config.log_capture:
        logging.basicConfig(level=logging.DEBUG)

@given('a bazaar where two agents trade')
def step_impl(context):
    context.bazaar = Bazaar()
    context.buyer = Agent(context.bazaar)
    context.seller = Agent(context.bazaar)

@given('the {agent} has {amount} {commodity}')
def step_impl(context, agent, amount, commodity):
    if agent == 'buyer':
        context.buyer.inventory[commodity] = int(amount)
    elif agent == 'seller':
        context.seller.inventory[commodity] = int(amount)

@when('the seller wants to sell {amount} {commodity} for {value} Coins')
def step_impl(context, amount, commodity, value):
    context.seller.create_ask = Mock(return_value={
        'price': int(value),
        'amount': int(amount),
        'commodity': commodity,
        'seller': context.seller
    })
    ask = context.seller.create_ask()
    context.bazaar.register_ask(ask)

@when('the buyer wants to buy {amount} {commodity} for {value} Coins')
def step_impl(context, amount, commodity, value):
    context.buyer.create_bid = Mock(return_value={
        'price': int(value),
        'amount': int(amount),
        'commodity': commodity,
        'buyer': context.buyer
    })
    bid = context.buyer.create_bid()
    context.bazaar.register_bid(bid)

@then('the sale succeeds')
def step_impl(context):
    context.bazaar.update()

@then('the seller has {amount} Coins')
def step_impl(context, amount):
    assert int(context.seller.inventory['Coins']) == int(amount)

@then('the buyer has {amount} {commodity}')
def step_impl(context, amount, commodity):
    assert int(context.buyer.inventory[commodity]) == int(amount)

@given('a bazaar')
def step_impl(context):
    context.bazaar = Bazaar()

@then('he wants to buy Wood')
def step_impl(context):
    assert context.bazaar.ask_book != []

@then('he wants to sell Food')
def step_impl(context):
    assert context.bazaar.bid_book != []

@then('the books are empty')
def step_impl(context):
    assert len(context.bazaar.bid_book) == 0

@then('the bazaar has registered the trade')
def step_impl(context):
    assert len(context.bazaar.history) > 0
    trade = {'commodity': 'Wood', 'price': 7, 'amount': 2}
    assert context.bazaar.history[0] == [trade]

@when('the buyer wants to buy Wood')
def step_impl(context):
    context.buyer.create_bid('Wood', 10)

@then('the bazaar has not registered a bid')
def step_impl(context):
    assert len(context.bazaar.bid_book) == 0