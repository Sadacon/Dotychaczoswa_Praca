from datetime import datetime

# Pobranie aktualnego czasu
current_time = datetime.now().time()

# Wyświetlenie aktualnego czasu
print("Aktualny czas:", current_time)
print("Godzina:", current_time.hour)
print("Minuta:", current_time.minute)
print("Sekunda:", current_time.second)
print("Mikrosekunda:", current_time.microsecond)
