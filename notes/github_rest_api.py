''' Learn to consume REST APIs using the requests module.

Github REST API is documented at:  https://developer.github.com/v3/
Requests in documented at:         http://docs.python-requests.org/en/master/

'''

import requests

root_url = 'https://api.github.com/users/'

def show_user_info(user):
    "Print a Github user's name, company, and contact information"
    url = root_url + user
    info = requests.get(url).json()
    print 'Mr %(name)s works for %(company)s.  Contact at %(email)s' % info

if __name__ == '__main__':

    show_user_info('raymondh')
