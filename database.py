import psycopg2.extras
def inserter(datum,bericht,station,naam, keuring, naammod, mailadres, datum_mod): #wil alle benodigde info hebben om dit in de database te schijven

    with open('wachtwoord.txt') as w:
        wachtwoord = w.readline()

    connection_string = f"host = '20.254.113.210' dbname = 'stationszuil' user = 'postgres' password = {wachtwoord}"

    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    query = f"""INSERT INTO public.berichten(bericht, naam, datums, station, keuring, naam_mod, mailadres, datum_mod)
        VALUES ('{bericht}', '{naam}', '{datum}','{station}', '{keuring}', '{naammod}', '{mailadres}', '{datum_mod}');""" #voegt de benodigde variabele van het moderatie bestand toe

    cursor.execute(query)
    conn.commit() #verstuurt de informatie naar de database
    conn.close()

