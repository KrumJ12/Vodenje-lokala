import sqlite3
conn = sqlite3.connect('lokal.db')
c = conn.cursor()
c.execute('DELETE FROM izdelki')
# vsakič izpraznemo tabelo pred novim vnosom

st = 1
for vrstica in open('uvozPijace.txt',encoding='utf-8'):
    sez = vrstica.split()
    ind = 0
    ime = ""
    while ind < len(sez)-1:
        ime +=sez[ind]+" "
        ind = ind + 1
    cena = sez[-1]
    stavek = 'INSERT INTO izdelki (id,ime,zaloga,tip,cena) VALUES (?, ?, ?, ?, ?)'
    c.execute(stavek, (st, ime, 0, "pijaca", cena))
    st +=1

conn.commit()
