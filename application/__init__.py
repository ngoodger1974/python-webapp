from flask import Flask
from flask_wtf.csrf import CSRFProtest

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

from application import routes


