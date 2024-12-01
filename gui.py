import tkinter as tk

# Tworzenie głównego okna
root = tk.Tk()
root.title("Moje pierwsze GUI")

# Dodanie etykiety
label = tk.Label(root, text="Witaj w Tkinter!")
label.pack()

# Dodanie przycisku
button = tk.Button(root, text="Kliknij mnie", command=lambda: label.config(text="Kliknięto przycisk!"))
button.pack()

# Uruchomienie aplikacji
root.mainloop()
