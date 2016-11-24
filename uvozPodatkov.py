import sqlite3
conn = sqlite3.connect('lokal.db')
c = conn.cursor()
poizvedba = c.execute('SELECT ime FROM zaposleni')

c.execute('DELETE FROM izdelki')

st = 1
for vrstica in open('pijaca.txt',encoding='utf-8'):
    sez = vrstica.split()
    el = sez[-1]
    if sez[-1] == '€':
        el = sez[-2]+sez[-1]
    el = el.split(',')
    el = el[0]+'.'+el[1][:2]
    ime = sez[0]
    cena = el
    stavek = 'INSERT INTO izdelki (id,ime,zaloga,tip,cena) VALUES (?, ?, ?, ?, ?)'
    c.execute(stavek, (st, ime, 0, "pijaca", cena))

    st +=1

conn.commit()
