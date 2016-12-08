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

def seznamIzdelkov_id():
    izdelki=[]
    p.execute('SELECT id FROM izdelki')
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

def vnesiPogodbo(ime,id_dobavitelja,tip,veljavnost):
    # id se dodeli sam AUTO INCREMENT
    # tip je "hrana","pijača","ostalo"
    # veljavnost do vključno "LETO-MESEC"
    if veljavnost[4] != "-":
        raise Exception('Datum pogodbe je neveljaven')
    stavek = 'INSERT INTO pogodba (id_dobavitelja,tip,veljavnost,ime) VALUES (?,?,?,?)'
    p.execute(stavek, (id_dobavitelja,tip,veljavnost,ime))
    povezava.commit()

def vnesiDobavitelja(naziv,naslov,telefon,e_posta,davcna_stevilka,trr):
    #naziv npr. Naziv s.p.
    # telefon xxx xxx xxx
    # davcna 8 mestna
    # trr SI56 xxxx xxxx xxxx xxx
    if not "@" in e_posta:
        raise Exception('Nepravilen zapis e-pošte')
    if len(str(davcna_stevilka)) != 8:
        raise Exception('Nepravilna davčna številka')
    if len(trr) != 23:
        raise Exception('Nepravilen TRR')
    stavek = 'INSERT INTO dobavitelji (naziv,naslov,telefon,e_posta,davcna_stevilka,trr) VALUES (?,?,?,?,?,?)'
    p.execute(stavek, (naziv,naslov,telefon,e_posta,davcna_stevilka,trr))
    povezava.commit()
    
def vnesiRacun():
    pass

def vnesiIzdelek(ime,zaloga,tip='/',cena = 0):
    if ime in seznamIzdelkov():
        stavek = 'UPDATE izdelki SET zaloga = zaloga + ? WHERE ime = ?'
        p.execute(stavek,(zaloga,ime))
    else:
        if tip == '/' or cena == 0:
            raise Exception('Gre za nov izdelek! Vnesi tip izdelka in/ali ceno!')
        stavek = 'INSERT INTO izdelki (ime,zaloga,tip,cena) VALUES (?,?,?,?)'
        p.execute(stavek,(ime,zaloga,tip,cena))
    povezava.commit()

def vnesiAkcijo(izdelek_ime, zacetek, konec, vrednost):
    #zacetek in konec akcije sta v obliki llll-mm-dd
    #vrednost akcije je med 0 in 100
    #vneseš ime izdelka
    sez_imen=seznamIzdelkov()
    id_izdelka=seznamIzdelkov_id()[sez_imen.index(izdelek_ime)]
    stavek = 'INSERT INTO akcija (izdelek, zacetek_akcije,konec_akcije,vrednost) VALUES (?,?,?,?)'
    p.execute(stavek,(id_izdelka, zacetek, konec, vrednost))
    povezava.commit()
    
    
