import sqlite3
import time
from datetime import date, time, datetime
povezava = sqlite3.connect('lokal.db')
p = povezava.cursor()
povezava.row_factory = sqlite3.Row


def seznamZaposlenih():
    sql = '''SELECT id,ime,priimek,datum_rojstva,e_posta,datum_zaposlitve,telefon,prebivalisce FROM zaposleni  ORDER BY datum_zaposlitve DESC'''
    return list(povezava.execute(sql))

def izdaniRacuni():
    sql = '''SELECT id,id_natakarja,znesek,cas_nakupa,nacin_placila FROM racuni ORDER BY cas_nakupa DESC'''
    return list(povezava.execute(sql))

def tabIzdelkov():
    sql = '''SELECT id,ime,zaloga,tip,cena FROM izdelki'''
    return list(povezava.execute(sql))


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
    povezava.execute(stavek, (ime,priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce))
    povezava.commit()

def seznamIzdelkov():
    izdelki = []
    p.execute('SELECT ime FROM izdelki')
    for izdelek in p.fetchall():
        izdelki.append(izdelek[0])
    return izdelki


def tabelaIzdelkov():
    sql = '''SELECT ime,tip,zaloga,cena FROM izdelki ORDER BY ime'''
    return list(povezava.execute(sql))


def imeInCenaIzdelkov():
    sql = '''SELECT ime,cena FROM izdelki ORDER BY tip'''
    return list(povezava.execute(sql))

def seznamIzdelkov_id():
    izdelki=[]
    p.execute('SELECT id FROM izdelki')
    for izdelek in p.fetchall():
        izdelki.append(izdelek[0])
    return izdelki

def seznamPogodb():
    sql = '''SELECT ime,tip,veljavnost,id_dobavitelja,id FROM pogodba'''
    return list(povezava.execute(sql))

def seznamDobaviteljev():
    sql = '''SELECT naziv,naslov,telefon,e_posta,davcna_stevilka,trr FROM dobavitelji'''
    return list(povezava.execute(sql))

def imenaDobaviteljev():
    sql = '''SELECT naziv FROM dobavitelji'''
    return list(povezava.execute(sql))

def vrniIDDobavitelja(naziv):
    sql = '''SELECT id FROM dobavitelji WHERE naziv = ?'''
    return list(p.execute(sql,[naziv]))[0][0]

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
    
def vnesiRacun(id_natakarja,znesek,nacin_placila):
    # znesek je potrebno izračunati s funkcijo izracunajZnesek
    # cas_nakupa bo ob vnosu računa
    # način plačila je niz 'gotovina','kartica','dobavnica'

    #cas nakupa ob vnosu racuna
    dt = datetime.now()
    tt = dt.timetuple()
    sezCasNakupa = []
    i = 0
    while i < 5:
        sezCasNakupa.append(str(tt[i]))
        i+=1
    for i in range(1,5):
        if len(sezCasNakupa[i]) <2:
            sezCasNakupa[i] = "0"+sezCasNakupa[i]
    tt = sezCasNakupa
    cas_nakupa = tt[0]+"-"+tt[1]+"-"+tt[2]+" "+tt[3]+":"+tt[4]

    #id natakarja

    # znesek

def izracunajZnesek():
    pass

def vnesiIzdelek(ime,zaloga,tip=None,cena = 0):
    if ime in seznamIzdelkov():
        stavek = 'UPDATE izdelki SET zaloga = zaloga + ? WHERE ime = ?'
        p.execute(stavek,(zaloga,ime))
    else:
        if tip == None or cena == 0:
            raise Exception('Gre za nov izdelek! Vnesi tip izdelka in/ali ceno!')
        stavek = 'INSERT INTO izdelki (ime,zaloga,tip,cena) VALUES (?,?,?,?)'
        p.execute(stavek,(ime,zaloga,tip,cena))
    povezava.commit()

def vnesiAkcijo(izdelek_ime, zacetek, konec, vrednost):
    #zacetek in konec akcije sta v obliki llll-mm-dd
    #vrednost akcije je med 0 in 100
    #vneseš ime izdelka
    sez_imen=seznamIzdelkov()
    if izdelek_ime not in sez_imen:
        raise Exception('Izdelka ni v bazi')
    if zacetek[4] != '-' or zacetek[7] !='-':
        raise Exception('Napačen čas začetka akcije')
    if konec[4] != '-' or konec[7] !='-':
        raise Exception('Napačen čas konca akcije')
    if 0<=vrednost<=100:
        raise Exception('Napačna vrednost akcije')
    id_izdelka=seznamIzdelkov_id()[sez_imen.index(izdelek_ime)]
    stavek = 'INSERT INTO akcija (izdelek, zacetek_akcije,konec_akcije,vrednost) VALUES (?,?,?,?)'
    p.execute(stavek,(id_izdelka, zacetek, konec, vrednost))
    povezava.commit()

    
    

def vrniZaposlenega(mesto):
    '''vnesi številko od 1 do 5. 1--> šef, 2--> vodja izmene, 3--> kuhar, 4--> natakar
5--> ostalo osebje'''
    sez=[]
    stavek= 'SELECT ime, priimek FROM zaposleni WHERE funkcija = ?'
    p.execute(stavek, (str(mesto)))
    for zaposlen in p.fetchall():
        sez.append(zaposlen)
    povezava.commit()
    return sez

def seznamImenovIzdelkov():
    sql='''SELECT ime FROM izdelki ORDER BY ime ASC'''
    return list(povezava.execute(sql))

def spremeniCeno(ime_izdelka,nova_cena):
    '''danemu izdelku bomo spremenili ceno'''
    if ime_izdelka in seznamIzdelkov():
        stavek = 'UPDATE izdelki SET cena= ? WHERE ime=?'
        p.execute(stavek, (nova_cena, ime_izdelka))
    else:
        raise Exception ('Izdeleka še ni v tabeli')
    povezava.commit()

def dodajZalogo(ime, kolicina):
    #dobiti je treba, koliko je izdelkov sedaj
    #in prišteti novo
    stavek='UPDATE izdelki SET zaloga= zaloga + ? WHERE ime=?'
    p.execute(stavek, (kolicina, ime))
    povezava.commit()

def oseba(oseba):
    sql = '''
        SELECT id, ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce
        FROM zaposleni
        WHERE id = ?
    '''
    return povezava.execute(sql, [oseba]).fetchone()
    
def uredi_osebo(oseba, ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce):
    sql = '''
        UPDATE zaposleni
        SET ime = ?, priimek = ?, datum_rojstva = ?, e_posta = ?, funkcija = ?, datum_zaposlitve = ?, telefon = ?, prebivalisce = ?
        WHERE id = ?
    '''
    povezava.execute(sql, [ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce, oseba])
    povezava.commit()
    
    
