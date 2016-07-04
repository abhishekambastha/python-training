'''Goal:  Learn to build small web apps and REST APIs using micro-webframeworks

CDN:                 Content Delivery Network brings selected static data closer to the user

Balancer/Manager:    Nginx        Varnish       HAProxy

Webserver:           wsgiref       apache       twisted tornado          gunicorn             
                     (simple)     (threads)     (non-blocking async)     (processes -> preforking)

Micro-webframework:  bottle, flask, cherrypy,  .....            django, pylons, zope
                     [--- lightweight or micro ---]            [--- heavyweight ---]

This file (links)    import bottle
                     @route('/quad')
                     def quad():
                         return someapp.quad()

Application:         algebra.py            <== Standalone Python Package

Shared DataStore     memcached                   sqlite   mysql postgres oracle     mongodb couchdb cassanda
                     (lightweight key/value)     (local)  (bigger sql acid)              (no sql db)
                                                                                       eventual consistency
'''

# Simple challenge:  add a signature to your cookies
# http://pythonhosted.org/itsdangerous/

# Another challenge:
# * Make a simple login form modeled after quadratic_input_html
# * Get the username and password
# * session_id = ''.join([random.choice(string.letters) for i in range(30)])
# * If it matches, send a timestamped, signed random session cookie
# Use that session_id to allow access to /netstat and /files

from bottle import route, run, post         # route() is like register().   run() is like interpret().
from bottle import response, request
import time, os
import algebra, monkey_patching
import subprocess

@route('/')
def welcome():
    response.content_type = 'text/plain'
    return 'Howdy!\nI am from Texas!\n'

@route('/now')
def show_time():
    response.content_type = 'text/plain'
    return time.ctime()

@route('/files')
def display_files():
    return {'dirname': 'notes',
            'time': time.time(),
            'files':os.listdir('notes')}

@route('/netstat')
def show_network_interfaces():
    response.content_type = 'text/plain'
    return subprocess.check_output(['netstat', '-i'])

@route('/upper/<word>')
def uppercase_service(word=''):
    response.content_type = 'text/plain'
    return word.upper()

@route('/area/triangle')
def triangle_area_service():
    '''
        >>> requests.get('http://localhost:8080/area/triangle',  dict(base=400, height=50)).json()['area']
        10000.0
    '''
    base = float(request.query.get('base', '0'))
    height = float(request.query.get('height', '0'))
    area = algebra.area_triangle(base, height)
    return dict(base=base, height=height, area=area,
                service='/area/triangle')

# localhost:8080/quadratic?a=8&b=22&c=15

quad_results_html_template = '''\
<html>
<head>
<title> Quadratic </title>
</head>
<body>
<h1> Quadratic solution </h1>
<hr>
<ul>
</ul>
  <li> a: %f </li>
  <li> b: %f </li>
  <li> c: %f </li>
  <li> x1: %f + %fi </li>
  <li> x2: %f + %fi  </li>
</body>
</hmtl>
'''

@route('/quadratic')
def quadratic_solver():
    a = float(request.query.get('a', '0.0'))
    b = float(request.query.get('b', '0.0'))
    c = float(request.query.get('c', '0.0'))
    x1, x2 = algebra.quadratic(a, b, c)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        return quad_results_html_template % (
            a, b, c, x1.real, x1.imag, x2.real, x2.imag)

    return dict(service='/quadratic', a=a, b=b, c=c,
                x1=dict(real=x1.real, imag=x1.imag),
                x2=dict(real=x2.real, imag=x2.imag))

quadratic_input_html = '''\
<html>
  <head>
    <title>Quadratic Solver</title>
  </head>
  <body>
    <h2> Input the Coefficients of a Quadratic Equation </h2>
    <hr>
    <form method="post" action="/quad">
      <label>a <input name="a" type="text", value="%s"> </label>
      <label>b <input name="b" type="text", value="%s"> </label>
      <label>c <input name="c" type="text", value="%s"> </label>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
'''

@route('/quad')
def quadratic_html_service():
    a = request.get_cookie('a', '0.0')
    b = request.get_cookie('b', '0.0')
    c = request.get_cookie('c', '0.0')
    return quadratic_input_html % (a, b, c)

@post('/quad')
def html_quadratic_solver():
    a = float(request.forms.get('a', '0.0'))
    b = float(request.forms.get('b', '0.0'))
    c = float(request.forms.get('c', '0.0'))
    x1, x2 = algebra.quadratic(a, b, c)
    response.set_cookie('a', str(a))
    response.set_cookie('b', str(b))
    response.set_cookie('c', str(c))
    return quad_results_html_template % (
        a, b, c, x1.real, x1.imag, x2.real, x2.imag)
    
if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True)    
