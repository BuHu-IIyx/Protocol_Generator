from Model.DB import ConnectionDB
from Model.Protocol import generate_protocol_func


def get_labs_list():
    ini_db = ConnectionDB()
    return ini_db.get_all_labs()


def get_customer_list():
    ini_db = ConnectionDB()
    return ini_db.get_all_customer()


def get_factors_list(customer):
    ini_db = ConnectionDB()
    return ini_db.get_customer_factors(customer)


def get_measure_list(factor):
    ini_db = ConnectionDB()
    return ini_db.get_measure_factor(factor)


def get_experts_list():
    ini_db = ConnectionDB()
    return ini_db.get_experts_list()


def get_methodologies_list(factor):
    ini_db = ConnectionDB()
    return ini_db.get_methodologies_factor(factor)


def generate_protocol(lab, cust, fact, zamer, oformitel, measure, methodologies, date, date_izm):
    ini_db = ConnectionDB()
    laboratory = ini_db.get_lab(lab, (zamer,), (oformitel,), (measure,), (methodologies,), fact)
    customer = ini_db.get_customer(cust)
    generate_protocol_func(laboratory, customer, date, date_izm)
