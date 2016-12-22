#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, get, post, redirect
import modeli

@route('/')
def domov():
    return template(
        'domov')

@route('/tabela')
def tabela():
    return template("tabelaIzdelkov",izdelki = modeli.tabelaIzdelkov())

@route('/izdelki')
def izdelki():
    return template(
        'izdelki')

@route('/pogodbe')
def pogodbe():
    return template(
        'pogodbe',seznam=modeli.seznamPogodb())

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

@route('/racun')
def racun():
    return template(
        'racun',seznam = modeli.izdaniRacuni())

@get('/izdelki')
def forma():
    return template('izdelki')

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



run(debug=True)


