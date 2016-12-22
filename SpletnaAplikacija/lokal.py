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
        'pogodbe')

@route('/zaposleni')
def zaposleni():
    return template(
        'zaposleni',seznam = modeli.seznamZaposlenih())

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
    return template('izdelki.tpl')



@post('/izdelki')
def preberi():
    ime = request.forms.get('ime')
    zaloga  = request.forms.get('zaloga')
    tip = request.forms.get('tip')
    cena  = request.forms.get('cena')

    print(ime,zaloga,tip,cena)
    redirect('/izdelki')
    

run(debug=True)
