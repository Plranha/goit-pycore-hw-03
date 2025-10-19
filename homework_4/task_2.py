import random

def get_numbers_ticket(min, max, quantity):

   
   if not (min >= 1 and max <= 1000 and min <= quantity <= max):
       return []
        
   unique_numbers = set()

   while len(unique_numbers) < quantity:
       number = random.randint(min,max)
       unique_numbers.add(number)

   return sorted(list(unique_numbers))


lottery_numbers = get_numbers_ticket(1,49,6)
print("Ваші лотерейні числа: ",lottery_numbers)

   
