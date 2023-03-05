from flask import render_template, Blueprint

ice=Blueprint('ice',__name__)

#Iced, en egen side for å bli iced
#@app.route("/image")
#def image():
#    return send_from_directory(".", "ice.jpeg", as_attachment=False)

#Alternativ route for å åpne bildet i en annen fane
@ice.route("/ice")
def ice_home():
    return render_template('ice.html', title='ice')
