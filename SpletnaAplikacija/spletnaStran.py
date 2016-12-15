from bottle import route, run, static_file, template
from funkcije import *
@route('/')
def hello():
    return "Pozdravljeni na spletni strani"

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='')

@route('/tabela')
def izdelki():
    return template("tabelaIzdelkov",izdelki = tabelaIzdelkov())

run(host='localhost', port=8080, debug=True)
