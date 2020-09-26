from flask import Flask;
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.secret_message
import codeitsuisse.routes.healthcheck
import codeitsuisse.routes.sort
import codeitsuisse.routes.geometry
import codeitsuisse.routes.salad