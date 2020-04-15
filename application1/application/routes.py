from application import app
from flask import render_template, request, Response
import requests


@app.route('/', methods=['GET'])   
def accountref():

    three_lower = requests.get('http://application2:5001/generator/three_lower')	 
    get_sixdig = requests.get('http://application3:5002/generator/sixdig')
 
    return render_template('home.html', title='home', three_lower=three_lower.text, get_sixdig=get_sixdig.text) 

#post is to do with service 4 as it posts the generated letters & numbers - not sure yet how to do this but think it is:
@app.route('/prize', methods=['GET', 'POST'])
def prize():

   # three_lower = requests.post(‘http://application2:5003/generator/three_lower’, data= three_lower.text) it is posting back to container for service 4? #
   # get_sixdig = requests.post(‘http://application3:5003/generator/get_sixdig’, data=get_sixdig.text)#

    return render_template('prize.html', title='Prize')



