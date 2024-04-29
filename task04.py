from datetime import datetime, timedelta

users = [{'name': 'Василь Підкова', 'birthday': '2000.02.12'},
         {'name': 'Наталія Борт', 'birthday': '1945.06.22'},
         {'name': 'Остап Вишня', 'birthday': '1999.04.29'},
         {'name': 'Алоізій Шкварка', 'birthday': '1987.05.21'},
         {'name': 'Алоізій Шкварка', 'birthday': '1987.05.02'},
         {'name': 'Алоізій Шкварка', 'birthday': '1987.05.21'},
         {'name': 'Алоізій Шкварка', 'birthday': '1987.05.21'}]

def get_upcoming_birthdays(users):
    today = datetime.today().date()

    result = []

    for user in users:
        # парсимо дату народження
        birth_date = datetime.strptime(user['birthday'], '%Y.%m.%d').date()

        # створюємо дану дня народження цього року
        birthday_this_year = datetime(year = today.year, month = birth_date.month, day = birth_date.day).date()

        # якщо день народження вже минув, беремо день народження у наступному році
        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, birth_date.month, birth_date.day).date()

        # знаходимо різницю сьогоднішньої дати та дати наступного дня народження
        left = birthday_this_year - today

        # Якщо припадає на найближчий тиждень
        if (left.days <= 7):
            week_no = birthday_this_year.weekday()
            
            # Якщо припадає на вихідні - переносимо на найближчий понеділок
            if week_no >= 5:
                birthday_this_year = birthday_this_year + timedelta(days = 6 - week_no)

            result.append({'name': user['name'], 'congratulation_date': birthday_this_year})

    return result
        

        