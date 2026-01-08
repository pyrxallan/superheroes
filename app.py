from flask import Flask, request, jsonify, make_response
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Hero Powers API</h1>'

# GET /heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_dict = [hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]
    return make_response(jsonify(heroes_dict), 200)

# GET /heroes/:id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()
    
    if not hero:
        return make_response(jsonify({"error": "Hero not found"}), 404)
    
    hero_dict = hero.to_dict(only=('id', 'name', 'super_name', 'hero_powers'))
    return make_response(jsonify(hero_dict), 200)

# GET /powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_dict = [power.to_dict(only=('id', 'name', 'description')) for power in powers]
    return make_response(jsonify(powers_dict), 200)

# GET /powers/:id
@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.filter(Power.id == id).first()
    
    if not power:
        return make_response(jsonify({"error": "Power not found"}), 404)
    
    power_dict = power.to_dict(only=('id', 'name', 'description'))
    return make_response(jsonify(power_dict), 200)

# PATCH /powers/:id
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.filter(Power.id == id).first()
    
    if not power:
        return make_response(jsonify({"error": "Power not found"}), 404)
    
    data = request.get_json()
    
    try:
        if 'description' in data:
            power.description = data['description']
        
        db.session.commit()
        
        power_dict = power.to_dict(only=('id', 'name', 'description'))
        return make_response(jsonify(power_dict), 200)
    
    except ValueError as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)

# POST /hero_powers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    try:
        new_hero_power = HeroPower(
            strength=data.get('strength'),
            power_id=data.get('power_id'),
            hero_id=data.get('hero_id')
        )
        
        db.session.add(new_hero_power)
        db.session.commit()
        
        hero_power_dict = new_hero_power.to_dict(only=(
            'id', 'hero_id', 'power_id', 'strength', 'hero', 'power'
        ))
        
        return make_response(jsonify(hero_power_dict), 201)
    
    except ValueError as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)
    except Exception as e:
        return make_response(jsonify({"errors": ["validation errors"]}), 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)