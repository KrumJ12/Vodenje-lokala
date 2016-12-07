import random
import sqlite3
conn = sqlite3.connect('lokal.db')
c = conn.cursor()
c.execute('DELETE FROM nakupi')
c.execute('DELETE FROM racuni')

# vsakič izpraznemo tabelo pred novim vnosom

# cene, idji izdelkov
c.execute('SELECT id,cena FROM izdelki')
i = 0
cene = []
idji = []
for el in c.fetchall():
    idji.append(el[0])
    cene.append(el[1])

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
    # na generiranem računu bo od 1 do 3 artiklov
    znesek = 0
    koliko = random.randint(1,3)
    for x in range(koliko):
        kolicina = random.randint(1,2)
        artikel = random.randint(0,len(cene)-1)
        znesek += kolicina*cene[artikel]
        #print(st,idji[artikel],kolicina,len(cene),artikel)
        # vnesemo sproti v nakupe
        stavek2 = 'INSERT INTO nakupi (id_racuna,id_izdelka,kolicina) VALUES (?,?,?)'
        c.execute(stavek2, (st,idji[artikel],kolicina))
    # cas
    leto = random.choice(['2011','2012','2013','2014','2015','2016'])
    mesec = str(random.randint(1,12))
    if int(mesec) < 10:
        mesec = "0"+mesec
        
    dan = str(random.randint(1,28))
    if int(dan) < 10:
        dan = "0"+dan
    
    ura = str(random.randint(10,22))
    ura2 = "0" + str(random.randint(6,9))
    minute = str(random.randint(10,59))
    minute2 = "0"+str(random.randint(0,9))

    cas = leto + "-" + mesec + "-" + dan + " "
    cas += random.choice([ura,ura2])
    cas += ":"+random.choice([minute,minute2])
    
    # vnesimo v bazo
    stavek = 'INSERT INTO racuni (id,id_natakarja,znesek,cas_nakupa,nacin_placila) VALUES (?,?,?,?,?)'
    c.execute(stavek, (st,natakar,round(znesek,2),cas,nacin))

conn.commit()
