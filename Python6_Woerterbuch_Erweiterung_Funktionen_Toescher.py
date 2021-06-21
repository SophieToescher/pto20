# Erweiterung des WB-Beispiels um Funktionen
# Funktion für Suchen, Befehleingabe, Hinzufügen, Löschen und Beenden.
woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

def befehl():                        #Funktion für die Befehleingabe                              
    while True:                                     
        wahl = input("Was möchten Sie machen? [E]infügen, [L]öschen, [A]bfragen oder [B]eenden: ")
        if wahl.lower() == "e" or  wahl.lower() =="l" or wahl.lower() =="a" or wahl.lower() =="b":   # Kontrolle ob Eingabe möglich
            return wahl.lower()                                                                               
        else:
            print("Befehl leider nicht erkannt.") #Wenn falsche Eingabe
            
def sucheWort(Input): #Unterfunktion für die Suche eines Worts im WB
    index = 0
    for wort in woerterbuch_deutsch:   
        if Input.lower() == wort.lower():  
            break
        index +=1   
    
    if index == len(woerterbuch_deutsch):
        index = 0
        for wort in woerterbuch_english:          
            if Input.lower() == wort.lower():
                break
            index +=1    
        
        if index == len(woerterbuch_english):
            raise Exception("Das Wort steht nicht im Wörterbuch")    # Sonst -> Ausgabe "Das Wort steht nicht im Wörterbuch"  
    return (woerterbuch_deutsch[index], woerterbuch_english[index], index)

def einfuegen(de, en): # Funktion für das Einfügen von einem Wort auf DE und EN in das WB
    try:
        sucheWort(de) #Überprüft die deutsche Eingabe --> Ob bereits im WB
        print("Wort bereits gespeichert.") 
    except:
        woerterbuch_deutsch.append(de) #Eingegebener Begrgiff wird an die Liste angefügt
        woerterbuch_english.append(en) #Eingegebener Begrgiff wird an die Liste angefügt

def loeschen():  # Funktion zum Entfernen von begriffen
    try:
        entfernung = sucheWort(input("Begriff zum Löschen:"))
        woerterbuch_deutsch.remove(entfernung[0])                            
        woerterbuch_english.remove(entfernung[1])
    except Exception as e:                                               
        print(e) # Fehlermeldung wird ausgegeben
        

def abfragen(): #Übersetzen eines Wortes
    try:
        output = sucheWort(input("Gib einen deutschen oder englischen Begriff für ein Obst ein:"))             
        print(output[0] + "[DE]")                                        
        print(output[1]+ "[EN]")                                        
    except Exception as e:                                               
        print(e) # Fehlermeldung wird ausgegeben


while True:
    auswahl = befehl()                             
    if auswahl == "e": #Einfügen
        einfuegen(input("Deutscher Begriff:"), input("Englischer Begriff:"))
    elif auswahl == "l": #Löschen
        loeschen()
    elif auswahl == "b": #Beenden
        print("Vielen Dank für die Benutzung! Bis zum nächsten mal ;)")
        break   
    else:
        abfragen() #Abfragen -> Standardvorgang
        
    print("Das aktuelle Wörterbuch lautet:", woerterbuch_deutsch, woerterbuch_english) # Zur besseren Übersicht - Ausgabe der aktuellen Version des WB

