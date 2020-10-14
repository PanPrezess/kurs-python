
psw = "haslo123"

print("\nWpisz hasło:\n")
inpt = input("> ")

if psw == "haslo":
    print("Hasło jest nieprawidłowe!")
    print("Podane hasło: " + str(inpt))
    inpt = input("> ")
elif psw != inpt:
    print("Jesteś blisko")
    inpt = input("> ")
else:
    print("Hasło prawidłowe!")
    inpt = input("> ")