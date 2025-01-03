from datetime import datetime
import pytz

# Wyświetlenie wszystkich dostępnych stref czasowych
print("Dostępne strefy czasowe:\n")
for timezone in pytz.all_timezones:
    print(timezone)

# Pobranie wyboru strefy czasowej od użytkownika
timezone_name = input("\nPodaj nazwę strefy czasowej z powyższej listy: ")

try:
    # Pobranie strefy czasowej
    timezone = pytz.timezone(timezone_name)

    # Pobranie aktualnego czasu w wybranej strefie czasowej
    current_time = datetime.now(timezone)

    # Wyświetlenie czasu
    print(f"\nAktualny czas w strefie {timezone_name}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
except pytz.UnknownTimeZoneError:
    print("\nNieznana nazwa strefy czasowej. Spróbuj ponownie.")
