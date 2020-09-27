from flask import Flask;
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.secret_message
import codeitsuisse.routes.healthcheck
import codeitsuisse.routes.sort
import codeitsuisse.routes.geometry
import codeitsuisse.routes.salad
import codeitsuisse.routes.fruit
import codeitsuisse.routes.inventory
import codeitsuisse.routes.clean
import codeitsuisse.routes.olympiad
import codeitsuisse.routes.cluster
import codeitsuisse.routes.gmo
import codeitsuisse.routes.scribe
import codeitsuisse.routes.socialdistancing
import codeitsuisse.routes.contact_tracing

