#Variante 2 mittels try/except:
woerterbuch_deutsch ={"Apfel" : "apple",
              "Birne" : "pear",
              "Kirsche" : "cherry",
              "Melone" : "melon",
              "Marille" : "apricot",
              "Pfirsich" : "peach"
              }

                   
woerterbuch_englisch = {"apple" : "Apfel",
              "pear" : "Birne",
              "cherry" : "Kirsche",
              "melon" : "Melone",
              "apricot" : "Marille",
              "peach" : "Pfirich"
              }

               
try:
    eingabe = input("Begriff: ") 
    print(woerterbuch_deutsch[eingabe], "[en]") #Falls die Eingabe ein Key im deutschen WB ist wird der passende Value ausgegeben
except KeyError: 
    try:
        print(woerterbuch_englisch[eingabe], "[de]") #Falls die Eingabe ein Key im englischen WB ist wird der passende Value ausgegeben
    except KeyError:
        print("Wort existiert nicht") # Falls die Eingabe erneut zu einem KeyError führt
