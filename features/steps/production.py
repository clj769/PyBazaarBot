from agent import Agent

@given('a {worker} with {amount} {commodity}')
def step_impl(context, worker, amount, commodity):
    if getattr(context, 'worker', None) is None:
        context.worker = Agent(occupation=worker)
    context.worker.inventory[commodity] = {'amount': int(amount)}

@when('he works')
def step_impl(context):
    context.worker.update()

@then('a {worker} has {amount} {commodity}')
def step_impl(context, worker, amount, commodity):
    assert context.worker.inventory.get(commodity, {}).get('amount', 0) == int(amount)

@given('a {worker} has a tool')
def step_impl(context, worker):
    context.worker.inventory['Tools'] = {'amount': 1}
