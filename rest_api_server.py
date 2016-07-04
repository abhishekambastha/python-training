'Build small webapps and rest api using micro-webframeworks'
from bottle import route, run
from bottle import response, request
import time
import os
import algebra

@route('/')
def welcome():
    response.content_type = 'text/plain'
    return 'Howdy!\n'

@route('/now')
def show_time():
    response.content_type = 'text/plain'
    return time.ctime()

@route('/Files')
def display_files():
    return {'dir': 'notes', 'time': time.time(), 'files':os.listdir('notes')}

@route('/upper/<word>')
def upppercase_service(word=''):
    response.content_type = 'text/plain'
    return word.upper()

@route('/query')
def display_query():
    print request.query.items()
    return 'XXX'

@route('/area/traingle')
def triangle_area_service():
    base = float(request.query.get('base', '0'))
    height = float(request.query.get('height', '0'))
    print 'Tri', base, height
    return 'XXX'

@route('/quadritic')
def solve_eq():
    a = float(request.query.get('a', '0'))
    b = float(request.query.get('b', '0'))
    c = float(request.query.get('c', '0'))
    return dict(zip(('x1', 'x2'), algebra.quadratic(a, b, c)))

htm = '''
<html>
  <head>
    <title>Quadratic Solver</title>
  </head>
  <body>
    <h2> Input the Coefficients of a Quadratic Equation </h2>
    <hr>
    <form method="post" action="/quad">
      <label>a <input name="a" type="text"> </label>
      <label>b <input name="b" type="text"> </label>
      <label>c <input name="c" type="text"> </label>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
'''

@route('/quad')
def inp():
    return htm

@post('/quat')
def html_quad():
    a = float(request.form.get('a', 0.0))
    b = float(request.form.get('a', 0.0))
    c = float(request.form.get('a', 0.0))
    print a, b, c

def show_network_interfaces():
    pass

 __name__ == '__main__':

    run(host='localhost', port=8080, debug=True)

