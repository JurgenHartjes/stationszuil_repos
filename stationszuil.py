import datetime
import random
current_datetime = datetime.datetime.now().date()


def random_station():   #kiest een random station uit een tekstbestand
    lst = []
    file = open('stations.txt')
    for line in file:
        lst.append(line)
        station = random.choice(lst).strip()
    return station


naam = input('mijn naam (laat leeg als je anoniem wil blijven): ') #vraagt naar de naam van de schrijver

if naam == '':      #vraagt naar een naam, als deze leeg blijft, moet wordt het bericht anoniem ingezonden
    naam = 'Anoniem'

while True:  # zorgt ervoor dat als het bericht langer is dan 140 tekens, er nog een keer wordt gevraagd naar het bericht
    bericht = input('Wat voor bericht wil je voor bericht opslaan? (Max 140 tekens) ')
    if len(bericht) <= 140:
        naam_info = f'Bericht opgeslagen door \'{naam}\''
        print(naam_info)
        station_info = f'Station in {random_station()}'
        print(station_info)
        save_time = datetime.datetime.now()
        save_time = save_time.strftime('%Y-%m-%d %H:%M:%S.%f')  #laat de datum en tijd alleen het jaar,maand,dag en uur,minuut,seconde en fractie invoeren
        save_time = save_time[:-7] #haalt 7 karakters van save_time af. hierdoor komen er geen fracties meer achter
        print(save_time)
        break
    elif len(bericht) > 140: #als er meer dan 140 karakters zijn wordt het aantal karakters genoemd, en mag de persoon het opnieuw invoeren
        print('Dit bericht heeft ' + str((len(bericht)-140)) + ' tekens te veel. Maximaal 140 tekens')

toevoegen = f'{bericht}; {naam}; {station_info}; {save_time}\n'
with open('bericht_info.csv', 'a') as f: #schrijft de benodigde info (toevoegen) in het .csv bestand
    f.write(toevoegen)





