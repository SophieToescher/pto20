# Variante 1 - ohne try/except! Wird bei dieser Variante nicht benötigt da die
# print()-Funktion immer mit einer if-Bedingung geknüft ist und es somit zu keinem Key- bzw. ValueError kommen kann.

woerterbuch ={"Apfel" : "apple",
              "Birne" : "pear",
              "Kirsche" : "cherry",
              "Melone" : "melon",
              "Marille" : "apricot",
              "Pfirsich" : "peach"
              }
zaehler = 0
test = len(woerterbuch)

eingabe = input("Begriff: ")

for key, value in woerterbuch.items(): #Inhalt vom Wörterbuch wird nach der Reihe durchgegangen

    if value == eingabe: # Für die Übersetzung von Englisch auf Deutsch
        print ([key for key in woerterbuch][zaehler]) #Der Key an der Stelle "EINGABE = VALUE" wird ausgegeben
        break # Schleife beenden damit Zähler nicht erhöht wird

    elif key == eingabe: # Für die Übersetzung von Deutsch auf Englisch
        print ([value for key in woerterbuch][zaehler])  #Der Value an der Stelle "EINGABE = KEY" wird ausgegeben
        break

    zaehler+=1  #Zähler bestimmt den Index des Dictionaries
    
if zaehler == test:
    print ("Wort wurde nicht gefunden")
    