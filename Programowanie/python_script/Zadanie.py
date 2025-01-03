import datetime



def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False



user_input = input("Podaj datę w formacie YYYY-MM-DD: ")

if is_valid_date(user_input):
    # Konwersja na obiekt daty
    input_date = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
    christmas_date = datetime.date(year=input_date.year, month=12, day=24)


    days_to_christmas = (christmas_date - input_date).days

    if days_to_christmas >= 0:
        print(f"Od {input_date} do świąt pozostało {days_to_christmas} dni.")
    else:
        print(f"Święta w roku {input_date.year} już minęły!")
else:
    print("Niepoprawny format daty")
