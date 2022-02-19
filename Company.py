from Laboratory import *
from Customer import *


class Company:
    def __init__(self):
        laboratories = []
        customers = []

    def add_laboratories(self, lab):
        self.laboratories[lab.name] = lab

    def add_customers(self, customer):
        self.customers[customer.name] = customer

    def get_protocol(self, lab, customer, date):
        self.laboratories[lab]
        self.customers[customer]
