woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

verwendung = bool(True) #bool für das gesamte Programm - wird beim beenden auf False gesetzt


while verwendung == bool(True): #Schleife für das gesamte Programm - kann nur durch beenden unterbrochen werden
    auswahl = input("Was möchten Sie machen? [E]infügen, [L]öschen, [A]bfragen oder [B]eenden: ")
    
    #Einfügen
    if auswahl == 'E'  or auswahl == 'e':
        anhang_de = input("Deutscher Begriff: ") 
        woerterbuch_deutsch.append(anhang_de) #Eingegebener Begrgiff wird an die Liste angefügt
        anhang_en = input("Englischer Begriff: ")
        woerterbuch_english.append(anhang_en) #Eingegebener Begrgiff wird an die Liste angefügt
        print("Danke - Dein Eintrag wurde gespeichert!")

    #Löschen   
    elif auswahl == 'L' or auswahl == 'l':
        print("Diese Wörter stehen zum Löschen zur Auswahl: ", woerterbuch_deutsch, woerterbuch_english)
        loeschen = (input("Begriff zum Löschen:"))
        i = (len(woerterbuch_deutsch)) #Vergleichsvariable, Anzahl der Begriffe im Wörterbuch
        j = 0 #Zählvariable wird auf 0 gesetzt
        while j < i:
            if woerterbuch_deutsch[j].lower() == loeschen.lower():      #für eine deutsche Eingabe
                index_english = woerterbuch_english[j] #Index in Variable speichern
                woerterbuch_deutsch.remove(woerterbuch_deutsch[j])
                woerterbuch_english.remove(index_english)
                print("Begriff wurde aus dem Wörterbuch entfernt")
                break
            elif woerterbuch_english[j].lower() == loeschen.lower():    #für eine englische Eingabe
                index_deutsch = woerterbuch_deutsch[j] #Index in Variable speichern
                woerterbuch_english.remove(woerterbuch_english[j])
                woerterbuch_deutsch.remove(index_deutsch)
                print("Begriff wurde aus dem Wörterbuch entfernt")
                break
            
            j=j+1 # Zählvariable wird um 1 erhöht und die Schleife erneut ausgeführt
        if j == i: #Wenn die Zählvariable gleich der Azahl der Begriffe ist, wird die Schleife beendet
            print("Wort befindet sich nicht im Wörterbuch") 

   
           
    #Beenden
    elif auswahl == 'B' or auswahl == 'b':
        print("Vielen Dank für die Benutzung! Bis zum nächsten mal ;)")
        verwendung = bool(False)

    #Abfrage -> Standardvorgang  
    else:
        suche = (str(input("Gib einen deutschen oder englischen Begriff für ein Obst ein:")))
        i = (len(woerterbuch_deutsch)) #Vergleichsvariable, Anzahl der Begriffe im Wörterbuch
        j = 0 #Zählvariable wird auf 0 gesetzt
        while j < i:
            if woerterbuch_deutsch[j].lower() == suche.lower():
                print(woerterbuch_english[j], "(EN)")
                break
            elif woerterbuch_english[j].lower() == suche.lower():
                print (woerterbuch_deutsch[j],"(DE)")
                break
            j=j+1
        if j == i: #Wenn die Zählvariable gleich der Azahl der Begriffe ist, wird die Schleife beendet
            print("Wort nicht gefunden")
    
