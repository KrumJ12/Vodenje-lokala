import random
import sqlite3
conn = sqlite3.connect('lokal.db')
c = conn.cursor()
c.execute('DELETE FROM dobavitelji')
# vsakič izpraznemo tabelo pred novim vnosom

sezNaslovov = []
for vrstica in open("naslovi.txt",encoding = 'utf-8'):
    naslov = vrstica.rstrip() + " " + str(random.randint(1,50))
    sezNaslovov.append(naslov)

sezPriimkov = []

for vrstica in open("priimki.txt",encoding='utf-8'):
    priimek = vrstica.split()[1]
    sezPriimkov.append(priimek)


n = 25 # stevilo dobaviteljev
for dobaviteljId in range(n):
    
    # telefon
    telefon = ""
    zac = ["030","031","041","040","051"]
    telefon += random.choice(zac) +" "
    for i in range(6):
        if i == 3:
            telefon +=" "
        cifra = random.randint(0,9)
        telefon += str(cifra)
        
    # imePodjetja   
    ime = random.choice(sezPriimkov)
    nazivi = [" s.p."," d.o.o."]
    sezPriimkov.remove(ime)
    naziv = ime+random.choice(nazivi)
    
    # e-posta
    koncMail = ["gmail.com","outlook.com","yahoo.com"]
    email = ime+"@"+random.choice(koncMail)
    
    # ID
    st = dobaviteljId + 1
    
    # davcna stevilka 8mestna
    davcna = ""
    for i in range(8):
        cifra = random.randint(0,9)
        davcna +=str(cifra)

    # trr
    # Primer pravilne strukture IBAN za račun v SLO: SI56 xxxx xxxx xxxx xxx.
    trr = "SI56 "
    for i in range(3):
        for j in range(4):
            trr += str(random.randint(0,9))
        trr +=" "
    for k in range(3):
        trr += str(random.randint(0,9))

    # naslov
    naslov = random.choice(sezNaslovov)
    sezNaslovov.remove(naslov)
    

    # vnesimo v bazo
    stavek = 'INSERT INTO dobavitelji (id,naziv,naslov,telefon,e_posta,davcna_stevilka,trr) VALUES (?,?,?,?,?,?,?)'
    c.execute(stavek, (st,naziv,naslov,telefon,email,davcna,trr))
conn.commit()

        
