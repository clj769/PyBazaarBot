# from behave import given, when, then
# from agent import Agent
# from bazaar import Bazaar
#
#
# @given('a {worker} with {amount} {commodity}')
# def step_given_agent_with_commodity(context, worker, amount, commodity):
#     b = Bazaar()
#     context.worker = Agent(name=worker, occupation=worker,  bazaar=b, inventory={commodity: int(amount)})
#
# @given('a {worker} has a tool')
# def step_given_agent_has_tool(context, worker):
#     context.worker.inventory['Tools'] = 1
#
# @when('he works')
# def step_when_he_works(context):
#     context.worker.update()
#
#
# @then('a {worker} has {amount} {commodity}')
# def step_then_agent_has_commodity(context, worker, amount, commodity):
#     assert context.worker.inventory.get(commodity, 0) == int(amount)
#
#
