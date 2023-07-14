# from behave import given, when, then
# from bazaar import Bazaar
# from agent import Agent
#
# @given('a bazaar where two agents trade')
# def step_given_a_bazaar(context):
#     context.bazaar = Bazaar()
#     context.seller = Agent(name='seller', inventory={}, bazaar=context.bazaar)
#     context.buyer = Agent(name='buyer', inventory={}, bazaar=context.bazaar)
#
# @given('the seller has {amount} {commodity}')
# def step_given_seller_has_commodity(context, amount, commodity):
#     context.seller.inventory[commodity] = int(amount)
#
# @given('the buyer has {amount} {commodity}')
# def step_given_buyer_has_commodity(context, amount, commodity):
#     context.buyer.inventory[commodity] = int(amount)
#
# @when('the seller wants to sell {amount} {commodity} for {price} Coins')
# def step_seller_wants_to_sell(context, amount, commodity, price):
#     ask = {
#         'seller': context.seller,
#         'commodity': commodity,
#         'amount': int(amount),
#         'price': float(price)
#     }
#     context.bazaar.register_ask(ask)
#
# @when('the buyer wants to buy {amount} {commodity} for {price} Coins')
# def step_buyer_wants_to_buy(context, amount, commodity, price):
#     bid = {
#         'buyer': context.buyer,
#         'commodity': commodity,
#         'amount': int(amount),
#         'price': float(price)
#     }
#     context.bazaar.register_bid(bid)
#
# from behave import when
#
# @when(u'the buyer wants to buy Wood')
# def step_buyer_wants_to_buy_wood(context):
#     # Assuming the buyer is willing to pay 1 Coin for Wood
#     bid = {
#         'buyer': context.buyer,
#         'commodity': 'Wood',
#         'amount': 1,
#         'price': 1.0  # Price for each unit of Wood
#     }
#     context.bazaar.register_bid(bid)
#
#
# @then('the sale succeeds')
# def step_the_sale_succeeds(context):
#     context.bazaar.update()
#
# @then('the seller has {amount} Coins')
# def step_seller_has_coins(context, amount):
#     assert context.seller.inventory['Coins'] == int(amount)
#
# @then('the buyer has {amount} {commodity}')
# def step_buyer_has_commodity(context, amount, commodity):
#     assert context.buyer.inventory[commodity] == int(amount)
#
# @then('the books are empty')
# def step_the_books_are_empty(context):
#     assert not context.bazaar.bid_book
#     assert not context.bazaar.ask_book
#
# @then('the bazaar has registered the trade')
# def step_bazaar_has_registered_the_trade(context):
#     assert len(context.bazaar.history) > 0
#
# @then('the bazaar has not registered a bid')
# def step_bazaar_has_not_registered_a_bid(context):
#     context.bazaar.update()
#     assert len(context.bazaar.bid_book) == 0
