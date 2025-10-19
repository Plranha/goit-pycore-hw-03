from datetime import datetime

def get_days_from_today(date):
 try:
    format_day = datetime.strptime(date,"%Y-%m-%d")
    current_day = datetime.today()

    days_diffrence = ( current_day - format_day).days

    return print(f"Різниця у днях:{days_diffrence}")
 except ValueError as e:
   print(f"Помилка: Некоректний формат дати '{date}', Очікуваний формат -> YYYY-MM-DD ")
   return None


date = "20-1010-18"
get_days_from_today(date)
