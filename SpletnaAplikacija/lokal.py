from bottle import route, run, template
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

@route('/zaposleni')
def zaposleni():
    return template(
        'zaposleni')

@route('/dobavitelji')
def dobavitelji():
    return template(
        'dobavitelji')

@route('/racun')
def racun():
    return template(
        'racun')

run(debug=True)
