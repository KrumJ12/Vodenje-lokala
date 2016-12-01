import random
import sqlite3
conn = sqlite3.connect('lokal.db')
c = conn.cursor()
c.execute('DELETE FROM zaposleni')
# vsakič izpraznemo tabelo pred novim vnosom

sezNaslovov = []
for vrstica in open("naslovi.txt",encoding = 'utf-8'):
    naslov = vrstica.rstrip() + " " + str(random.randint(1,50))
    sezNaslovov.append(naslov)

zenske = []
moski = []
for vrstica in open("imena.txt",encoding='utf-8'):
    sez = vrstica.split()
    moskoIme = sez[1]
    zenskoIme = sez[3]
    zenske.append(zenskoIme)
    moski.append(moskoIme)

sezPriimkov = []

for vrstica in open("priimki.txt",encoding='utf-8'):
    priimek = vrstica.split()[1]
    sezPriimkov.append(priimek)


imena = zenske + moski
n = 25 # stevilo zaposlenih
for zaposlen in range(n):
    
    # funkcija
    # 1-sef, 2-vodjaIzmene, 3-kuhar 4-natakar, 5-ostaloOsebje
    # prvi je sef, drugi vodja izmene
    funkcije = [3,4,5]
    funkcija = random.choice(funkcije)
    if zaposlen == 0:
        funkcija = 1
    if zaposlen == 1:
        funkcija = 2
    

    #datum rojstva
    datumRojstva = ""
    letoRojstva = random.randint(1950,1998)
    datumRojstva += str(letoRojstva)
    mesecRojstva = random.randint(1,12)
    danRojstva = random.randint(1,28)
    datumRojstva +="/"+str(mesecRojstva)
    datumRojstva +="/"+str(danRojstva)

    # datum zaposlitve
    datum = ""
    leto = random.randint(2010,2016)
    mesec = random.randint(1,12)
    dan = random.randint(1,28)
    datum +=str(leto)
    datum +="/"+str(mesec)
    datum +="/"+str(dan)
    # telefon
    telefon = ""
    zac = ["030","031","041","040","051"]
    telefon += random.choice(zac) +" "
    for i in range(6):
        if i == 3:
            telefon +=" "
        cifra = random.randint(0,9)
        telefon += str(cifra)
    # ime, priimek    
    ime = random.choice(imena)
    imena.remove(ime)
    priimek = random.choice(sezPriimkov)
    sezPriimkov.remove(priimek)
    # e-posta
    koncMail = ["gmail.com","hotmail.com","outlook.com","yahoo.com"]
    email = ime+"."+priimek+"@"+random.choice(koncMail)
    # ID
    st = zaposlen + 1
    # prebivalisce
    naslov = random.choice(sezNaslovov)
    sezNaslovov.remove(naslov)

    # vnesimo v bazo
    stavek = 'INSERT INTO zaposleni (id,ime,priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce) VALUES (?,?,?,?,?,?,?,?,?)'
    c.execute(stavek, (st,ime,priimek,datumRojstva,email,funkcija,datum,telefon,naslov))
    
conn.commit()

        
