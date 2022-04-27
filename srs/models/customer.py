from srs.data.models.customers import Customers


class Customer:
    def __init__(self, first_name, last_name, age, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'name: {self.first_name}' \
               f', last name: {self.last_name}' \
               f', age: {self.age}' \
               f', phone: {self.phone}' \
               f', e-mail: {self.email}'

    @staticmethod
    def map(customer: Customers):
        return Customer(customer.firstname,
                        customer.lastname,
                        customer.age,
                        customer.email,
                        customer.phone)
