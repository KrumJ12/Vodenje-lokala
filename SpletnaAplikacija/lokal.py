#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, get, post, redirect
import modeli

@route('/')
def domov():
    izdelki = [int(x) for x in request.query.getall('id')]

    # seznam rabimo pri vnosu racuna
    global sez
    sez = izdelki
    return template(
        'domov',
        imena=modeli.tabIzdelkov(),
        izdelki = izdelki,
        stari_niz='&'.join('id={}'.format(x) for x in izdelki)
    )

@route('/vnesi')
def vnesiRacun():
    znesek = round(modeli.izracunajZnesek(sez),2)
    if znesek == 0:
        redirect('/')
        return
    modeli.vnesiRacun(znesek)
    redirect('/racun')

@route('/izdelki')
def izdelki():
    return template('izdelki',imena=modeli.seznamImenovIzdelkov(),
                    izdelki = modeli.tabelaIzdelkov())

@post('/spremeniCeno')
def spremeniCeno():
    ime=request.forms.izdelek
    cena=float(request.forms.cena)
    modeli.spremeniCeno(ime,cena)
    redirect('/izdelki')

@post('/dodajZalogo')
def dodaj_Zalogo():
    ime=request.forms.izdelek
    zaloga=int(request.forms.zaloga)
    modeli.dodajZalogo(ime,zaloga)
    redirect('/izdelki')

@route('/pogodbe')
def pogodbe():
    return template(
        'pogodbe',seznam=modeli.seznamPogodb(),imena=modeli.imenaDobaviteljev())

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
    

@route('/zaposleni')
def zaposleni():
    return template(
        'zaposleni',seznam = modeli.seznamZaposlenih())

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
    

@route('/racun')
def racun():
    return template(
        'racun',seznam = modeli.izdaniRacuni())

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
######### ######### ######### #########
# UREDI ZAPOSLENEGA
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
    datum_zaposlitve = request.forms.datum_zaposlitve
    telefon = request.forms.telefon
    prebivalisce = request.forms.prebivalisce
    modeli.uredi_zaposlenega(id_zap, ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce)
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
# UREDI, ODSTRANI DOBAVITELJA
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


