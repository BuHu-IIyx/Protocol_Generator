import psycopg2


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
        self.cursor.execute('INSERT INTO customers_departments(name, department_id, is_noise, is_local_vibration, '
                            'is_general_vibration, is_chemestry, is_dust, is_infrasound, is_electromagnetic, '
                            'is_microclimate, is_illumination, is_aeroion) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, '
                            '%s, %s, %s)',
                            (name, department_id, is_noise, is_local_vibration, is_general_vibration, is_chemestry,
                             is_dust, is_infrasound, is_electromagnetic, is_microclimate, is_illumination, is_aeroion))
        self.conn.commit()



    def __del__(self):
        self.conn.close()
