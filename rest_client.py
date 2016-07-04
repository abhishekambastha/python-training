import requests

root_url = 'http://localhost:8080/quadritic'

def solve_quadritic(d):
    string = '?' + 'a='+ d['a'] + '&' + 'b='+  d['b'] + '&' + 'c=' + d['c']
    url = root_url + string
    info = requests.get(url)
    print info.text

if __name__ == '__main__':

    show_user_info('raymondh')
