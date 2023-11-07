import time
import tkinter
from tkinter import *
from time import *
import psycopg2
import threading
from datetime import datetime
import requests, json


def groningen():
    global stadsnaam
    global plaatjes
    global stationsnaam

    stadsnaam = 'Groningen'
    weerbericht()
    labelA = Label(master=root, text="Groningen ", height=1, bg='#FFEB3B', fg='#2D5EA9',
                   font=('Helvetica', 50, 'bold italic'))
    labelA.place(x=700, y=20)
    buttonU.destroy()
    buttonA.destroy()
    buttonG.destroy()

    img = PhotoImage(file='berichtenvak.png')
    img = img.subsample(1, 1)
    plaatjes.append(img)
    label = Label(master=root, image=img, borderwidth=0)
    label.place(x=0, rely=0.64)

    imgweer = PhotoImage(file='berichtenvak.png')
    imgweer = imgweer.zoom(5, 1)
    plaatjes.append(imgweer)
    labelw = Label(master=root, image=imgweer, borderwidth=0)
    labelw.place(x=540, rely=0.64)

    label = Label(master=root, text="berichten van NS gebruikers: ", height=1, bg='#2D5EA9', fg='#F7F7F7',
                  font=('Helvetica', 16, 'bold italic'))
    label.place(relx=0.05, rely=0.64)

    labelfaci = Label(master=root, text=f"aanwezige faciliteiten in {stadsnaam}: ", height=1, bg='#2D5EA9', fg='#F7F7F7',
                      font=('Helvetica', 16, 'bold italic'))
    labelfaci.place(x=640, rely=0.64)

    thread1 = threading.Thread(target=looping)
    thread1.start()

    thread2 = threading.Thread(target=starttijd)
    thread2.start()

    faciliteiten = haalfaciliteiten()
    ovbike = faciliteiten[1][1]
    elevator = faciliteiten[1][2]
    toilet = faciliteiten[1][3]
    park_and_ride = faciliteiten[1][4]



    if ovbike == True:
        ovbikep = PhotoImage(file='img_ovfiets.png')
        ovbikep = ovbikep.zoom(1, 1)
        plaatjes.append(ovbikep)
        labelbik = Label(master=root, image=ovbikep, borderwidth=0)
        labelbik.place(x=850, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=890, rely=0.88)

    elif ovbike == False:
        ovbikep = PhotoImage(file='img_ovfiets.png')
        ovbikep = ovbikep.zoom(1, 1)
        plaatjes.append(ovbikep)
        labelbik = Label(master=root, image=ovbikep, borderwidth=0)
        labelbik.place(x=850, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=890, rely=0.88)

    if elevator == True:
        elevatorp = PhotoImage(file='img_lift.png')
        elevatorp = elevatorp.zoom(1, 1)
        plaatjes.append(elevatorp)
        labelele = Label(master=root, image=elevatorp, borderwidth=0)
        labelele.place(x=1050, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1090, rely=0.88)
    elif elevator == False:
        elevatorp = PhotoImage(file='img_lift.png')
        elevatorp = elevatorp.zoom(1, 1)
        plaatjes.append(elevatorp)
        labelele = Label(master=root, image=elevatorp, borderwidth=0)
        labelele.place(x=1050, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1090, rely=0.88)

    if toilet == True:
        toiletp = PhotoImage(file='img_toilet.png')
        toiletp = toiletp.zoom(1, 1)
        plaatjes.append(toiletp)
        labelto = Label(master=root, image=toiletp, borderwidth=0)
        labelto.place(x=1250, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1290, rely=0.88)
    elif toilet == False:
        toiletp = PhotoImage(file='img_toilet.png')
        toiletp = toiletp.zoom(1, 1)
        plaatjes.append(toiletp)
        labelto = Label(master=root, image=toiletp, borderwidth=0)
        labelto.place(x=1250, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1290, rely=0.88)

    if park_and_ride == True:
        penrp = PhotoImage(file='img_pr.png')
        penrp = penrp.zoom(1, 1)
        plaatjes.append(penrp)
        labelpr = Label(master=root, image=penrp, borderwidth=0)
        labelpr.place(x=650, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=690, rely=0.88)
    elif park_and_ride == False:
        penrp = PhotoImage(file='img_pr.png')
        penrp = penrp.zoom(1, 1)
        plaatjes.append(penrp)
        labelpr = Label(master=root, image=penrp, borderwidth=0)
        labelpr.place(x=650, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=690, rely=0.88)


def utrecht():
    global stadsnaam
    global plaatjes
    global stationsnaam

    stadsnaam = 'Utrecht'
    weerbericht()
    labelA = Label(master=root, text="Utrecht ", height=1, bg='#FFEB3B', fg='#2D5EA9',
                   font=('Helvetica', 50, 'bold italic'))
    labelA.place(x=700, y=20)
    buttonU.destroy()
    buttonA.destroy()
    buttonG.destroy()

    img = PhotoImage(file='berichtenvak.png')
    img = img.subsample(1, 1)
    plaatjes.append(img)
    label = Label(master=root, image=img, borderwidth=0)
    label.place(x=0, rely=0.64)

    imgweer = PhotoImage(file='berichtenvak.png')
    imgweer = imgweer.zoom(5, 1)
    plaatjes.append(imgweer)
    labelw = Label(master=root, image=imgweer, borderwidth=0)
    labelw.place(x=540, rely=0.64)

    label = Label(master=root, text="berichten van NS gebruikers: ", height=1, bg='#2D5EA9', fg='#F7F7F7',
                  font=('Helvetica', 16, 'bold italic'))
    label.place(relx=0.05, rely=0.64)

    labelfaci = Label(master=root, text=f"aanwezige faciliteiten in {stadsnaam}: ", height=1, bg='#2D5EA9', fg='#F7F7F7',
                      font=('Helvetica', 16, 'bold italic'))
    labelfaci.place(x=640, rely=0.64)

    thread1 = threading.Thread(target=looping)
    thread1.start()

    thread2 = threading.Thread(target=starttijd)
    thread2.start()

    faciliteiten = haalfaciliteiten()
    ovbike = faciliteiten[2][1]
    elevator = faciliteiten[2][2]
    toilet = faciliteiten[2][3]
    park_and_ride = faciliteiten[2][4]

    if ovbike == True:
        ovbikep = PhotoImage(file='img_ovfiets.png')
        ovbikep = ovbikep.zoom(1, 1)
        plaatjes.append(ovbikep)
        labelbik = Label(master=root, image=ovbikep, borderwidth=0)
        labelbik.place(x=850, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=890, rely=0.88)

    elif ovbike == False:
        ovbikep = PhotoImage(file='img_ovfiets.png')
        ovbikep = ovbikep.zoom(1, 1)
        plaatjes.append(ovbikep)
        labelbik = Label(master=root, image=ovbikep, borderwidth=0)
        labelbik.place(x=850, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=890, rely=0.88)

    if elevator == True:
        elevatorp = PhotoImage(file='img_lift.png')
        elevatorp = elevatorp.zoom(1, 1)
        plaatjes.append(elevatorp)
        labelele = Label(master=root, image=elevatorp, borderwidth=0)
        labelele.place(x=1050, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1090, rely=0.88)
    elif elevator == False:
        elevatorp = PhotoImage(file='img_lift.png')
        elevatorp = elevatorp.zoom(1, 1)
        plaatjes.append(elevatorp)
        labelele = Label(master=root, image=elevatorp, borderwidth=0)
        labelele.place(x=1050, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1090, rely=0.88)

    if toilet == True:
        toiletp = PhotoImage(file='img_toilet.png')
        toiletp = toiletp.zoom(1, 1)
        plaatjes.append(toiletp)
        labelto = Label(master=root, image=toiletp, borderwidth=0)
        labelto.place(x=1250, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1290, rely=0.88)
    elif toilet == False:
        toiletp = PhotoImage(file='img_toilet.png')
        toiletp = toiletp.zoom(1, 1)
        plaatjes.append(toiletp)
        labelto = Label(master=root, image=toiletp, borderwidth=0)
        labelto.place(x=1250, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1290, rely=0.88)

    if park_and_ride == True:
        penrp = PhotoImage(file='img_pr.png')
        penrp = penrp.zoom(1, 1)
        plaatjes.append(penrp)
        labelpr = Label(master=root, image=penrp, borderwidth=0)
        labelpr.place(x=650, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=690, rely=0.88)
    elif park_and_ride == False:
        penrp = PhotoImage(file='img_pr.png')
        penrp = penrp.zoom(1, 1)
        plaatjes.append(penrp)
        labelpr = Label(master=root, image=penrp, borderwidth=0)
        labelpr.place(x=650, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=690, rely=0.88)

plaatjes = []
def amsterdam():
    global stadsnaam
    global plaatjes
    global stationsnaam

    stadsnaam = 'Amsterdam'
    weerbericht()
    labelA = Label(master=root, text="Amsterdam ", height=1, bg='#FFEB3B', fg='#2D5EA9',
                  font=('Helvetica', 50, 'bold italic'))
    labelA.place(x=700, y = 20)
    buttonU.destroy()
    buttonA.destroy()
    buttonG.destroy()


    img = PhotoImage(file='berichtenvak.png')
    img = img.subsample(1, 1)
    plaatjes.append(img)
    label = Label(master=root, image=img, borderwidth=0)
    label.place(x=0, rely=0.64)

    imgweer = PhotoImage(file='berichtenvak.png')
    imgweer = imgweer.zoom(5, 1)
    plaatjes.append(imgweer)
    labelw = Label(master=root, image=imgweer, borderwidth=0)
    labelw.place(x=540, rely=0.64)

    label = Label(master=root, text="berichten van NS gebruikers: ", height=1, bg='#2D5EA9', fg='#F7F7F7',
                  font=('Helvetica', 16, 'bold italic'))
    label.place(relx=0.05, rely=0.64)

    labelfaci = Label(master=root, text=f"aanwezige faciliteiten in {stadsnaam}: ", height=1, bg='#2D5EA9', fg='#F7F7F7',
                  font=('Helvetica', 16, 'bold italic'))
    labelfaci.place(x=640, rely=0.64)

    thread1 = threading.Thread(target=looping)
    thread1.start()

    thread2 = threading.Thread(target=starttijd)
    thread2.start()

    faciliteiten = haalfaciliteiten()
    ovbike = faciliteiten[0][1]
    elevator = faciliteiten[0][2]
    toilet = faciliteiten[0][3]
    park_and_ride = faciliteiten[0][4]



    if ovbike == True:
        ovbikep = PhotoImage(file='img_ovfiets.png')
        ovbikep = ovbikep.zoom(1, 1)
        plaatjes.append(ovbikep)
        labelbik = Label(master=root, image=ovbikep, borderwidth=0)
        labelbik.place(x=850, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=890, rely=0.88)

    elif ovbike == False:
        ovbikep = PhotoImage(file='img_ovfiets.png')
        ovbikep = ovbikep.zoom(1, 1)
        plaatjes.append(ovbikep)
        labelbik = Label(master=root, image=ovbikep, borderwidth=0)
        labelbik.place(x=850, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=890, rely=0.88)



    if elevator == True:
        elevatorp = PhotoImage(file='img_lift.png')
        elevatorp = elevatorp.zoom(1, 1)
        plaatjes.append(elevatorp)
        labelele = Label(master=root, image=elevatorp, borderwidth=0)
        labelele.place(x=1050, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1090, rely=0.88)
    elif elevator == False:
        elevatorp = PhotoImage(file='img_lift.png')
        elevatorp = elevatorp.zoom(1, 1)
        plaatjes.append(elevatorp)
        labelele = Label(master=root, image=elevatorp, borderwidth=0)
        labelele.place(x=1050, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1090, rely=0.88)

    if toilet == True:
        toiletp = PhotoImage(file='img_toilet.png')
        toiletp = toiletp.zoom(1, 1)
        plaatjes.append(toiletp)
        labelto = Label(master=root, image=toiletp, borderwidth=0)
        labelto.place(x=1250, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1290, rely=0.88)
    elif toilet == False:
        toiletp = PhotoImage(file='img_toilet.png')
        toiletp = toiletp.zoom(1, 1)
        plaatjes.append(toiletp)
        labelto = Label(master=root, image=toiletp, borderwidth=0)
        labelto.place(x=1250, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=1290, rely=0.88)

    if park_and_ride == True:
        penrp = PhotoImage(file='img_pr.png')
        penrp = penrp.zoom(1, 1)
        plaatjes.append(penrp)
        labelpr = Label(master=root, image=penrp, borderwidth=0)
        labelpr.place(x=650, rely=0.75)

        kruisp = PhotoImage(file='vinkje.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=690, rely=0.88)
    elif park_and_ride == False:
        penrp = PhotoImage(file='img_pr.png')
        penrp = penrp.zoom(1, 1)
        plaatjes.append(penrp)
        labelpr = Label(master=root, image=penrp, borderwidth=0)
        labelpr.place(x=650, rely=0.75)

        kruisp = PhotoImage(file='kruis.png')
        kruisp = kruisp.subsample(10, 10)
        plaatjes.append(kruisp)
        kruisl = Label(master=root, image=kruisp, borderwidth=0)
        kruisl.place(x=690, rely=0.88)


def haalfaciliteiten():
    connection_string = "host = '20.254.113.210' dbname = 'stationszuil' user = 'postgres' password = 'fj6YDB5D'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    query = "Select station_city, ov_bike, elevator, toilet, park_and_ride From public.station_service where station_city = 'Amsterdam' or station_city = 'Utrecht' or station_city = 'Groningen'"
    cursor.execute(query)
    service = cursor.fetchall()  #verbindt met de database en kijkt in de tabel of de service's aanwezig zijn of niet
    conn.close()
    return service
def haaltext():
    #verbindt met de database haalt de benodigde informatie uit de tabel
    connection_string = "host = '20.254.113.210' dbname = 'stationszuil' user = 'postgres' password = 'fj6YDB5D'"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    query = "Select bericht, naam, datums, station From public.berichten where keuring = 'y' order by datums desc Limit 5"
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records


def starttijd():
    while True: #laat de volgende code opnieuw runnen tot het 'break'commando wordt bereikt (wat nooit gebeurt)
        nu = datetime.now()
        tijd = nu.strftime('%H:%M:%S')  #stelt de tijd in om alleen de uren, minuten en seconden te laten zien
        klokje = Label(master = root, font = ('Helvetica', 35,  'bold italic'), text=tijd, bg = '#FFEB3B', fg = '#2D5EA9')   #zet de digitale klok als tekst in het tk venster
        klokje.place(x= 35,y= 35)
        sleep(1) #laat de code een seconde wachten voordat het verder gaat


def looping():

    allerows = haaltext()
    i = 0
    while i <= 4: #laat de volgende code opnieuw runnen tot het 'break'commando wordt bereikt (wat nooit gebeurt)
        berichtregel = allerows[i]  #pakt het bericht met index i
        textlabel = berichtregel[0].strip()
        berichttekst = Label(master=root, text=textlabel, height=1, bg='#F7F7F7', fg='#000000',
                      font=('Helvetica', 18, 'bold italic')) #laat het bericht zien
        berichttekst.place(relx=0.05, rely=0.75)
        berichtnr = f'bericht {i+1} van de 5'
        berichtnummer = Label(master=root, text=berichtnr, height=1, bg='#F7F7F7', fg='#000000',
                      font=('Helvetica', 10, 'bold italic')) # laat het berichtnr zien
        berichtnummer.place(x=400, rely=0.7)
        berichtnaam = berichtregel[1].strip()

        berichtnamen = Label(master=root, text=f'bericht van {berichtnaam}', height=1, bg='#F7F7F7', fg='#000000',
                      font=('Helvetica', 10, 'bold italic')) #laat de schrijver van het bericht zien
        berichtnamen.place(x = 30, rely=0.7)
        stationsnaam = berichtregel[3].strip()

        stationsnamen = Label(master=root, text=f'van het station in {stationsnaam}', height=1, bg='#F7F7F7', fg='#000000',
                      font=('Helvetica', 10, 'bold italic')) #laat de schrijver van het bericht zien
        stationsnamen.place(x = 30, rely=0.72)
        sleep(8) #laat de code 8 seconden wachten tot het verder gaat
        berichttekst.destroy() #haalt het bericht weg zodat het vervangen wordt door de volgende ipv het er bovenop zetten
        berichtnummer.destroy()
        berichtnamen.destroy()
        stationsnamen.destroy()

        if i == 4:  #als i=4 is het 5e bericht gepresenteerd, dus moet het weer de eerste laten zien (i=0)
            i = 0
        else:
            i += 1 #telt 1 bij i op, zodat bij de volgende herhaling het volgende bericht wordt laten zien


def weerbericht():

    api_key = "5971236f1a5eabca19f2e65db8c05dc9"
    global stadsnaam #haalt de gekozen stad op om daarvan het weer op te vragen
    url = f'http://api.openweathermap.org/data/2.5/weather?q={stadsnaam}&appid={api_key}'
    response = requests.get(url)
    weerinfo = response.json() #in weerinfo staat alle informatie over het weer


    imgweer = PhotoImage(file='wolk.png')
    imgweer = imgweer.zoom(3, 6)
    imgweer = imgweer.subsample(2,5)
    labelweer = Label(master=root, image=imgweer, borderwidth=0)
    plaatjes.append(imgweer)
    labelweer.place(x=540, y=150)





    if weerinfo['cod'] == 200:
        kelvin = 273
        temperatuur = int(weerinfo['main']['temp'] - kelvin)        #temperatuur
        vochtigheid = int(weerinfo['clouds']['all'])        #luchtvochtigheid
        wolken= str(weerinfo['weather'][0]['description'])      #bijv. 'bewolkt' of 'mistig'
        wolkenicon = str(weerinfo['weather'][0]['icon'])    #geeft de code van het te gebruiken wolken plaatje
        print(wolkenicon)
        if wolken == 'broken clouds':       #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='04d@2x.png')
                imgweer = imgweer.zoom(2, 2)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='04d@2x.png')
                imgweer = imgweer.zoom(2, 2)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'overcast clouds':       #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='04d@2x.png')
                imgweer = imgweer.zoom(2, 2)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='04d@2x.png')
                imgweer = imgweer.zoom(2, 2)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'clear sky':       #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='01d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='01n@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'few clouds':      #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='02d@2x.png')
                imgweer = imgweer.zoom(3, 3)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='02n@2x.png')
                imgweer = imgweer.zoom(3, 3)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'scattered clouds':        #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='03n@2x.png')
                imgweer = imgweer.zoom(3, 3)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='03n@2x.png')
                imgweer = imgweer.zoom(3, 3)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'shower rain':     #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='09d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='09d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'rain':        #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='10d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='10n@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'thunderstorm':        #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='11d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='11d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'snow':        #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='13d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='13d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'mist':        #zorgt ervoor dat het correcte plaatje van het weer vertoont wordt
            if 'd' in wolkenicon:
                imgweer = PhotoImage(file='50d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
            if 'n' in wolkenicon:
                imgweer = PhotoImage(file='50d@2x.png')
                imgweer = imgweer.zoom(1, 1)
                labelweer = Label(master=root, image=imgweer, borderwidth=0)
                plaatjes.append(imgweer)
                labelweer.place(x=770, y=330)
        if wolken == 'clear sky':
            wolken = 'helder'
        if wolken == 'rain':
            wolken = 'aan het regenen'      #zorgt ervoor dat het tekst balkje in het nederlands vertoont wordt
        if wolken == 'few clouds':
            wolken = 'licht bewolkt'
        if wolken == 'scattered clouds':
            wolken = 'bewolkt'
        if wolken == 'broken clouds':
            wolken = 'dicht bewolkt'
        if wolken == 'shower rain':
            wolken = 'aan het gieten'
        if wolken == 'thunderstorm':
            wolken = 'aan het stormen'
        if wolken == 'snow':
            wolken = 'aan het sneeuwen'
        if wolken == 'mist':
            wolken = 'mistig'

        labelA = Label(master=root, text=f"het is nu {wolken} ", height=1, bg='#FFFFFF', fg='#2D5EA9',
                       font=('Helvetica', 15, 'bold italic'))
        labelA.place(x=1050, y=350)

        labelA = Label(master=root, text=f"luchtvochtigheid:   {vochtigheid}% ", height=1, bg='#FFFFFF', fg='#2D5EA9',
                       font=('Helvetica', 15, 'bold italic'))
        labelA.place(x=1050, y=390)

        labelA = Label(master=root, text=f"temperatuur:   {temperatuur}°C", height=1, bg='#FFFFFF', fg='#2D5EA9',
                       font=('Helvetica', 15, 'bold italic'))
        labelA.place(x=1050, y=430)





root = Tk() #opent een scherm
root.title('stationsscherm') #naam van het venster heet 'stationsscherm
root.configure(bg= '#FFEB3B') #de volledige achtergrond is een geelige kleur
frame = Frame(root)
frame.pack()
root.geometry('1900x1000') #formaat van het venster wanneer deze wordt geopend

buttonA = Button(master = root,text = 'Amsterdam', font= ('Helvetica', 16, 'bold italic'), command=amsterdam, bg = '#2D5EA9', fg = '#F7F7F7')
buttonA.config(width=30, height= 5)
buttonA.place(x=480, y=350)     #laat een knop 'Amsterdam' zien en wanner er op wordt geklikt komt het scherm met de informatie van Amsterdam te staan

img1 = PhotoImage(file='NSlogo.png')    #pakt de blauwe balk die is gemaakt in paint
img1 = img1.subsample(3, 3)  #verkleind de afbeelding 3x
label = Label(master=root, image=img1, borderwidth=0)
label.place(relx= 0.9, y = 15)


blauwbalk = PhotoImage(file='blauwe balk.png') #pakt de blauwe balk die is gemaakt in paint
blauwbalk = blauwbalk.subsample(1, 3) #verkleind de afbeelding 3x op de ywaarde
blauwbalk = blauwbalk.zoom(5,1) #vergroot de afbeelding 5x op de xwaarde
blauwlabel = Label(master=root, image=blauwbalk, borderwidth=0)
blauwlabel.place(x=0, y=120)

thread2 = threading.Thread(target=starttijd)
thread2.start()     #zorgt ervoor dat de functie starttijd() runt terwijl de rest van de code blijft lopen



buttonG = Button(master = root,text = 'Groningen', font= ('Helvetica', 16, 'bold italic'), command=groningen, bg = '#2D5EA9', fg = '#F7F7F7')
buttonG.config(width=30, height= 5)
buttonG.place(x=700, y=500)     #laat een knop 'Groningen' zien en wanner er op wordt geklikt komt het scherm met de informatie van Groningen te staan

buttonU = Button(master = root,text = 'Utrecht', font= ('Helvetica', 16, 'bold italic'), command=utrecht, bg = '#2D5EA9', fg = '#F7F7F7')
buttonU.config(width=30, height= 5)
buttonU.place(x=900, y=350)     #laat een knop 'Utrecht' zien en wanner er op wordt geklikt komt het scherm met de informatie van Utrecht te staan







root.mainloop()



