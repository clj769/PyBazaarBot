from unittest.mock import Mock
from behave import *
from agent import Agent
from bazaar import Bazaar


@given('a bazaar where two agents trade')
def step_impl(context):
    context.bazaar = Bazaar()
    context.buyer = Agent(context.bazaar)
    context.seller = Agent(context.bazaar)

@given('the {agent} has {amount} {commodity}')
def step_impl(context, agent, amount, commodity):
    if agent == 'buyer':
        context.buyer.inventory[commodity] = {'amount': int(amount)}
    elif agent == 'seller':
        context.seller.inventory[commodity] = {'amount': int(amount)}

@when('the seller wants to sell {amount} {commodity} for {value} coins')
def step_impl(context, amount, commodity, value):
    context.seller.create_ask = Mock(return_value={
        'price': int(value),
        'amount': int(amount),
        'commodity': commodity,
        'seller': context.seller
    })
    ask = context.seller.create_ask()
    context.bazaar.register_ask(ask)

@when('the buyer wants to buy {amount} {commodity} for {value} coins')
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

@then('the seller has {amount} coins')
def step_impl(context, amount):
    assert int(context.seller.inventory['coins']['amount']) == int(amount)

@then('the buyer has {amount} {commodity}')
def step_impl(context, amount, commodity):
    assert int(context.buyer.inventory[commodity]['amount']) == int(amount)

@then('a bid remains on the bid book')
def step_impl(context):
    assert len(context.bazaar.bid_book) > 0