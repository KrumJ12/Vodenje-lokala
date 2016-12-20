from bottle import route, run, template
import modeli
import cgi, cgitb

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

@route('/preberi')
def preberi():
    # Create instance of FieldStorage 
    form = cgi.FieldStorage() 

    # Get data from fields
    ime = form.getvalue('ime')
    zaloga  = form.getvalue('zaloga')
    tip = form.getvalue('tip')
    cena  = form.getvalue('cena')

    print(ime,zaloga,tip,cena)
    
    

run(debug=True)
