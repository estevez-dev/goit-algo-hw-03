import random

def get_numbers_ticket(min, max, quantity):
    if min < 1:
        return set()
    
    if max > 1000:
        return set()
    
    if quantity < min or quantity > max:
        return set()
    
    numbers = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)