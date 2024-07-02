from payi import Payi

client = Payi(
    payi_api_key="foo"
    )

r = client.budgets.create(budget_name="foo", budget_amount=1000, budget_currency="USD")

