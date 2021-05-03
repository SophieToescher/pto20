#Ändern bzw. erweitern Sie das Wörterbuch-Bsp -> So ändern, dass man entweder einen englischen oder deutschen begriff eingeben kann. z.B.: Apple oder Apfel möglich


woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

vergleich = bool(False)
i = (len(woerterbuch_deutsch))
j = 0
suche = (str(input("Gib einen deutschen oder englischen Begriff für ein Obst ein:")))
while j < i:
    if woerterbuch_deutsch[j].lower() == suche.lower():
        print(woerterbuch_english[j], "(EN)")
        vergleich = bool(True)
        break
    elif woerterbuch_english[j].lower() == suche.lower():
        print (woerterbuch_deutsch[j],"(DE)")
        vergleich = bool(True)
        break
    j=j+1
if vergleich == bool(False):
    print("Wort nicht gefunden")
    
