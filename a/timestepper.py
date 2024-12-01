def calculate_time(distance, speed):
    if speed == 0:
        return "Prędkość nie może wynosić 0!"
    time = distance / speed
    return time

# Wprowadzanie danych
try:
    a = float(input("Podaj dystans (w metrach): "))
    v = float(input("Podaj prędkość (w m/s): "))
    result = calculate_time(a, v)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Czas przejścia wynosi: {result:.2f} sekund")
except ValueError:
    print("Wprowadź prawidłowe liczby!")
