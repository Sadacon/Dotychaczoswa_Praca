import os

try:
    os.mkdir('AutomatyzacjaTestów')  # Próba utworzenia katalogu
    print('inna instrukcja')
except FileExistsError:
    print('Nie można utworzyć katalogu o tej samej nazwie')
except BaseException:
    print('Nie udało się utworzyć katalogu')
else:
    print('Super, udało się...')  # Gdy żaden wyjątek nie został zgłoszony

 #pokazuje liste plików w systemie/katalogu
for file_name in os.listdir():
    print(f'Plik {file_name}')

#Tworzy katalogi 1 po drugim
os.makedirs('komputer/monitor/rezystor', exist_ok=True)#exist_ok=True \ niezgłasza wyjątku
# Funkcja chdir i getcwd
print(f'Gdzie ja jestem? {os.getcwd()}')
os.chdir('komputer')
print(f' Gdzie ja jestem? {os.getcwd()}')



