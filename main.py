from testInit import *
from Protocol import *
from interface import *
from Company import *

lab = lab_ini()
customer = customer_ini()
company = Company()
company.add_laboratories(lab)
company.add_customers(customer)

# interface(company.get_labs_list(), company.get_cust_list(), ["sadas", "sdsad", "fdfd"], ["ewqrt", "ety", "dfd", "fd"],
#           ["dfdsfsd", "dfsdf", "gfg"])



generate_protocol(lab, customer, "20 февраля 2022 г.", "14.02.2022 г.")

