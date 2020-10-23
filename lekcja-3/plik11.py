from time import sleep

# Przykład użycia funkcji.

def wiadomosc():
    print("Dzień dobry!")
    inpt = input("> ")

def autor():
    print("Autor - Prezes")
    inpt = input("> ")

print("## MENU GŁÓWNE ##\n")
print("W - Zobacz wiadomość")
print("S - Autor Aplikacji")
print("D - Wyjdź")
inpt = input("> ")
if inpt == "w":
    wiadomosc()
elif inpt == "s":
    autor()
elif inpt == "d":
    print("Wychodzenie z aplikacji...")
    sleep(2)
else:
    print("Błąd!")
    sleep(3)