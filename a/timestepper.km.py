def calculate_time(distance, speed):
    """
    Funkcja oblicza czas na podstawie dystansu i prędkości.
    """
    if speed <= 0:
        return "Prędkość musi być większa od zera!"
    time = distance / speed
    return time


while True:
    try:
        # Pobieranie danych od użytkownika
        distance = float(input("Podaj dystans (w kilometrach): "))
        speed = float(input("Podaj prędkość (w km/h): "))

        # Obliczanie czasu
        result = calculate_time(distance, speed)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Czas przejazdu wynosi: {result:.2f} godziny")

        # Opcja zakończenia
        again = input("Czy chcesz wykonać kolejne obliczenie? (tak/nie): ").strip().lower()
        if again != "tak":
            print("Dziękuję za skorzystanie z programu!")
            break
    except ValueError:
        print("Proszę wprowadzić poprawne wartości liczbowe!")
