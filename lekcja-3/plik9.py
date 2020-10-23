
print("Wpisz swoją notatkę!")
inpt = input("> ")
nt = open("notatka.txt","w+") # tworzy plik
nt.write(inpt) # Dodaje do notatki inpt