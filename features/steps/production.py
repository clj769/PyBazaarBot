from agent import Agent
from bazaar import Bazaar

@given('a {worker} with {amount} {commodity}')
def step_impl(context, worker, amount, commodity):
    if getattr(context, 'worker', None) is None:
        b = Bazaar()
        context.worker = Agent(occupation=worker, bazaar=b)
    context.worker.inventory[commodity] = int(amount)

@when('he works')
def step_impl(context):
    context.worker.update()

@then('a {worker} has {amount} {commodity}')
def step_impl(context, worker, amount, commodity):
    assert context.worker.inventory.get(commodity, 0) == int(amount)

@given('a {worker} has a tool')
def step_impl(context, worker):
    context.worker.inventory['Tools'] = 1
