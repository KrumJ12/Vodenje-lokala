Vodenje lokala
======
Seminarska naloga pri predmetu Podatkovne baze 1, Praktična matematika

Namen
------

Lastnik lokala bi rad imel pregled nad stvarmi, ki se odvijajo v lokalu. Na enem mestu bi rad imel zbrane podatke o svojih zaposlenih, izdanih računih ter shrambi pijače/hrane/prigrizkov.Ker ima veliko različnih pogodb z dobavitelji za kavo in druge vrste pijač in hrane, bi imeli še pregled nad dobavitelji. 

####Imeli bi program, ki bi omogočal vpogled v določene tabele(torej v ozadju bi bila baza podatkov).


###Tako bi imeli več tabel:
- tabela Računi (ID, znesek, način plačila, ID natakarja, ...)
- tabela Zaposleni (ID, ime, priimek, funkcija/delovno mesto, prebivališče, datum zaposlitve, e-pošta, telefon, ...)
- tabela Pijače (ime, tip, količina, enot(koliko enot je še na voljo v shrambi), cena, ...)
- tabela Hrana (ime, količina, enot, cena)
- tabela Dobavitelji (ID dobavitelja, ID pogodbe, ime priimek (oz. ime podjetja), naslov, e-pošta, telefon)
- tabela Pogodbe (ID pogodbe, ime, tip, ...)
- tabela Zaloga (ime pijače/hrane, tip, količina , ...)

Ukazi SQL (potrebni za poizvedbo) bi bili seveda »zamaskirani« v gumbe, ker ne pričakujemo da bo končni uporabnik (lastnik, zaposleni v lokalu) obvladal jezik SQL.
Uporabnik bi lahko izbral ustrezno »tabelo« oziroma kategorijo, ki ga zanima, potem pa z vnosom niza oziroma številke dobil ustrezne rezultate. (npr. klik na ID računa, vnesel bi ustrezno številko in bi dobil vse podatke o tem izdanem računu)
Imel bi npr. gumbe za vnos oziroma popravek količine pijače/hrane v shrambi. S klikom na ustrezno mesto v tabeli, bi lahko popravil vnos (npr. podatke o zaposlenih, seveda pa ne znesek računa).
Če bi želeli iz ponudbe umakniti določeno pijačo, bi za to poskrbel drug gumb, ipd…

![alt text](http://shrani.si/f/2h/w4/1hrJomVs/diagram.png "ER Diagram")
