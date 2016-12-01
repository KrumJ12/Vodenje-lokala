import random
import sqlite3
conn = sqlite3.connect('lokal.db')
c = conn.cursor()
c.execute('DELETE FROM pogodba')
# vsakič izpraznemo tabelo pred novim vnosom

# idji dobaviteljev
c.execute('SELECT id FROM dobavitelji')
idji = []
for el in c.fetchall():
    idji.append(el[0])


n = 10 # stevilo pogodb
for pogodba in range(n):
    
    # ID
    st = pogodba + 1
    
    # ID dobavitelja
    iddob = random.choice(idji)
    idji.remove(iddob)
    
    # tip
    tipi = ['pijaca','hrana','ostalo']
    tip = random.choice(tipi)

    # veljavnost
    leto = random.choice(['2015','2016','2017'])
    mesec = str(random.randint(1,12))
    velja = leto + "/" + mesec

    # ime
    ime = 'KAVA'
    
    # vnesimo v bazo
    stavek = 'INSERT INTO pogodba (id,id_dobavitelja,tip,veljavnost,ime) VALUES (?,?,?,?,?)'
    c.execute(stavek, (st,iddob,tip,velja,ime))

conn.commit()
