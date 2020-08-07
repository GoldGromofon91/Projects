from flask import Flask
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Status</a>"

@app.route("/status")
def status():
    return {'status': random.randint(0,1),
            'name': 'Charlse',
            'date':datetime.now()
            }


app.run()