import os
from flask import Flask
from App import operations

app = Flask(__name__)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.register_blueprint(operations.bp)