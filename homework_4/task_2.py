import random

def get_numbers_ticket(min, max, quantity):
    # Виправлена умова перевірки
    if not (min >= 1 and max <= 1000 and 1 <= quantity <= (max - min + 1)):
        return []
    
    unique_numbers = set()

    while len(unique_numbers) < quantity:
        number = random.randint(min, max)
        unique_numbers.add(number)

    return sorted(list(unique_numbers))

# Перевірка
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)