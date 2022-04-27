from srs.data.context import ContextMonitoring
from srs.data.models.customers import Customers
from srs.models.customer import Customer


class CustomerStore:
    def __init__(self, context: ContextMonitoring):
        self.session = context.session_marker()

    def get_all(self):
        return self.session.query(Customers).all()

    def get_one(self, id_number: int):
        return self.session.query(Customers).where(Customers.id == id_number).first()
