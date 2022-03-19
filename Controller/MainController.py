def get_labs_list():
    return [1, 2, 3]


def get_customer_list(lab):
    if lab == '1':
        return ['a', 'b', 'c']
    elif lab == '2':
        return ['b', 'c', 'd']
    else:
        return ['c', 'd', 'e']


def get_factors_list(customer):
    if customer == 'a':
        return ['Вибрация общая', 'Шум', 'Вибрация локальная']
    elif customer == 'b':
        return ['Шум', 'Вибрация общая']
    else:
        return ['Вибрация общая', 'Шум']


def generate_protocol(lab, cust, fact, zamer, oformitel, measure, methodologies, date, date_izm):
    print(date, date_izm)
