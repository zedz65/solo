from application import app
from flask import request, Response
import random
import math
from random import randint



@app.route('/generator/sixdig', methods = ['GET'])
def get_sixdig():
    return Response((str(random.randint(100000,999999))), mimetype='text/plain')

@app.route('/generator/eightdig', methods = ['GET'])
def get_eightdig():
    return Response((str(random.randint(10000000,99999999))), mimetype='text/plain')

print(get_sixdig())
print(get_eightdig())

