from flask import Flask
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  

application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'

from fold.home.routes import home
from fold.meth.routes import meth
from fold.carbon_app.routes import carbon_app
from fold.users.routes import users

application.register_blueprint(home)
application.register_blueprint(meth)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

