import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    regex = r'\D'

    # Видалимо усе, окрім цифр
    only_digits = re.sub(regex, '', phone_number)

    # Тепер повернемо + та код країни, якщо потрібно
    if str.startswith(only_digits, '380'):
        return f'+{only_digits}'
    elif str.startswith(only_digits, '0'):
        return f'+38{only_digits}'
    else:
        return only_digits