import tkinter as tk

print("Program uruchomiony...")

root = tk.Tk()
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

print("Tkinter działa, oczekiwanie na wejście...")
root.mainloop()



def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def add_days_to_date(day, month, year, days_to_add):
    days_in_month = {
        1: 31,
        2: 29 if is_leap_year(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    day += days_to_add
    while day > days_in_month[month]:
        day -= days_in_month[month]
        month += 1
        if month > 12:
            month = 1
            year += 1
            days_in_month[2] = 29 if is_leap_year(year) else 28

    return day, month, year


def calculate_new_date():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        days_to_add = int(entry_days_to_add.get())

        new_day, new_month, new_year = add_days_to_date(day, month, year, days_to_add)
        result_label.config(text=f"Nowa data: {new_day:02d}-{new_month:02d}-{new_year}")
    except ValueError:
        messagebox.showerror("Błąd", "Upewnij się, że wszystkie pola są poprawnie wypełnione liczbami.")


# Tworzenie głównego okna
root = tk.Tk()
root.title("Dodawanie dni do daty")

# Etykiety i pola tekstowe
tk.Label(root, text="Dzień:").grid(row=0, column=0, padx=5, pady=5)
entry_day = tk.Entry(root)
entry_day.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Miesiąc:").grid(row=1, column=0, padx=5, pady=5)
entry_month = tk.Entry(root)
entry_month.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Rok:").grid(row=2, column=0, padx=5, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Dni do dodania:").grid(row=3, column=0, padx=5, pady=5)
entry_days_to_add = tk.Entry(root)
entry_days_to_add.grid(row=3, column=1, padx=5, pady=5)

# Przycisk obliczania
calculate_button = tk.Button(root, text="Oblicz", command=calculate_new_date)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Etykieta wyniku
result_label = tk.Label(root, text="Nowa data: ")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Uruchomienie pętli głównej
root.mainloop()
print("Program uruchomiony, czekam na wejście...")
