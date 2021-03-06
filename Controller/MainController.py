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


def get_customer(customer_short_name, factor_name):
    ini_db = ConnectionDB()
    fact_id = ini_db.get_factor_id(factor_name)
    customer = ini_db.get_customer_tree(customer_short_name, fact_id)
    return customer


def generate_protocol(lab, cust, fact, zamer, oformitel, measure, methodologies, date, date_izm):
    ini_db = ConnectionDB()
    fact_id = ini_db.get_factor_id(fact)
    laboratory = ini_db.get_lab(lab, (zamer,), (oformitel,), measure, methodologies, fact_id)
    customer = ini_db.get_customer(cust, fact_id)
    if customer.is_factor_fill and customer.is_meteo_fill:
        generate_protocol_func(laboratory, customer, date, date_izm, fact_id)
        return 0
    elif not customer.is_meteo_fill and not customer.is_factor_fill:
        return 1
    elif not customer.is_meteo_fill:
        return 2
    else:
        return 3


def add_laboratory_click(short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail):
    ini_db = ConnectionDB()
    ini_db.add_laboratory(short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail)


def add_customer_click(short_name, name, legal_address, actual_address, contract_number, contract_date):
    ini_db = ConnectionDB()
    ini_db.add_customer(short_name, name, legal_address, actual_address, contract_number, contract_date)


def add_department_click(dep_name, customer_name):
    ini_db = ConnectionDB()
    customer_id = ini_db.get_customer_id(customer_name)
    ini_db.add_department(dep_name, customer_id)


def add_workplace_click(wp_name, dep_id, is_noise, is_local_vibration, is_general_vibration):
    ini_db = ConnectionDB()
    ini_db.add_working_area(wp_name, dep_id, is_noise, is_local_vibration, is_general_vibration, False, False, False,
                            False, False, False, False)


def edit_department_click(dep_id, new_name):
    ini_db = ConnectionDB()
    ini_db.edit_department(dep_id, new_name)


def edit_workplace_click(workplace_id, name, is_noise, is_local_vibration, is_general_vibration):
    ini_db = ConnectionDB()
    ini_db.edit_working_area(workplace_id, name, is_noise, is_local_vibration, is_general_vibration)


def export_workplaces_click(file, short_name, factor=''):
    ini_db = ConnectionDB()
    ini_db.export_workplaces(short_name, factor, file)


def import_workplaces_click(file, factor=''):
    ini_db = ConnectionDB()
    ini_db.import_workplaces(file, factor)


def import_wp_click(file, short_name):
    ini_db = ConnectionDB()
    ini_db.import_csv_customer(file, short_name)

