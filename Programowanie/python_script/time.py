from datetime import time


t = time(hour=8, minute=30, second=20, microsecond=1)

print("czas:", t)
print("Godzina:", t.hour)
print("Minuta:", t.minute)
print("Sekunda:", t.second)
print("Mikrosekunda:", t.microsecond)

