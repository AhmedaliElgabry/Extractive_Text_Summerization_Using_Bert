from flask import Flask,flash, request, jsonify, render_template,redirect,send_from_directory,session, url_for
import flask
from werkzeug.utils import secure_filename
import pickle
import requests
from io import BytesIO
import spacy
import glob
from summarizer import Summarizer
import numpy as np
#-------------------------





app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
      text = request.form['message']
      body = text
      model = Summarizer()
      result = model(body, min_length=100)
      full = ''.join(result)
      print(full)
     
      return redirect(url_for('success', name=full))

    else:
      return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    print('summery: ',name)
    return render_template('index.html',data = name)

if __name__ == "__main__":
    app.run(debug=True)