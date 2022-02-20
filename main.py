from testInit import *
from Protocol import *

lab = lab_ini()
customer = customer_ini()
print(customer.get_hazard_wp())

generate_protocol(lab, customer, "20 февраля 2022 г.", "14.02.2022 г.")

