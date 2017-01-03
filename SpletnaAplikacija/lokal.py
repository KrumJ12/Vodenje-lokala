#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, get, post, redirect
import modeli

@route('/')
def domov():
    return template(
        'domov',imena=modeli.imeInCenaIzdelkov())


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

@get('/oseba/<oseba>/uredi')
def uredi_osebo(oseba):
    return template(
        'urediOsebo',
        oseba=modeli.oseba(oseba)
    )

@post('/oseba/<oseba>/uredi')
def uredi_osebo_submit(oseba):
    oseba = request.forms.oseba
    ime = request.forms.ime
    priimek = request.forms.priimek
    datum_rojstva = request.forms.datum_rojstva
    e_posta = request.forms.e_posta
    funkcija = request.forms.funkcija
    datum_zaposlitve = request.forms.datum_zaposlitve
    telefon = request.forms.telefon
    prebivalisce = request.forms.prebivalisce
    modeli.uredi_osebo(oseba, ime, priimek,datum_rojstva,e_posta,funkcija,datum_zaposlitve,telefon,prebivalisce)
    redirect('/zaposleni')



run(debug=True)


