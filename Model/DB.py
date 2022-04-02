import psycopg2
import csv

from Model.Customer import Customer
from Model.Laboratory import Laboratory


class ConnectionDB:
    # Create connection
    def __init__(self):
        self.conn = psycopg2.connect("dbname=LabDB user=postgres host=localhost password=452204 port=5432")
        self.cursor = self.conn.cursor()

    # Add laboratory in DB
    def add_laboratory(self, short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail):
        self.cursor.execute('INSERT INTO laboratory(short_name, name, name_laboratory, lab_logo, director, address, '
                            'certificate_number, phone, e_mail) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                            (short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail))
        self.conn.commit()

    # Add expert in DB
    def add_expert(self, name, position, certificate_number):
        self.cursor.execute('INSERT INTO experts(name, "position", certificate_number) VALUES(%s, %s, %s)',
                            (name, position, certificate_number))
        self.conn.commit()

    # Add measuring equipment in DB
    def add_measuring(self, factory_number, name, accurate, factor_id, laboratory_id):
        self.cursor.execute('INSERT INTO measuring(factory_number, measuring_name, accurate, factor_id, laboratory_id) '
                            'VALUES(%s, %s, %s, %s, %s)', (factory_number, name, accurate, factor_id, laboratory_id))
        self.conn.commit()

    # Add certificate on measuring equipment in DB
    def add_certificate(self, number, date_start, date_off, measure_id):
        self.cursor.execute('INSERT INTO verification_certificate(number, date_start, date_off, measure_id) '
                            'VALUES(%s, %s, %s, %s)', (number, date_start, date_off, measure_id))
        self.conn.commit()

    # Add methodology off measurement in DB
    def add_methodology(self, name, application, factor_id):
        self.cursor.execute('INSERT INTO methodology(name, application, factor_id) '
                            'VALUES(%s, %s, %s)', (name, application, factor_id))
        self.conn.commit()

    # Add requisites of customer in DB
    def add_customer(self, short_name, name, legal_address, actual_address, contract_number, contract_date):
        self.cursor.execute('INSERT INTO customer(short_name, name, legal_address, actual_address, contract_number, '
                            'contract_date) VALUES(%s, %s, %s, %s, %s, %s)',
                            (short_name, name, legal_address, actual_address, contract_number, contract_date))
        self.conn.commit()

    # Add department of customer in DB
    def add_department(self, name, customer_id):
        self.cursor.execute('INSERT INTO customers_departments(name, customer_id) VALUES(%s, %s)', (name, customer_id))
        self.conn.commit()

    def edit_department(self, dep_id, new_name):
        self.cursor.execute('UPDATE customers_departments SET name=%s WHERE department_id=%s', (new_name, dep_id))
        self.conn.commit()

    # Add working area in DB
    def add_working_area(self, name, department_id, is_noise, is_local_vibration, is_general_vibration, is_chemestry,
                         is_dust, is_infrasound, is_electromagnetic, is_microclimate, is_illumination, is_aeroion):
        self.cursor.execute('INSERT INTO department_working_area(name, department_id, is_noise, is_local_vibration, '
                            'is_general_vibration, is_chemestry, is_dust, is_infrasound, is_electromagnetic, '
                            'is_microclimate, is_illumination, is_aeroion) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, '
                            '%s, %s, %s)',
                            (name, department_id, is_noise, is_local_vibration, is_general_vibration, is_chemestry,
                             is_dust, is_infrasound, is_electromagnetic, is_microclimate, is_illumination, is_aeroion))
        self.conn.commit()

    def edit_working_area(self, workplace_id, name, is_noise, is_local_vibration, is_general_vibration):
        self.cursor.execute('UPDATE department_working_area SET name=%s, is_noise=%s, is_local_vibration=%s, '
                            'is_general_vibration=%s WHERE working_area_id=%s',
                            (name, is_noise, is_local_vibration, is_general_vibration, workplace_id))
        self.conn.commit()

    # Add noise parameters in DB
    def add_noise_params(self, working_area_id, noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl):
        self.cursor.execute('INSERT INTO noise_params(working_area_id, noise_source, nature_of_noise, sound_lvl, '
                            'max_sound_lvl, eq_sound_lvl) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (working_area_id)'
                            ' DO UPDATE SET noise_source=%s, nature_of_noise=%s, sound_lvl=%s, max_sound_lvl=%s, '
                            'eq_sound_lvl=%s', (working_area_id, noise_source, nature_of_noise, sound_lvl,
                                                max_sound_lvl, eq_sound_lvl, noise_source, nature_of_noise, sound_lvl,
                                                max_sound_lvl, eq_sound_lvl))
        self.conn.commit()

    # Add weather conditions in DB
    def add_weather_conditions(self, working_area_id, temperature, atmo_pressure, humidity):
        self.cursor.execute('INSERT INTO working_area_weather_condition(working_area_id, temperature, atmo_pressure, '
                            'humidity) VALUES (%s, %s, %s, %s) ON CONFLICT (working_area_id) DO UPDATE SET '
                            'temperature=%s, atmo_pressure=%s, humidity=%s',
                            (working_area_id, temperature, atmo_pressure, humidity, temperature, atmo_pressure,
                             humidity))
        self.conn.commit()

    # Get customer ID from DB on name
    def get_customer_id(self, short_name):
        self.cursor.execute('SELECT customer_id FROM customer WHERE short_name=%s', (short_name,))
        customer_id = self.cursor.fetchone()
        return customer_id[0]

    # Get department ID from DB on name
    def get_department_id(self, customer_id, department_name):
        self.cursor.execute('SELECT department_id FROM customers_departments WHERE customer_id=%s AND name=%s',
                            (customer_id, department_name))
        department_id = self.cursor.fetchone()
        return department_id[0]

    # Get factor ID from DB on name
    def get_factor_id(self, factor):
        self.cursor.execute('SELECT factor_id FROM factor_dic WHERE factor = %s', (factor,))
        factor_id = self.cursor.fetchone()
        return factor_id[0]

    # Get all workplaces in customers departments
    def get_workplaces_in_customer(self, customer_id):
        self.cursor.execute('SELECT working_area_id, customers_departments.name, department_working_area.name '
                            'FROM department_working_area INNER JOIN customers_departments '
                            'ON department_working_area.department_id = customers_departments.department_id	'
                            'WHERE customers_departments.customer_id=%s AND department_working_area.is_noise=true',
                            (customer_id,))
        workplaces = self.cursor.fetchall()
        return workplaces

    # Import data from CSV file with departments and workplaces
    def import_csv_customer(self, file, short_name):
        customer_id = self.get_customer_id(short_name)
        with open(file, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            count = 0
            count_departments = -1
            department_id = 0
            for row in file_reader:
                if count != 0:
                    if row[1] == "":
                        self.add_department(row[0], customer_id)
                        department_id = self.get_department_id(customer_id, row[0])
                        count_departments += 1
                    else:
                        self.add_working_area(row[1], department_id, row[2], row[3], row[4], row[5], row[6], row[7],
                                              row[8],
                                              row[9], row[10], row[11])
                count += 1

    # Create CSV file with departments and workplaces for import data in fields
    def export_workplaces(self, short_name, factor):
        customer_id = self.get_customer_id(short_name)
        if factor == 0:
            header = ('working_area_id', 'department', 'working_area', 'temperature', 'atmo_pressure', 'humidity')
            short_name += '(meteo)'
        elif factor == 1:
            header = ('working_area_id', 'department', 'working_area', 'noise_source', 'nature_of_noise',
                      'sound_lvl', 'max_sound_lvl', 'eq_sound_lvl')
            short_name += '(noise)'
        else:
            header = ('1', '2', '3', '4')
            short_name += '(other)'
        file = f'{short_name}.csv'
        with open(file, 'w', encoding='Windows-1251', newline='') as r_file:
            writer = csv.writer(r_file, delimiter=";")
            writer.writerow(header)
            work_places = self.get_workplaces_in_customer(customer_id)
            writer.writerows(work_places)

    # Import noise parameters in DB
    def import_noise_params(self, file):
        with open(file, encoding='Windows-1251') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            count = 0
            for row in file_reader:
                if count != 0:
                    self.add_noise_params(row[0], row[3], row[4], row[5], row[6], row[7])
                count += 1

    # Import weather conditions in DB
    def import_weather_conditions(self, file):
        with open(file, encoding='Windows-1251') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            count = 0
            for row in file_reader:
                if count != 0:
                    self.add_weather_conditions(row[0], float(row[3].replace(',', '.')), row[4], row[5])
                count += 1

    # Laboratory fabric
    def get_lab(self, lab_short_name, experts_ids, zamer_ids, measure_ids, methodology_ids, fact):
        factor_id = self.get_factor_id(fact)
        self.cursor.execute('SELECT laboratory_id, short_name, name, name_laboratory, lab_logo, director, address, '
                            'certificate_number, phone, e_mail FROM laboratory WHERE short_name = %s',
                            (lab_short_name,))
        ini_data = self.cursor.fetchone()
        lab = Laboratory(ini_data[0], ini_data[1], ini_data[2], ini_data[3], ini_data[4], ini_data[5], ini_data[6],
                         ini_data[7], ini_data[8], ini_data[9])

        self.cursor.execute('SELECT name, "position", certificate_number FROM experts WHERE certificate_number IN %s',
                            (experts_ids,))
        exp_data = self.cursor.fetchall()
        for exp in exp_data:
            lab.add_expert(exp[0], exp[1], exp[2], 'expert')

        self.cursor.execute('SELECT name, "position", certificate_number FROM experts WHERE certificate_number IN %s',
                            (zamer_ids,))
        exp_data = self.cursor.fetchall()
        for exp in exp_data:
            lab.add_expert(exp[0], exp[1], exp[2], 'zamer')

        self.cursor.execute('SELECT factory_number, measuring_name, accurate, "number", date_start, '
                            'date_off FROM measuring INNER JOIN (SELECT DISTINCT ON (1) measure_id AS measure, '
                            '"number", date_start, date_off FROM verification_certificate ORDER BY 1, date_off desc) '
                            'AS cert ON measuring.measuring_id = measure WHERE measuring.factory_number IN %s AND '
                            'factor_id = %s',
                            (measure_ids, factor_id))
        measure_data = self.cursor.fetchall()
        for measure in measure_data:
            cert = dict(number=measure[3], date_start=measure[4], date_off=measure[5])
            lab.add_measuring(measure[0], measure[1], measure[2], cert)

        self.cursor.execute('SELECT application, name FROM methodology WHERE "ID" IN %s',
                            (methodology_ids,))
        meth_data = self.cursor.fetchall()
        for meth in meth_data:
            lab.add_methodology(meth[0], meth[1])

        return lab

    # Customer fabric
    def get_customer(self, customer_short_name):
        self.cursor.execute('SELECT customer_id, short_name, name, legal_address, actual_address, contract_number, '
                            'contract_date FROM customer WHERE short_name = %s',
                            (customer_short_name,))
        data = self.cursor.fetchone()
        customer = Customer(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        self.cursor.execute('SELECT department_id, name FROM customers_departments WHERE customer_id = %s',
                            (customer.customer_id, ))
        depts = self.cursor.fetchall()
        for dept in depts:
            customer.add_department(dept[0], dept[1])
            n = len(customer.departments) - 1
            self.cursor.execute('SELECT department_working_area.working_area_id, name, temperature, atmo_pressure, '
                                'humidity, noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl FROM '
                                'department_working_area LEFT JOIN working_area_weather_condition ON '
                                'department_working_area.working_area_id = '
                                'working_area_weather_condition.working_area_id LEFT JOIN noise_params ON '
                                'working_area_weather_condition.working_area_id = noise_params.working_area_id WHERE '
                                'department_working_area.department_id = %s AND is_noise = true',
                                (dept[0],))
            areas = self.cursor.fetchall()
            for area in areas:
                weather = dict(temperature=area[2], atmo_pressure=area[3], humidity=area[4])
                params = dict(noise_source=area[5], nature_of_noise=area[6], sound_lvl=area[7], max_sound_lvl=area[8],
                              eq_sound_lvl=area[9])
                if area[2] and area[5]:
                    if int(area[7]) > 80 or int(area[8]) > 110:
                        hazard = True
                    else:
                        hazard = False
                else:
                    hazard = False
                    weather = 0
                    params = 0
                customer.departments[n].add_working_area(area[0], area[1], hazard, weather, params)
        return customer

    # Interface data
    # Get laboratories list
    def get_all_labs(self):
        self.cursor.execute('SELECT short_name FROM laboratory')
        labs = self.cursor.fetchall()
        labs_name_list = []
        for lab in labs:
            if len(labs_name_list) == 0:
                labs_name_list = [lab[0]]
            else:
                labs_name_list.append(lab[0])
        return labs_name_list

    # Get customers list
    def get_all_customer(self):
        self.cursor.execute('SELECT short_name FROM customer')
        customers = self.cursor.fetchall()
        customers_name_list = []
        for cust in customers:
            if len(customers_name_list) == 0:
                customers_name_list = [cust[0]]
            else:
                customers_name_list.append(cust[0])
        return customers_name_list

    # Get factors from dictionary
    def get_all_factors(self):
        self.cursor.execute('SELECT factor_id, factor FROM factor_dic WHERE factor_id != 0')
        factors = self.cursor.fetchall()
        factors_name_list = dict()
        for fact in factors:
            factors_name_list[fact[0]] = fact[1]
        return factors_name_list

    # Get factors from customer
    def get_customer_factors(self, customer_name):
        self.cursor.execute('SELECT BOOL_OR(is_chemestry), ''false'', BOOL_OR(is_dust), BOOL_OR(is_noise), '
                            'BOOL_OR(is_infrasound), ''false'', BOOL_OR(is_general_vibration), '
                            'BOOL_OR(is_local_vibration), BOOL_OR(is_electromagnetic), ''false'', '
                            'BOOL_OR(is_microclimate), BOOL_OR(is_illumination), ''false'', ''false'', '
                            'BOOL_OR(is_aeroion) FROM department_working_area WHERE department_id IN (SELECT '
                            'department_id FROM customers_departments WHERE customer_id = '
                            '(SELECT customer_id FROM customer WHERE short_name = %s))',
                            (customer_name,))
        customer_fact = self.cursor.fetchone()
        all_fact = self.get_all_factors()
        result = []
        for i in range(0, 14):
            if customer_fact[i]:
                result.append(all_fact.get(i+1))
        return result

    # Get measure from DB on factor
    def get_measure_factor(self, factor):
        factor_id = self.get_factor_id(factor)
        self.cursor.execute('''SELECT factory_number || ': ' || measuring_name	FROM measuring WHERE factor_id = %s 
        ORDER BY measuring_name''', (factor_id,))
        measure = self.cursor.fetchall()
        result = []
        for m in measure:
            result.append(m[0])
        return result

    # Get methodologies from DB on factor
    def get_methodologies_factor(self, factor):
        factor_id = self.get_factor_id(factor)
        self.cursor.execute('''SELECT "ID" || ': ' || application || ' - ' || name	FROM methodology WHERE factor_id 
        IN (0, %s) ORDER BY application, factor_id''', (factor_id,))
        method = self.cursor.fetchall()
        result = []
        for m in method:
            result.append(m[0])
        return result

    # Get experts from DB
    def get_experts_list(self):
        self.cursor.execute('''SELECT certificate_number || ': ' || name FROM experts''')
        experts = self.cursor.fetchall()
        result = []
        for m in experts:
            result.append(m[0])
        return result

    # Close connection
    def __del__(self):
        self.conn.close()
