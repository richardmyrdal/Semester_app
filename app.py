#Importerer flask
from flask import Flask, render_template
#For def image, ice
from flask import send_from_directory
#importer random for å kunne velge randome navn
import random
app = Flask(__name__)

#NB! Jeg har brukt forkortelsen App for application
#Lager et nettverk av routes
@app.route('/')
@app.route('/home')

def home():
    names = ["Richard", "Alex", "Simen", "Kaja" ]
    name = random.choice(names)
    return render_template('home.html', title='home', name=name)

@app.route('/meth') #Forkortelse meth=methodology
def meth():
    return render_template('meth.html', title='meth')

@app.route('/carbon_app')
def carbon_app():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')


@app.route('/app_calculator')
def app_calculator():
    return render_template('app_calculator.html', title='app_calculator')

#Iced, en egen side for å bli iced
#@app.route("/image")
#def image():
#    return send_from_directory(".", "ice.jpeg", as_attachment=False)

#Alternativ route for å åpne bildet i en annen fane
@app.route("/image")
def image():
    html = "<html><head><title>Image</title><style>body{background-color: white; text-align: center;}</style></head><body><h1>Du har blitt ICED!</h1><img class='ice' src='/static/images/ice.jpeg'/></body></html>"
    return html

#Egen side for å håndtere errors (Må lage 404 siden) funker ikke nå ikke laget
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', 404)

if __name__ == '__main__':
    app.run(debug = True)



