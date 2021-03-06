import random
from Model.DB import ConnectionDB
from Model.Laboratory import *
from Model.Customer import *
import csv
import datetime



def lab_ini():
    ini_db = ConnectionDB()
    # print(ini_db.get_customer_factors("ООО «Василек»"))
    # print(ini_db.get_all_labs())
    # print(ini_db.get_all_customer())
    # lab = ini_db.get_lab('ЭКСПЕРТЭГИДА', (1,), (1,), (27, 28, 29), (31, 32, 33, 40))
    # customer = ini_db.get_customer("ООО «Василек»")
    # generate_protocol(lab, customer, '30.11.1988', '30.12.1988')

    # print(customer.get_hazard_wp())
    # print(customer.get_text('30.11.1988'))
    # print(lab.get_measure(0))
    # for measure in lab.methodologies:
    #     print(measure.name)
    # ini_db.export_workplaces("ООО «Василек»", 0)
    # ini_db.export_workplaces("ООО «Василек»", 1)
    # file = 'Vasilek.csv'
    # ini_db.import_workplaces(file, "ООО «Василек»")

    # file = 'Romashka2.csv'
    # ini_db.import_csv_customer(file, "ООО «Василек»")

    # short_name = "ООО «Василек»"
    # name = "Общество с ограниченной ответственностью «Василек» (ООО «Василек»)"
    # legal_address = "124154, г. Санкт-Петербург, пр-т. Невский, д. 1"
    # actual_address = "124154, г. Санкт-Петербург, пр-т. Невский, д. 1"
    # contract_number = "0000004-I"
    # contract_date = "18.12.2020"
    #
    # ini_db.add_customer(short_name, name, legal_address, actual_address, contract_number, contract_date)
    #





    # file = 'DIC_ND.csv'
    # with open(file, encoding='Windows-1251') as r_file:
    #     file_reader = csv.reader(r_file, delimiter=";")
    #     count = 0
    #     for row in file_reader:
    #         # print(row[1], row[2], row[3])
    #         if count != 0:
    #             ini_db.add_methodology(row[1], row[2], row[3])
    #         count += 1
    #     print(f'Всего в файле {count} строк.')


    # file = 'ATT_DEVICE.csv'
    # with open(file, encoding='Windows-1251') as r_file:
    #     file_reader = csv.reader(r_file, delimiter=";")
    #     count = 0
    #     for row in file_reader:
    #         if count != 0:
    #             ini_db.add_measuring(row[4], row[2], row[6], row[5], 1)
    #         count += 1
    #     print(f'Всего в файле {count} строк.')

    # ini_db.add_expert("Д.А. Шебаршов", "Инженер по специальной оценке условий труда", "0000")
    # ini_db.add_expert("К.С. Казакова", "Инженер по специальной оценке условий труда", "0001")

    # short_name = "ЭКСПЕРТЭГИДА"
    # name = "Общество с ограниченной ответственностью «ЦЕНТР ОХРАНЫ ТРУДА И ЭКОЛОГИИ «ЭКСПЕРТЭГИДА»\n" \
    #        "(ООО «ЭКСПЕРТЭГИДА»)"
    # name_lab = "Испытательная лаборатория ООО «ЦЕНТР ОХРАНЫ ТРУДА И ЭКОЛОГИИ «ЭКСПЕРТЭГИДА»"
    # logo = "C:/Users/buhu_/ITMO/11. Python/Зачетное задание/Эгида/logo.jpg"
    # director = "О.П. Гречкин"
    # address = "344011, Россия, Ростовская обл, Октябрьский р-н, г. Ростов-на-Дону, пр-кт Буденновский, д. 97, лит. А," \
    #           " Б, 2 этаж "
    # certificate_number = "RA.RU.21ЭГ03"
    # phone = "8 (863) 303-64-39"
    # e_mail = "info@expertegida.ru"
    # ini_db.add_laboratory(short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail)


#     lab1 = Laboratory(short_name, name, name_lab, logo, director, address, certificate_number, phone, e_mail)
#     lab1.add_expert("Д.А. Шебаршов", "Инженер по специальной оценке условий труда", "0000")
#     lab1.add_expert("К.С. Казакова", "Инженер по специальной оценке условий труда", "0001")
#     lab1.add_measuring("202515", "Анализатор шума и вибрации АССИСТЕНТ", "±0,3 дБ")
#     lab1.measuring[0].add_verification_certificate("С-ГЛР/27-09-2021/97809249", "27.09.2021", "26.09.2022")
#     lab1.add_measuring("9037", "Калибратор портативный АТ01m", "±2%")
#     lab1.measuring[1].add_verification_certificate("С-ДУИ/22-10-2021/103495751", "22.10.2021", "21.10.2022")
#     lab1.add_measuring("86613", "Измеритель параметров микроклимата «Метеоскоп-М»", "Температура воздуха: ± 0,2°С; "
#                                                                                     "Относительная влажность воздуха: "
#                                                                                     "± 3 "
#                                                                                     "%; Скорость движения воздуха: от "
#                                                                                     "0, "
#                                                                                     "1 до 1 м/с: ±(0.05+0.05V) м/с; "
#                                                                                     "от 1 "
#                                                                                     "до 20 м/с: ±(0,1+0,05V) м/с; "
#                                                                                     "Давление воздуха: ± 0,13 кПа")
#     lab1.measuring[2].add_verification_certificate("20061", "02.06.2020", "01.06.2022")
#     lab1.add_methodology("Измерение", "Руководство по эксплуатации БВЕК.438150-005РЭ. Анализатор шума и вибрации "
#                                       "Ассистент. (№ СИ в ГРСИ 39671-08)")
#     lab1.add_methodology("Оценка",
#                          "СанПиН 1.2.3685-21 «Гигиенические нормативы и требования к обеспечению безопасности и "
#                          "(или) безвредности для человека факторов среды обитания» (утверждены постановлением "
#                          "Главного государственного санитарного врача РФ от 28.01.2021 № 2) (зарегистрировано в "
#                          "Минюсте России 29 января 2021 года № 62296)")
#     return lab1
#
#
# def department_import(file, customer):
#     with open(file, encoding='utf-8') as r_file:
#         file_reader = csv.reader(r_file, delimiter=";")
#         count = 0
#         count_departments = -1
#         for row in file_reader:
#             if row[1] == "":
#                 customer.add_department(row[0])
#                 count_departments += 1
#             else:
#                 customer.departments[count_departments].add_working_area(row[0], row[1])
#             count += 1
#         print(f'Всего в файле {count} строк.')
#         print(f'В организации {count_departments} отделов.')
#
#
# def measure_ini(departments):
#     for department in departments:
#         for area in department.working_areas:
#             noise_source = "Производственное оборудование"
#             nature_of_noise = "Непостоянный широкополосный"
#             sound_lvl = random.randint(70, 90)
#             max_sound_lvl = random.randint(sound_lvl, sound_lvl + 10)
#             eq_sound_lvl = "-"
#             area.noise_parameter_ini(noise_source, nature_of_noise, sound_lvl, max_sound_lvl, eq_sound_lvl)
#             temperature = random.randint(210, 230)/10
#             atmo_pressure = random.randint(745, 749)
#             humidity = random.randint(40, 55)
#             area.weather_condition_ini(temperature, atmo_pressure, humidity)
#             # print(f'Уровень звука: {sound_lvl}; Максимальный уровень звука: {max_sound_lvl};')
#             # print(f'Температура воздуха: {temperature}; Атмосферное давление: {atmo_pressure}; '
#             #       f'Относительная влажность: {humidity}')
#
#
# def customer_ini():
#     short_name = "ООО «Ромашка»"
#     name = "Общество с ограниченной ответственностью «Ромашка» (ООО «Ромашка»)"
#     legal_address = "236022, Калининградская обл., г. Калининград, пр-т. Гвардейский, д. 15"
#     actual_address = "236022, Калининградская обл., г. Калининград, пр-т. Гвардейский, д. 15"
#     contract_number = "303522-VI"
#     contract_date = "15.11.2021"
#     customer1 = Customer(short_name, name, legal_address, actual_address, contract_number, contract_date)
#     file = "Romashka.csv"
#     department_import(file, customer1)
#     measure_ini(customer1.departments)
#     return customer1
