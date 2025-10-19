from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days
        
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            
            if congratulation_date.weekday() >= 5: 
                days_until_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_until_monday)
            
        
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

if __name__ == "__main__":
    users = [
        {"name": "Олег Христенко", "birthday": "1985.10.19"},
        {"name": "Віталій Smith", "birthday": "1990.10.20"},
        {"name": "Микола Johnson", "birthday": "1992.10.21"}, 
        {"name": "Вікторія Wilson", "birthday": "1988.10.15"}   
    ]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)