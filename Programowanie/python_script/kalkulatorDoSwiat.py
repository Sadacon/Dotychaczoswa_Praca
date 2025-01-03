import datetime


date = input('Podaj datę w formacie YYYY-MM-DD: ')
try:
    date = datetime.date.fromisoformat(date)
except ValueError:
    print('Niepoprawny format daty')
else:
    christmas_date = datetime.date(2024, 12, 24)
    days = (christmas_date - date).days
    print(f'Od {date} do świąt pozostało {days} dni')