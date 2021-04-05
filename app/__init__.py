from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisaverysecretkey"

from app import routes
