from testInit import *
from Protocol import *

lab = lab_ini()
customer = customer_ini()
print(customer.get_hazard_wp())
print(lab.get_all())

generate_protocol()

