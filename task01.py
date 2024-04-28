from datetime import datetime

def get_days_from_today(date):
    try:
        dt = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Невірний формат дати. Бажаємо успіху наступного разу.')

        return 'error'

    now = datetime.now()

    delta = now - dt

    return delta.days