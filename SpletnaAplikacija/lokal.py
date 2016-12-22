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
@post('/pogodbe')
def dodaj_pogodbo():
    ime=request.forms.ime
    tip=request.forms.tip
    veljavnost=request.forms.veljavnost
    id_dobavitelja=request.forms.id_dobavitelja
    modeli.vnesiPogodbo(ime,id_dobavitelja,tip,veljavnost)
    redirect('/pogodbe')
    

@route('/zaposleni')
def zaposleni():
    return template(
        'zaposleni',seznam = modeli.seznamZaposlenih())

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


