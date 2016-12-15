from bottle import route, run, template

@route('/')
def index():
    return 'Pozdravljeni na spletni strani'

run(reloader=True,debug=True)
