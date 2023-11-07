from database import inserter
import csv
import datetime
info = f''
informatie = []

        #vraagt de moderator om zijn "inloggegevens"
mailadres = input('wat is je mailadres?')
naammod = input('wat is je naam? ')

        #leest alle regels in het csv bestand en stopt ze in een lijst zodat ze later teruggestopt kunnen worden (zonder de beoordeelde items)
with open('bericht_info.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\n')
    for regel in reader:
        for stuk in regel:
            informatie.append(stuk)

        #opent het bestand nog een keer zodat de informatie er uit gelezen kan worden en kan worden verwerkt
with open('bericht_info.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\n')
    for line in reader:
        for item in line:
        #zorgt ervoor dat elke regel wordt gesorteerd op zijn kolom in de database
            items = item.split('; ')
            bericht = items[0]
            naam = items[1]
            station = items[2]
            datum = items[3]
            datum = datum.strip()
            print(item)






