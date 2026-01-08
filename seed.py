from app import app, db
from models import Hero, Power, HeroPower
import random

with app.app_context():
    db.create_all()