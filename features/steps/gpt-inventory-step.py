# from behave import given, when, then
# from agent import Agent
#
# @given('the Agent')
# def step_given_agent(context):
#     context.agent = Agent()
#
# @when('given {amount} Tools')
# def step_when_given_tools(context, amount):
#     context.agent.inventory['Tools'] = int(amount)
#
# @then('the Agent owns {amount} Tools')
# def step_then_agent_owns_tools(context, amount):
#     assert context.agent.inventory.get('Tools', 0) == int(amount)
#
# @given('the Agent has {amount} inventory space')
# def step_given_agent_inventory_space(context, amount):
#     context.agent = Agent(inventory_space=int(amount))
#
# @when('given {amount} Food')
# def step_when_given_food(context, amount):
#     context.agent.inventory['Food'] = int(amount)
#
# @then('the Agent has {amount} inventory space left')
# def step_then_agent_has_inventory_left(context, amount):
#     assert context.agent.available_inventory_space == int(amount)
#
# @when('given {amount} Coins')
# def step_when_given_coins(context, amount):
#     context.agent.inventory['Coins'] = int(amount)
