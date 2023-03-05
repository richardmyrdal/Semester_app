from flask import render_template, Blueprint
#importer random for å kunne velge randome navn
import random

home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_home():
  names = ["Richard", "Alex", "Simen", "Kaja" ]
  name = random.choice(names)
  return render_template('home.html', name=name)



