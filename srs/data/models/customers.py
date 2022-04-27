from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Customers(Base):
    __tablename__ = "Customers"

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    phone = Column(String)

    def __str__(self):
        return f'name: {self.firstname}' \
               f', last name: {self.lastname}' \
               f', age: {self.age}' \
               f', phone: {self.phone}' \
               f', e-mail: {self.email}'
