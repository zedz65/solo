from flask import Flask
app = Flask(__name__)
#object gets created from the class of FLask import name
from application import routes
# this needs to always be at the end or it will be an infinite loop
