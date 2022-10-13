"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Usuario, Favorite_planets, Favorite_characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.filter().all()
    result = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(result), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get(planet_id)
    if planet == None:
        return jsonify({"msg":"Planeta no existe"}), 404
    return jsonify(planet.serialize()), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.filter().all()
    result = list(map(lambda character: character.serialize(), characters))
    return jsonify(result), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Characters.query.get(character_id)
    if character == None:
        return jsonify({"msg":"Characters no existe"}), 404
    return jsonify(character.serialize()), 200

@app.route('/usuario', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.filter().all()
    result = list(map(lambda usuario: usuario.serialize(), usuarios))
    return jsonify(result), 200

@app.route('/usuario/<int:usuario_id>/favorite_planets', methods=['GET'])
def get_usuario_favorite_planets():
    usuario_favorite_planets =     Usuario.query.filter().all()


    result = list(map(lambda usuario: usuario.serialize(), usuarios))
    return jsonify(result), 200





   

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
