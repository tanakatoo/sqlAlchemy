from flask import Flask, request, jsonify, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///pets_db'
app.config['SQLALCHEMY_ECHO'] = True #so we know what went wrong, prints out actual queries being run
app.config['SECRET_KEY'] = 'ohsosecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug=DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    return render_template('home.html')