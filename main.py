
import task01
import task02
import task03
import task04

# Головне меню домашки для перевикористання
main_menu = '''1. Кількість днів від заданої дати
2. Випадкові числа для лотереї
3. Нормалізація телефонних номерів
4. Дні народження
5. Вихід'''

# Перший вивід головного меню
print(main_menu)

# Повторюємо виконання вічність, або поки користовач не попросить вийти
while True:
    action = input('Введіть номер завдання, що необхідно запустити або \'5\' для виходу: ')

    match action:
        case '1':
            # Користувач обрав перше завдання
            str_date = input('Введіть будь-яку дату у форматі РРРР-ММ-ДД: ')

            result = task01.get_days_from_today(str_date)

            if result != 'error':
                print(f'\nРізниця у днях між вказаною датою та сьогодні: {result}\n')
        case '2':
            # Користувач обрав друге завдання
            try:
                min = int(input('Введіть мінімальне число: '))
                max = int(input('Введіть максимальне число: '))
                qty = int(input('Введіть кількість чисел, що необхідно згенерувати: '))

                print('Числа для лотереї:')
                print(task02.get_numbers_ticket(min, max, qty))
            # Обробляємо помилку введення
            except ValueError:
                print('Це не число. Щасти наступного разу.')
        case '3':
            print('От з чим доводиться працювати: ', task03.raw_numbers)

            sanitized_numbers = [task03.normalize_phone(num) for num in task03.raw_numbers]

            print('Нормалізовані номери телефонів для SMS-розсилки: ', sanitized_numbers)
        case '4':
            congratulations = task04.get_upcoming_birthdays(task04.users)

            if len(congratulations) == 0:
                print('Нема кого вітати у наступні 7 днів')
            else:
                for congrats in congratulations:
                    print(f'{congrats['congratulation_date']} треба буде привітати {congrats['name']}')
        case '5':
            # Користувач обрав вихід. Перериваємо вічний цикл
            break
        case _:
            # Обробка помилкового введення
            print('Не вірно. Спробуйте ще')

    # Не виводитимо меню одразу, щоб користувачеві було зручно подивитися результати виконнання завдання
    input("Тисніть Enter щоб продовжити...")
    
    # Знову меню
    print(main_menu)