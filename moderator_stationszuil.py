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

        #laat de moderator een bericht keuren, en deze wordt vervolgens weggescheven naar de database via een functie uit 'database.py'
            while True:
                keuring = input('is dit bericht goedgekeurd (y) of afgekeurd (n)?')
                if keuring == 'y' or keuring == 'n':
                    print('schrijven naar database\n')
                    datum_mod = datetime.datetime.now()
                    datum_mod = datum_mod.strftime(
                        '%Y-%m-%d %H:%M:%S')  # laat de datum en tijd alleen het jaar,maand,dag en uur,minuut,seconde invoeren
                    inserter(datum, bericht, station, naam, keuring, naammod, mailadres, datum_mod)
                        #verwijdert het beoordeelde item uit de lijst 'informatie'
                    informatie.remove(item)
                        #schrijft de regels opnieuw in het csv bestand
                    with open('bericht_info.csv', 'w') as f:
                        f.write('')
                        for item in informatie:
                            item += '\n'
                            #schrijft elk item in de lijst 'informatie' weg in het csv bestand
                            with open('bericht_info.csv', 'a') as file:
                                file.write(item)
                    break

                else:
                    #als er geen y of n in wordt gevoerd krijgt het een foutmelding en kan je het opnieuw invoeren
                    print('dit is geen juist antwoord. alleen de kleine letters y en n zijn toegestaan.')




