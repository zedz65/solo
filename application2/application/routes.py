from application import app
from flask import request, Response
import string
import random
from random import randint


#route for three lowercase letters using get method 
@app.route('/generator/three_lower', methods = ['GET'])
def three_lower():
    result = ''.join(random.choices(string.ascii_lowercase,k=3))
    return Response(result, mimetype='text/plain')


#route for two uppercase letters for random generator using get
@app.route('/generator/two_upper', methods = ['GET'])
def two_upper():
    result = ''.join(random.choices(string.ascii_uppercase,k=2))
    return Response(result, mimetype='text/plain')

