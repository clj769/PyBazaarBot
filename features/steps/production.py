from agent import Farmer

@given('a {worker} with {amount} {commodity}')
def step_impl(context, worker, amount, commodity):
    if worker == 'farmer':
        context.worker = Farmer(None)
        context.worker.inventory[commodity] = {'amount': int(amount)}
    else:
        context.worker = None

@when('he works')
def step_impl(context):
    context.worker.update()

@then('a {worker} has {amount} {commodity}')
def step_impl(context, worker, amount, commodity):
    assert context.worker.inventory[commodity]['amount'] == int(amount)

@given('a {worker} has a tool')
def step_impl(context, worker):
    context.worker.inventory['Tools'] = {'amount': 1}
