from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os
# import run_text_files


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import *

@app.route('/')
def index():
  return render_template('hello.html')

@app.route('/hello')
def hello():
  return render_template('hello.html')

@app.route('/haiku', methods=['POST'])
def haiku():
    word = request.form['word']
    processed_word = word.lower()
    from runner import generateHaiku
    result = generateHaiku(processed_word).split('\n')
    return render_template('show.html', word=processed_word, result=result)

@app.route('/train', methods=['POST'])
def train():
  update1 = request.form['update1']
  update2 = request.form['update2']
  update3 = request.form['update3']
  from training import favorUnigram, unfavorUnigram, favorLine, unfavorLine
  if update1 == "like1":
    favorLine(request.form['line1'])
  elif update1 == "dislike1":
    unfavorLine(request.form['line1'])
  if update2 == "like2":
    favorLine(request.form['line2'])
  elif update2 == "dislike2":
    unfavorLine(request.form['line2'])
  if update3 == "like3":
    favorLine(request.form['line3'])
  elif update3 == dislike3:
    unfavorLine(request.form['line3'])
  return render_template('hello.html')

if __name__ == '__main__':
  app.run()
