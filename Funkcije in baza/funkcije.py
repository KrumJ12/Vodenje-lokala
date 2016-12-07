import sqlite3
import time
from datetime import date
povezava = sqlite3.connect('lokal.db')
p = povezava.cursor()


def seznamZaposlenih():
    p.execute('SELECT ime,priimek FROM zaposleni')
    return p.fetchall()

def vnesiZaposlenega(ime,priimek,datum_rojstva,e_posta,funkcija,telefon,prebivalisce):
    # id se dodeli sam (AUTO INCREMENT)
    # ime in priimek poljubna niza
    # datum rojstva v obliki 'LETO-MESEC-DAN'
    # e_posta poljuben niz
    # funkcija med 1 in 5
    # datum zaposlitve bo datum na dan vnosa
    # telefon je oblike 'xxx xxx xxx'
    # prebivališče poljuben niz
    if datum_rojstva[4] != '-' or datum_rojstva[7] != '-':
        raise Exception('Napačna oblika datuma')
    if not 1<=funkcija<=5:
        raise Exception('Ta funkcija ne obstaja')
    danes = date.today()
    datum_zaposlitve = danes.isoformat()
    stavek = 'INSERT INTO zaposleni (ime,priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce) VALUES (?,?,?,?,?,?,?,?)'
    p.execute(stavek, (ime,priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce))
    povezava.commit()

def seznamIzdelkov():
    izdelki = []
    p.execute('SELECT ime FROM izdelki')
    for izdelek in p.fetchall():
        izdelki.append(izdelek[0])
    return izdelki

def seznamPogodb():
    pogodbe = []
    p.execute('SELECT ime,tip,veljavnost FROM pogodba')
    for pogodba in p.fetchall():
        pogodbe.append(pogodba)
    return pogodbe

def seznamDobaviteljev():
    dob = []
    p.execute('SELECT naziv,davcna_stevilka FROM dobavitelji')
    for dobavitelj in p.fetchall():
        dob.append(dobavitelj)
    return dob

def vnesiRacun():
    pass

def vnesiPogodbo():
    pass

def vnesiDobavitelja():
    pass

def vnesiIzdelek():
    pass
