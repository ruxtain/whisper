#!/home/michael/anaconda3/bin/python

from flask import Flask 
from flask import render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('whisper.html')

with app.test_request_context():
    url_for('static', filename='vue.js')
    url_for('static', filename='style.css')