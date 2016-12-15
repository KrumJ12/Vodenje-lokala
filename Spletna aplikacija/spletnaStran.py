from bottle import route, run, static_file

@route('/')
def hello():
    return "Pozdravljeni na spletni strani"

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='')

run(host='localhost', port=8080, debug=True)
