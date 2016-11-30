import random
import sqlite3
conn = sqlite3.connect('lokal.db')
c = conn.cursor()
c.execute('DELETE FROM racuni')
# vsakič izpraznemo tabelo pred novim vnosom

# cene izdelkov
c.execute('SELECT cena FROM izdelki')
i = 0
cene = []
for cena in c.fetchall():
    cene.append(cena[0])

# seznam IDjev natakarjev
c.execute('SELECT id FROM zaposleni WHERE funkcija = 4')
natakarID = []
for natakar in c.fetchall():
    natakarID.append(natakar[0])

n = 100 # stevilo generiranih racunov
for racun in range(n):
    
    # ID
    st = racun + 1
    
    # nacin placila
    nacini = ['kartica','gotovina','gotovina','gotovina','kartica','dobavnica']
    nacin = random.choice(nacini)

    # natakar
    natakar = random.choice(natakarID)

    # znesek
    # na generiranem računu bo od 1 do 5 artiklov
    znesek = 0
    koliko = random.randint(1,3)
    for x in range(koliko):
        količina = random.randint(1,2)
        znesek += količina*random.choice(cene)

    # cas
    leto = random.choice(['2011','2012','2013','2014','2015','2016'])
    mesec = str(random.randint(1,12))
    dan = str(random.randint(1,28))
    ura = str(random.randint(10,22))
    ura2 = "0" + str(random.randint(6,9))
    minute = str(random.randint(10,59))
    minute2 = "0"+str(random.randint(0,9))

    cas = leto + "/" + mesec + "/" + dan + " "
    cas += random.choice([ura,ura2])
    cas += ":"+random.choice([minute,minute2])
    
    # vnesimo v bazo
    stavek = 'INSERT INTO racuni (id,id_natakarja,znesek,cas_nakupa,nacin_placila) VALUES (?,?,?,?,?)'
    c.execute(stavek, (st,natakar,round(znesek,2),cas,nacin))
conn.commit()
