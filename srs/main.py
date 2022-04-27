from fastapi import FastAPI,  HTTPException
from srs.helpers.injector import get_container as data
from srs.models.customer import Customer

app = FastAPI()


@app.get("/customers")
async def get_all():
    data_customers = data().customers_service().get_all()
    if data_customers is None:
        raise HTTPException(status_code=404, detail='customers not found')
    customers = []
    for customer in data_customers:
        customers.append(Customer.map(customer))
    return customers


@app.get("/customer/{id}")
async def say_hello(id: int):
    customer = data().customers_service().get_one(id)
    if customer is None:
        raise HTTPException(status_code=404, detail='customer not found')
    return Customer.map(customer)
