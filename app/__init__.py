from flask import Flask
from .config import Config
from .models import db
from .routes import orders

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(orders.bp)
db.init_app(app)

