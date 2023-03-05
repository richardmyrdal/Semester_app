from flask import render_template, Blueprint

meth=Blueprint('meth',__name__)

#NB! Jeg har forkortet methodology til meth
@meth.route('/meth')
def meth_home():
  return render_template('meth.html', title='meth')