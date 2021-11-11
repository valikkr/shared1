import os
import random
import string
import time
from string import ascii_letters, punctuation, digits
from random import choices

import flask
from flask import Flask, request

app = Flask(__name__)


@app.route('/whoami')
def whoami():
    ip_adress = flask.request.remote_addr
    browser = request.user_agent.browser
    server_time = time.strftime('%A %B, %d %Y %H:%M:%S')
    return f"Browser: {browser}; Ip Adress: {ip_adress}; Server time: {server_time}."


@app.route('/source_code')
def source_code():
    f = open('app.py', 'r')
    text = str(f.readlines())
    f.close()
    print(os.getcwd())

    return text


def get_random_str(length, specials, numbers):
    error = None
    try:
        length = int(length)
    except ValueError:
        return None, 'Length should be int'

    if numbers not in (None, '1'):
        return None, 'Numbers should be 0 or 1'

    if specials not in (None, '1'):
        return None, 'Specials should be 0 or 1'

    if length < 1 or length > 100:
        return None, 'Length should be in [1, 100]'
    chars = string.ascii_letters

    if specials:
        chars += string.punctuation
    if numbers:
        chars += string.digits

    res = ''
    if length and not error:
        res = ''.join(random.choices(chars, k=length))

    return res, None


@app.route('/')
def index():
    length = request.args.get('length', -1)
    specials = request.args.get('specials')
    numbers = request.args.get('numbers')

    res, error = get_random_str(length, specials, numbers)

    return f"""
    <html>
        <head>
            <title>{res if res else 'Random generator'}</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <style>
            h5 {{
            text-align:right
            
            }}
            body {{
            background-image: url(https://images2.minutemediacdn.com/image/upload/c_crop,h_1349,w_2400,x_0,y_138/v1628703164/shape/mentalfloss/649273-youtube-rick_astley.jpg?itok=8JRk0Avu)
            }}
            </style>
        </head>
        <body>
            <h1> My web page </h1>
        <form method='GET'>
            length: <input type='number' name='length' value='{length}'/><br/>
            specials: <input type='checkbox' name='specials' value='1'/><br/>
            numbers: <input type='checkbox' name = 'numbers' value='1'/><br/>
            <input type='submit'>
            <h2>Results: {res} </h2>
            <font text='red'>{error if error else ''}</font>
            <h5> Newer gonna {res} you up, <br/> newer gonna {res} you down</h5>
            
        </form
        </body>
    </html>
    
    
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

