from unittest.mock import Mock
from behave import *
from Agent import Agent
from Bazaar import Bazaar


@given('a bazaar with two agents')
def step_impl(context):
    context.bazaar = Bazaar()
    context.buyer = Agent(context.bazaar)
    context.seller = Agent(context.bazaar)

@given('{agent} has {amount} {item}')
def step_impl(context, agent, amount, item):
    if agent == 'buyer':
        context.buyer.inventory[item] = {'amount': amount}
    else:
        context.seller.inventory[item] = {'amount': amount}

@when('the seller wants to sell 1 food for 2 coins')
def step_impl(context):
    context.seller.create_bid = Mock(return_value={
        'bid_price': 2,
        'quantity_to_sell': 1,
        'commodity': 'Food'
    })
    bid = context.seller.create_bid()
    context.bazaar.register_bid(bid)

@when('the buyer wants to buy 1 food for 2 coins')
def step_impl(context):
    context.buyer.create_ask = Mock(return_value={
        'bid_price': 2,
        'quantity_to_buy': 1,
        'commodity': 'Food'
    })
    bid = context.buyer.create_ask()
    context.bazaar.register_ask(bid)

@then('the sale succeeds')
def step_impl(context):
    context.bazaar.update()

@then('the seller has 2 coins')
def step_impl(context):
    assert False

@then('the buyer has 1 food')
def step_impl(context):
    assert False
