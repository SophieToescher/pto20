# Aufgabe 1:
# Programm dass,
# 1) den Benutzer begrüßt
# 2) Eine erste Zahl entgegen nimmt
# 3) Einen zweite Zahl eintgegen nimmt
# 4) Die Summe errechnet und ausgibt
# 5) Die Differenz der kleineren von der Größeren Zahl berechnen
# 6) Die Produkt errechnet und ausgibt
# 7) Die Quotient (kleinere Zahl durch größere Zahl)

print("Hallo BenutzerIn!")

Zahl_1 = float(input("Gib hier deine erste Zahl ein:"))
Zahl_2 = float(input("Gib hier deine zweite Zahl ein:"))

Summe = Zahl_1 + Zahl_2
print(Summe)

if Zahl_1 > Zahl_2:
    Differenz = Zahl_1 - Zahl_2
else:
    Differenz = Zahl_2 - Zahl_1
    
print(Differenz)

Produkt = Zahl_1 * Zahl_2
print(Produkt)

if Zahl_1 > Zahl_2:
    Quotient = Zahl_2 / Zahl_1
else:
    Quotient = Zahl_1 / Zahl_2

print(Quotient)

