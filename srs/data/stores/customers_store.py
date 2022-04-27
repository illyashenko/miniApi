from srs.data.context import ContextMonitoring
from srs.data.models.customers import Customers
from srs.models.customer import Customer


class CustomerStore:
    def __init__(self, context: ContextMonitoring):
        self.session = context.session

    def get_all(self):
        data_customers = self.session.query(Customers).all()
        customers = []
        for customer in data_customers:
            customers.append(Customer.map(customer))
        return customers
