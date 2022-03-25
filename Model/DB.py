import psycopg2
import csv


class ConnectionDB:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=LabDB user=postgres host=localhost password=452204 port=5432")
        self.cursor = self.conn.cursor()

    def add_laboratory(self, short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail):
        self.cursor.execute('INSERT INTO laboratory(short_name, name, name_laboratory, lab_logo, director, address, '
                            'certificate_number, phone, e_mail) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                            (short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail))
        self.conn.commit()

    def add_expert(self, name, position, certificate_number):
        self.cursor.execute('INSERT INTO experts(name, "position", certificate_number) VALUES(%s, %s, %s)',
                            (name, position, certificate_number))
        self.conn.commit()

    def add_measuring(self, factory_number, name, accurate, factor_id, laboratory_id):
        self.cursor.execute('INSERT INTO measuring(factory_number, measuring_name, accurate, factor_id, laboratory_id) '
                            'VALUES(%s, %s, %s, %s, %s)', (factory_number, name, accurate, factor_id, laboratory_id))
        self.conn.commit()

    def add_certificate(self, number, date_start, date_off, measure_id):
        self.cursor.execute('INSERT INTO verification_certificate(number, date_start, date_off, measure_id) '
                            'VALUES(%s, %s, %s, %s)', (number, date_start, date_off, measure_id))
        self.conn.commit()

    def add_methodology(self, name, application, factor_id):
        self.cursor.execute('INSERT INTO methodology(name, application, factor_id) '
                            'VALUES(%s, %s, %s)', (name, application, factor_id))
        self.conn.commit()

    def add_customer(self, short_name, name, legal_address, actual_address, contract_number, contract_date):
        self.cursor.execute('INSERT INTO customer(short_name, name, legal_address, actual_address, contract_number, '
                            'contract_date) VALUES(%s, %s, %s, %s, %s, %s)',
                            (short_name, name, legal_address, actual_address, contract_number, contract_date))
        self.conn.commit()

    def add_department(self, name, customer_id):
        self.cursor.execute('INSERT INTO customers_departments(name, customer_id) VALUES(%s, %s)', (name, customer_id))
        self.conn.commit()

    def add_working_area(self, name, department_id, is_noise, is_local_vibration, is_general_vibration, is_chemestry,
                         is_dust, is_infrasound, is_electromagnetic, is_microclimate, is_illumination, is_aeroion):
        self.cursor.execute('INSERT INTO department_working_area(name, department_id, is_noise, is_local_vibration, '
                            'is_general_vibration, is_chemestry, is_dust, is_infrasound, is_electromagnetic, '
                            'is_microclimate, is_illumination, is_aeroion) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, '
                            '%s, %s, %s)',
                            (name, department_id, is_noise, is_local_vibration, is_general_vibration, is_chemestry,
                             is_dust, is_infrasound, is_electromagnetic, is_microclimate, is_illumination, is_aeroion))
        self.conn.commit()

    def add_noise_params(self, working_area_id, noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl):
        self.cursor.execute('INSERT INTO noise_params(working_area_id, noise_source, nature_of_noise, sound_lvl, '
                            'max_sound_lvl, eq_sound_lvl) VALUES (%s, %s, %s, %s, %s, %s)',
                            (working_area_id, noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl))
        self.conn.commit()

    def add_weather_conditions(self, working_area_id, temperature, atmo_pressure, humidity):
        self.cursor.execute('INSERT INTO working_area_weather_condition(working_area_id, temperature, atmo_pressure, '
                            'humidity) VALUES (%s, %s, %s, %s)',
                            (working_area_id, temperature, atmo_pressure, humidity))
        self.conn.commit()

    def get_customer_id(self, short_name):
        self.cursor.execute('SELECT customer_id FROM customer WHERE short_name=%s', (short_name,))
        customer_id = self.cursor.fetchone()
        return customer_id[0]

    def get_department_id(self, customer_id, department_name):
        self.cursor.execute('SELECT department_id FROM customers_departments WHERE customer_id=%s AND name=%s',
                            (customer_id, department_name))
        department_id = self.cursor.fetchone()
        return department_id[0]

    def get_workplaces_in_customer(self, customer_id):
        self.cursor.execute('SELECT working_area_id, customers_departments.name, department_working_area.name '
                            'FROM department_working_area INNER JOIN customers_departments '
                            'ON department_working_area.department_id = customers_departments.department_id	'
                            'WHERE customers_departments.customer_id=%s AND department_working_area.is_noise=true',
                            (customer_id,))
        workplaces = self.cursor.fetchall()
        return workplaces

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

    def export_workplaces(self, short_name, factor):
        customer_id = self.get_customer_id(short_name)
        file = f'{short_name}.csv'
        with open(file, 'w', encoding='Windows-1251', newline='') as r_file:
            writer = csv.writer(r_file, delimiter=";")
            header = ()
            if factor == 1:
                header = ('working_area_id', 'department', 'working_area', 'noise_source', 'nature_of_noise',
                          'sound_lvl', 'max_sound_lvl', 'eq_sound_lvl', 'temperature', 'atmo_pressure', 'humidity')

            else:
                header = ('1', '2', '3', '4')

            writer.writerow(header)
            work_places = self.get_workplaces_in_customer(customer_id)
            writer.writerows(work_places)

    def import_workplaces(self, file, short_name):
        customer_id = self.get_customer_id(short_name)
        with open(file, encoding='Windows-1251') as r_file:
            file_reader = csv.reader(r_file, delimiter=";")
            count = 0
            for row in file_reader:
                if count != 0:
                    self.add_noise_params(row[0], row[3], row[4], row[5], row[6], row[7])
                    self.add_weather_conditions(row[0], float(row[8].replace(',', '.')), row[9], row[10])
                count += 1

    def __del__(self):
        self.conn.close()
