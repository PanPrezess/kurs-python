
psw = "haslo123"

print("\nWpisz hasło:\n") # \n to jest jakby kliknąć enter
inpt = input("> ")

if psw == "haslo": # jeżeli psw to hasło
    print("Hasło jest nieprawidłowe!")
    print("Podane hasło: " + str(inpt))
    inpt = input("> ")
elif psw != inpt: # Jeżeli psw to nie inpt
    print("Jesteś blisko")
    inpt = input("> ")
else: # w każdym innym razie
    print("Hasło prawidłowe!")
    inpt = input("> ")
