from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)
import routes