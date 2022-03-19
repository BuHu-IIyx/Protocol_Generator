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


def get_measure_list(factor):
    if factor == 'Шум':
        return ['Ассистент', 'Экофизика', 'Калибратор']
    elif factor == 'Вибрация локальная':
        return ['Ассистент', 'Экофизика', 'Виброкалибратор']
    elif factor == 'Вибрация общая':
        return ['Ассистент', 'Экофизика', 'Виброкалибратор']


def get_experts_list():
    return ['Вася', 'Петя', 'Маша', 'Саша']


def get_methodologies_list(factor):
    if factor == 'Шум':
        return ['1234214', '421412', '421412']
    elif factor == 'Вибрация локальная':
        return ['1111', '2222', '3333']
    elif factor == 'Вибрация общая':
        return ['444', '4444', '5555']


def generate_protocol(lab, cust, fact, zamer, oformitel, measure, methodologies, date, date_izm):
    print(date, date_izm)

