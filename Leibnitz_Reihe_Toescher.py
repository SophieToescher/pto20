print("Hallo BenutzerIn! Mit diesem Programm kannst du die Zahl Pi näherungsweise berechnen.")
Anzahl = (int(input("Gib hier die Anzahl der Iterationen ein:")))

i = 0
Pi = 0
while i < Anzahl:
    Pi, i = Pi+((-1)**i)/(2*i+1), i +1
Final = Pi*4

print (Final)