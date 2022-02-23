from Laboratory import *
from Customer import *


class Company:
    def __init__(self):
        self.labs = []
        self.cust = []
        self.laboratories = []
        self.customers = []

    def add_laboratories(self, lab):
        self.labs.append(lab.short_name)
        self.laboratories.append(lab)

    def add_customers(self, customer):
        self.cust.append(customer.short_name)
        self.customers.append(customer)

    def get_protocol(self, lab, customer, date):
        self.laboratories[lab]
        self.customers[customer]

    def get_labs_list(self):
        return self.labs

    def get_cust_list(self):
        return self.cust

