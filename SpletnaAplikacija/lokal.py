#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, get, post, redirect
import modeli


################################################
# PRVA STRAN IN IZDAJA RAČUNOV
@route('/')
def domov():
    izdelki = [int(x) for x in request.query.getall('id')]
    nacin = request.query.getall('nacin')
    return template(
        'domov',
        imena=modeli.slovarIzdelkov(),
        imenaTIP = modeli.tabelaIzdelkovTIP(),
        izdelki = izdelki,
        nacin = nacin,
        akcija = modeli.slovarAkcij(),
        znesek = modeli.izracunajZnesek(izdelki),
        natakarji = modeli.seznamNatakarjev(),
        plac = '&'.join('nacin={}'.format(x) for x in nacin),
        link='&'.join('id={}'.format(x) for x in izdelki))

@post('/noviRacun')
def vnesiRacun():
    placilo = int(request.forms.getone('placilo'))
    znesek = float(request.forms.getone('znesek'))
    izdelki = request.forms.getall('izdelek')
    # če ni določen id_natakarja
    try:
        id_natakarja = request.forms.getall('id_nat')[0]
    except: # vzame prvega
        id_natakarja = modeli.seznamNatakarjev()[0][0]
    moznosti = ['gotovina','kartica','dobavnica']
    modeli.vnesiRacun(znesek,moznosti[placilo-1],id_natakarja)
    modeli.vnesiNakup(izdelki)
    modeli.popraviZalogo(izdelki)
    redirect('/racun')

    
################################################
# AKCIJE
@route('/akcije')
def akcija():
    return template('akcije',izdelki = modeli.tabIzdelkov(),
                    imena = modeli.seznamImenIzdelkov(),
                    seznamAkcij=modeli.akcije())

@post('/dodajAkcijo')
def dodajAkcijo():
    ime = request.forms.izdelek
    vrednost = request.forms.vrednost
    imeID = modeli.vrniIDizd(ime)
    modeli.dodajAkcijo(imeID,vrednost)
    redirect('/akcije')


@post('/spremeniAkcijo')
def spremeniAkcijo():
    ime=request.forms.akcija
    vrednost=int(request.forms.vrednost)
    ime = ime.split(' - ')[1]
    imeID = modeli.vrniIDizd(ime)
    modeli.spremeniAkcijo(imeID,vrednost)
    redirect('/akcije')


@get('/akcije/<id_akc>/uredi')
def uredi_akcijo(id_akc):
    return template(
        'urediAkcijo',
        akcija=modeli.akcija(id_akc))

@post('/akcije/<id_akc>/uredi')
def uredi_akcijo_submit(id_akc):
    id_akc = request.forms.id_akc
    izdelek = request.forms.izdelek
    vrednost = request.forms.vrednost
    modeli.uredi_akcijo(id_akc,izdelek,vrednost)
    redirect('/akcije')

@get('/akcije/<id_akc>/odstrani')
def odstrani_izdelek(id_akc):
    return template('odstraniAkcijo', izdelki = modeli.tabIzdelkov(),
                    akcija = modeli.akcija(id_akc))

@post('/akcije/<id_akc>/odstrani')
def odstrani_akcijo(id_akc):
    id_akc = request.forms.id_akc
    modeli.odstrani_akcijo(id_akc)
    redirect('/akcije')

################################################
# TABELA IZDANIH RAČUNOV
@route('/racun')
def racun():
    return template(
        'racun',seznam = modeli.izdaniRacuni(),
        naRacunu = modeli.kajJeNaRacunu())
#################################################

# IZDELKI
@route('/izdelki')
def izdelki():
    return template('izdelki',imena=modeli.seznamImenIzdelkov(),
                    izdelkiIme = modeli.tabelaIzdelkovIME())

@post('/spremeniCeno')
def spremeniCeno():
    ime=request.forms.izdelek
    cena=request.forms.cena
    modeli.spremeniCeno(ime,cena)
    redirect('/izdelki')

@post('/dodajZalogo')
def dodaj_Zalogo():
    ime=request.forms.izdelek
    zaloga=int(request.forms.zaloga)
    modeli.dodajZalogo(ime,zaloga)
    redirect('/izdelki')

@post('/izdelki')
def preberi():
    ime = request.forms.ime
    zaloga  = int(request.forms.zaloga)
    tip = request.forms.tip
    cena  = float(request.forms.cena)
    
    if 'Tip' in tip:
        tip = '/'
    modeli.vnesiIzdelek(ime,zaloga,tip,cena)
    
    redirect('/izdelki')

# UREDI, IZBRIŠI IZDELEK

@get('/izdelki/<id_izd>/uredi')
def uredi_izdelek(id_izd):
    return template(
        'urediIzdelek',
        izdelek=modeli.izdelek(id_izd))

@post('/izdelki/<id_izd>/uredi')
def uredi_izdelek_submit(id_izd):
    id_izd = request.forms.id_izd
    ime = request.forms.ime
    tip = request.forms.tip
    zaloga = request.forms.zaloga
    cena = request.forms.cena
    modeli.uredi_izdelek(id_izd,ime,tip,zaloga,cena)
    redirect('/izdelki')

@get('/izdelki/<id_izd>/odstrani')
def odstrani_izdelek(id_izd):
    return template('odstraniIzdelek', izdelek = modeli.izdelek(id_izd))

@post('/izdelki/<id_izd>/odstrani')
def odstrani_izdelek(id_izd):
    id_izd = request.forms.id_izd
    modeli.odstrani_izdelek(id_izd)
    modeli.odstrani_akcijo(id_izd)
    redirect('/izdelki')
    
######### ######### ######### #########

@route('/zaposleni')
def zaposleni():
    return template(
        'zaposleni',seznam = modeli.seznamZaposlenih(), fun=modeli.funkcijaVLokalu())

@post('/zaposleni')
def zaposleni():
    ime = request.forms.ime
    priimek = request.forms.priimek
    datum_rojstva = request.forms.datum_rojstva
    eposta = request.forms.eposta
    funkcija = request.forms.funkcija
    sez = ['Šef','Vodja izmene','Kuhar','Natakar','Ostalo osebje']
    funkcija = sez.index(funkcija)+1
    tel = request.forms.telefon
    prebivalisce = request.forms.prebivalisce
    modeli.vnesiZaposlenega(ime,priimek,datum_rojstva,eposta,funkcija,tel,prebivalisce)
    redirect('/zaposleni')
    
# UREDI, IZBRIŠI ZAPOSLENEGA
@get('/zaposleni/<id_zap>/uredi')
def uredi_zaposlenega(id_zap):
    return template(
        'urediZaposlenega',
        zaposlen=modeli.zaposlen(id_zap)
    )

@post('/zaposleni/<id_zap>/uredi')
def uredi_zaposlenega_submit(id_zap):
    id_zap = request.forms.id_zap
    ime = request.forms.ime
    priimek = request.forms.priimek
    datum_rojstva = request.forms.datum_rojstva
    e_posta = request.forms.e_posta
    funkcija = request.forms.funkcija
    sez = ['Šef','Vodja izmene','Kuhar','Natakar','Ostalo osebje']
    funkcija = sez.index(funkcija)+1
    telefon = request.forms.telefon
    prebivalisce = request.forms.prebivalisce
    modeli.uredi_zaposlenega(id_zap, ime, priimek,datum_rojstva,e_posta,funkcija,telefon,prebivalisce)
    redirect('/zaposleni')

@get('/zaposleni/<id_zap>/odstrani')
def odstrani_zaposlenega(id_zap):
    return template('odstraniZaposlenega', zaposlen = modeli.zaposlen(id_zap))

@post('/zaposleni/<id_zap>/odstrani')
def odstrani_zaposlenega(id_zap):
    id_zap = request.forms.id_zap
    modeli.odstrani_zaposlenega(id_zap)
    redirect('/zaposleni')

######### ######### ######### #########
# POGODBE
@route('/pogodbe')
def pogodbe():
    return template(
        'pogodbe',seznam=modeli.seznamPogodb(),
        imena=modeli.imenaDobaviteljev(),
        dobavitelji=modeli.IDimeDobaviteljev())

@post('/pogodbe')
def dodaj_pogodbo():
    ime=request.forms.ime
    tip=request.forms.tip
    veljavnost=request.forms.veljavnost
    # pretvori iz Imena v ID
    id_dobavitelja=request.forms.id_dobavitelja
    id_dobavitelja = modeli.vrniIDDobavitelja(id_dobavitelja)
    modeli.vnesiPogodbo(ime,id_dobavitelja,tip,veljavnost)
    redirect('/pogodbe')


# UREDI  POGODBE
@get('/pogodbe/<id_pog>/uredi')
def uredi_zaposlenega(id_pog):
    return template(
        'urediPogodbo',
        pogodba=modeli.pogodba(id_pog)
    )

@post('/pogodbe/<id_pog>/uredi')
def uredi_pogodbo_submit(id_pog):
    id_pog = request.forms.id_pog
    tip = request.forms.tip
    veljavnost = request.forms.veljavnost
    ime = request.forms.ime
    modeli.uredi_pogodbo(id_pog,tip,veljavnost,ime)
    redirect('/pogodbe')

# ODSTRANI POGODBO
@get('/pogodbe/<id_pog>/odstrani')
def odstrani_pogodbo(id_pog):
    return template('odstraniPogodbo', pogodba=modeli.pogodba(id_pog))

@post('/pogodbe/<id_pog>/odstrani')
def odstrani_pogodbo(id_pog):
    id_pog = request.forms.id_pog
    modeli.odstrani_pogodbo(id_pog)
    redirect('/pogodbe')

############################################
# DOBAVITELJI
    
@route('/dobavitelji')
def dobavitelji():
    return template(
        'dobavitelji',seznam = modeli.seznamDobaviteljev())


@post('/dobavitelji')
def dodaj_dobavitelja():
    naziv=request.forms.naziv
    naslov=request.forms.naslov
    tel=request.forms.telefon
    email=request.forms.eposta
    davcna=request.forms.davcna
    trr=request.forms.TRR
    modeli.vnesiDobavitelja(naziv,naslov,tel,email,davcna,trr)
    redirect('/dobavitelji')
    
# UREDI DOBAVITELJA
@get('/dobavitelji/<id_dob>/uredi')
def uredi_dobavitelja(id_dob):
    return template('urediDobavitelja', dobavitelj = modeli.dobavitelj(id_dob))

@post('/dobavitelji/<id_dob>/uredi')
def uredi_dobavitelja_submit(id_dob):
    id_dob = request.forms.id_dob
    naziv = request.forms.naziv
    naslov = request.forms.naslov
    telefon = request.forms.telefon
    e_posta = request.forms.e_posta
    davcna = request.forms.davcna
    trr = request.forms.trr
    modeli.uredi_dobavitelja(id_dob, naziv,naslov,telefon,e_posta,davcna,trr)
    redirect('/dobavitelji')
    
# ODSTRANI DOBAVITELJA

@get('/dobavitelji/<id_dob>/odstrani')
def odstrani_dobavitelja(id_dob):
    return template('odstraniDobavitelja', dobavitelj = modeli.dobavitelj(id_dob),
                    pogodbe = modeli.pogodbeDobaviteljev(id_dob))

@post('/dobavitelji/<id_dob>/odstrani')
def odstrani_dobavitelja(id_dob):
    id_dob = request.forms.id_dob
    modeli.odstrani_dobavitelja(id_dob)
    redirect('/dobavitelji')
################# ######### ######### #########
    
run(debug=True)


