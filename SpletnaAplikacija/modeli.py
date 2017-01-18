import sqlite3
import time
from datetime import date, time, datetime
povezava = sqlite3.connect('lokal.db')
p = povezava.cursor()
povezava.row_factory = sqlite3.Row


def seznamZaposlenih():
    sql = '''SELECT id,ime,priimek,datum_rojstva,e_posta,datum_zaposlitve,funkcija,telefon,prebivalisce FROM zaposleni  ORDER BY datum_zaposlitve DESC'''
    return list(povezava.execute(sql))



def akcije():
    sql = '''SELECT id,izdelek,vrednost FROM akcija ORDER BY izdelek ASC'''
    return list(povezava.execute(sql))
    
def tabIzdelkov():
    sql = '''SELECT id,ime,zaloga,tip,cena FROM izdelki'''
    return {el['id']: el for el in povezava.execute(sql)}

def imeCena(idizd):
    sql = '''SELECT ime,cena FROM izdelki WHERE id = ?'''
    return list(povezava.execute(sql),[idizd])

def seznamIzdelkov():
    izdelki = []
    p.execute('SELECT ime FROM izdelki')
    for izdelek in p.fetchall():
        izdelki.append(izdelek[0])
    return izdelki


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
    sql = '''SELECT id,naziv,naslov,telefon,e_posta,davcna_stevilka,trr FROM dobavitelji'''
    return list(povezava.execute(sql))

def imenaDobaviteljev():
    sql = '''SELECT naziv FROM dobavitelji'''
    return list(povezava.execute(sql))

def vrniIDDobavitelja(naziv):
    sql = '''SELECT id FROM dobavitelji WHERE naziv = ?'''
    return list(p.execute(sql,[naziv]))[0][0]

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

def seznamImenIzdelkov():
    sql='''SELECT ime FROM izdelki ORDER BY ime ASC'''
    return list(povezava.execute(sql))

##########################################################
# SEZNAM NATAKARJEV
def seznamNatakarjev():
    sql = '''SELECT id FROM zaposleni WHERE funkcija=4'''
    return list(povezava.execute(sql))


##########################################################
# VNESI RAČUN, NAKUP

def vnesiNakup(seznam):
    stavek = 'SELECT MAX(id) FROM racuni'
    idracuna = list(p.execute(stavek))[0][0]

    slovarIzd = {}
    for izd in seznam:
        slovarIzd[izd] = slovarIzd.get(izd,0) + 1

    # sez oblike {12: 1, 13: 1, 14: 2}
    for idizd in slovarIzd.keys():
        stavek = 'INSERT INTO nakupi (id_racuna,id_izdelka,kolicina) VALUES (?,?,?)'
        p.execute(stavek,(idracuna,idizd,slovarIzd[idizd]))
    povezava.commit()
    
def vnesiRacun(znesek,nacin_placila,id_natakarja):
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
    if znesek > 0:    
        stavek = 'INSERT INTO racuni (id_natakarja,znesek,cas_nakupa,nacin_placila) VALUES (?,?,?,?)'
        p.execute(stavek,(id_natakarja,znesek,cas_nakupa,nacin_placila))
        povezava.commit()

def vrniCeno(id_izd):
    stavek= 'SELECT cena FROM izdelki WHERE id = ?'
    return list(p.execute(stavek,[id_izd]))[0][0]

def izracunajZnesek(sez_izd):
    # dobi seznam izdelkov in izračuna znesek
    znesek = 0

    #seznam izdelkov in njihova cena
    sez_id_cena=[]
    #seznam akcij --> id-jev izdelkov in vrednost akcije
    id_akcij=list( x['izdelek']for x in akcije())
    vrednost_akcij=list(x['vrednost'] for x in akcije())
    for id_izd in sez_izd:
        #če je izdelek v akciji
        if int(id_izd) in id_akcij:
            #vrednost iz '40' pretvorimo v 0.6 koef. s katerim pomnožimo prvotno ceno 
            vrednost=(100-int(vrednost_akcij[id_akcij.index(int(id_izd))]))/100
            znesek+= float(vrniCeno(id_izd)) * vrednost
        else:
            znesek+= float(vrniCeno(id_izd))
    return round(znesek,2)

def izracunajZnesekSez():
    '''funkcija vrne seznam cen izdelkov z akcijo'''
    # dobi seznam izdelkov in izračuna znesek
    znesek = []
    #seznam izdelkov in njihova cena
    sez_id_cena=[]
    #seznam akcij --> id-jev izdelkov in vrednost akcije
    id_akcij=list( x['izdelek']for x in akcije())
    vrednost_akcij=list(x['vrednost'] for x in akcije())
    for id_izd in sorted(seznamIzdelkov_id()):
        #če je izdelek v akciji
        if int(id_izd) in id_akcij:
            #vrednost iz '40' pretvorimo v 0.6 koef. s katerim pomnožimo prvotno ceno 
            vrednost=(100-int(vrednost_akcij[id_akcij.index(int(id_izd))]))/100
            znesek.append(round(float(vrniCeno(id_izd)) * vrednost,2))
        else:
            znesek.append("/")
    return znesek

###################################################################
# IZDANI RAČUNI

def izdaniRacuni():
    sql = '''SELECT id,id_natakarja,znesek,cas_nakupa,nacin_placila FROM racuni ORDER BY cas_nakupa DESC'''
    return list(povezava.execute(sql))


####################################################################
# AKCIJE
def vrniIDizd(ime):
    """Iz imena izdelka dobimo ID izdelka"""
    sql = '''SELECT id FROM izdelki WHERE ime = ?'''
    return list(p.execute(sql,[ime]))[0][0]

# SPREMENI AKCIJO

def dodajAkcijo(id_izd, vrednost):
    stavek = 'INSERT INTO akcija (izdelek,vrednost) VALUES (?,?)'
    p.execute(stavek,(id_izd, vrednost))
    povezava.commit()  

def spremeniAkcijo(ime,vrednost):
    '''Obstojeci akciji bomo spremenili vrednost'''
    stavek = 'UPDATE akcija SET vrednost= ? WHERE izdelek=?'
    p.execute(stavek, (vrednost,ime))

    povezava.commit()
    
# UREJANJE, BRISANJE AKCIJE
def akcija(id_akc):
    sql = '''
        SELECT id,izdelek,vrednost FROM akcija
        WHERE id = ?
    '''
    return povezava.execute(sql,[id_akc]).fetchone()
    
def uredi_akcijo(id_akc,izdelek,vrednost):
    sql = '''
        UPDATE akcija
        SET izdelek = ?, vrednost = ?
        WHERE id = ?
    '''
    povezava.execute(sql, [izdelek,vrednost,id_akc])
    povezava.commit()

def odstrani_akcijo(id_akc):
    stavek = '''DELETE FROM akcija WHERE id = ?'''
    povezava.execute(stavek,[id_akc])
    povezava.commit()

    
###############################################################################################
# IZDELKI

def tabelaIzdelkov():
    sql = '''SELECT id,ime,tip,zaloga,cena FROM izdelki ORDER BY ime'''
    return list(povezava.execute(sql))

# VNESI IZDELEK

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

# UREJANJE, BRISANJE IZDELKA
def izdelek(id_izd):
    sql = '''
        SELECT id,ime,tip,zaloga,cena FROM izdelki
        WHERE id = ?
    '''
    return povezava.execute(sql,[id_izd]).fetchone()
    
def uredi_izdelek(id_izd,ime,tip,zaloga,cena):
    sql = '''
        UPDATE izdelki
        SET ime = ?, tip = ?, zaloga = ?, cena = ?
        WHERE id = ?
    '''
    povezava.execute(sql, [ime,tip,zaloga,cena,id_izd])
    povezava.commit()

def odstrani_izdelek(id_izd):
    stavek = '''DELETE FROM izdelki WHERE id = ?'''
    povezava.execute(stavek,[id_izd])
    povezava.commit()

###############################################################################################
# VNESI ZAPOSLENEGA
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



# UREJANJE ZAPOSLENEGA

def zaposlen(id_zap):
    sql = '''
        SELECT id, ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce
        FROM zaposleni
        WHERE id = ?
    '''
    return povezava.execute(sql, [id_zap]).fetchone()
    
def uredi_zaposlenega(id_zap, ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce):
    sql = '''
        UPDATE zaposleni
        SET ime = ?, priimek = ?, datum_rojstva = ?, e_posta = ?, funkcija = ?, datum_zaposlitve = ?, telefon = ?, prebivalisce = ?
        WHERE id = ?
    '''
    povezava.execute(sql, [ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce, id_zap])
    povezava.commit()

def odstrani_zaposlenega(id_zap):
    stavek = '''DELETE FROM zaposleni WHERE id = ?'''
    povezava.execute(stavek,[id_zap])
    povezava.commit()

###############################################################################################
# VNESI POGODBO

def vnesiPogodbo(ime,id_dobavitelja,tip,veljavnost):
    # id se dodeli sam AUTO INCREMENT
    # tip je "hrana","pijača","ostalo"
    # veljavnost do vključno "LETO-MESEC"
    if veljavnost[4] != "-":
        raise Exception('Datum pogodbe je neveljaven')
    stavek = 'INSERT INTO pogodba (id_dobavitelja,tip,veljavnost,ime) VALUES (?,?,?,?)'
    p.execute(stavek, (id_dobavitelja,tip,veljavnost,ime))
    povezava.commit()

# UREJANJE POGODBE

def pogodba(id_pog):
    sql = '''
        SELECT id, id_dobavitelja, tip, veljavnost, ime
        FROM pogodba
        WHERE id = ?
    '''
    return povezava.execute(sql, [id_pog]).fetchone()
    
def uredi_pogodbo(id_pog, tip, veljavnost, ime):
    sql = '''
        UPDATE pogodba
        SET tip = ?, veljavnost = ?, ime = ?
        WHERE id = ?
    '''
    povezava.execute(sql, [tip,veljavnost,ime,id_pog])
    povezava.commit()
# ODSTRANI POGODBO

def odstrani_pogodbo(id_pog):
    stavek = '''DELETE FROM pogodba WHERE id = ?'''
    povezava.execute(stavek,[id_pog])
    povezava.commit()
    
###############################################################################################
# VNESI DOBAVITELJA

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



# UREJANJE DOBAVITELJA

def dobavitelj(id_dob):
    """Vrne podatke o dobavitelju z IDjem id_dob
    V obliki za html"""
    stavek = '''SELECT id,naziv,naslov,telefon,e_posta,davcna_stevilka,trr FROM dobavitelji
                WHERE id = ?'''

    return povezava.execute(stavek,[id_dob]).fetchone()

def pogodbeDobaviteljev(id_dob):
    """Vrne podatke o pogodbah dobavitelja id_dob"""
    stavek = '''SELECT id,id_dobavitelja,tip,veljavnost,ime FROM pogodba WHERE id_dobavitelja = ?'''
    return povezava.execute(stavek,[id_dob]).fetchall()

def uredi_dobavitelja(id_dob,naziv,naslov,telefon,e_posta,davcna_stevilka,trr):
    stavek = '''UPDATE dobavitelji
    SET naziv = ?, naslov =?, telefon=?, e_posta=?, davcna_stevilka=?,trr=?
    WHERE id = ?'''
    povezava.execute(stavek,[naziv,naslov,telefon,e_posta,davcna_stevilka,trr,id_dob])
    povezava.commit()

# ODSTRANI DOBAVITELJA TER POGODBO, ČE JO IMA
def odstrani_dobavitelja(id_dob):
    stavek = '''DELETE FROM dobavitelji WHERE id = ?'''
    stavek2 = '''DELETE FROM pogodba WHERE id_dobavitelja= ? '''
    povezava.execute(stavek2,[id_dob])
    povezava.execute(stavek,[id_dob])

    povezava.commit()
    
################################################################################################

