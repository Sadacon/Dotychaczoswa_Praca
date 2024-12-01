def convert_time_to_decimal(hours, minutes=0):
    """
    Funkcja przelicza czas w godzinach i minutach na godziny dziesiętne.
    """
    return hours + (minutes / 60)

def calculate_average_speed(distance, time):
    """
    Funkcja oblicza średnią prędkość na podstawie dystansu i czasu.
    """
    if time <= 0:
        return "Czas musi być większy od zera!"
    avg_speed = distance / time
    return avg_speed

while True:
    try:
        # Pobieranie danych od użytkownika
        distance = float(input("Podaj dystans (w kilometrach): "))

        # Pobieranie czasu w godzinach i minutach
        hours = int(input("Podaj czas (godziny): "))
        minutes = int(input("Podaj czas (minuty): "))

        # Przeliczanie czasu na godziny dziesiętne
        time_in_hours = convert_time_to_decimal(hours, minutes)

        # Obliczanie średniej prędkości
        avg_speed = calculate_average_speed(distance, time_in_hours)
        if isinstance(avg_speed, str):
            print(avg_speed)
            continue

        # Wyświetlanie wyniku
        print(f"\nŚrednia prędkość: {avg_speed:.2f} km/h")

        # Opcja zakończenia
        again = input("\nCzy chcesz wykonać kolejne obliczenie? (tak/nie): ").strip().lower()
        if again != "tak":
            print("\nDziękuję za skorzystanie z programu!")
            break
    except ValueError:
        print("Proszę wprowadzić poprawne wartości
