from flask import render_template, Blueprint

ice=Blueprint('ice',__name__)

#Iced, en egen side for å bli iced
#@app.route("/image")
#def image():
#    return send_from_directory(".", "ice.jpeg", as_attachment=False)

#Alternativ route for å åpne bildet i en annen fane
@ice.route("/image")
def image_home():
    html = "<html><head><title>Image</title><style>body{background-color: white; text-align: center;}</style></head><body><h1>Du har blitt ICED!</h1><img class='ice' src='/static/images/ice.jpeg'/></body></html>"
    return html