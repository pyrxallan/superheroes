from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models after db initialization
from models import Hero, Power, HeroPower

@app.route('/')
def index():
    return {'message': 'Superheroes API'}

if __name__ == '__main__':
    app.run(port=5555, debug=True)
