from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(50), nullable=True)
    terrain = db.Column(db.String(50), nullable=True)
    population = db.Column(db.String(50), nullable=True)
    url_imagen = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "terrain": self.terrain,
            "population": self.population,
            "url_imagen": self.url_imagen
        }


class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(50), nullable=True)
    birth_year = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    height = db.Column(db.String(50), nullable=True)
    skin_color = db.Column(db.String(50), nullable=True)
    eye_color = db.Column(db.String(50), nullable=True)
    url_imagen = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "url_imagen": self.url_imagen
        }


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    user = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    password = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Usuario %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user": self.user,
            "email": self.email,
        }


class Favorite_planets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    planet_name = db.Column(db.String(150), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    usuario = db.relationship(Usuario)
    planets = db.relationship(Planets)

    def __repr__(self):
        return '<Favorite_planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "planet_name": self.planet_name
        }


class Favorite_characters(db.Model):
    __tablename__ = 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    character_name = db.Column(db.String(150),  nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    usuario = db.relationship(Usuario)
    characters = db.relationship(Characters)

    def __repr__(self):
        return '<Favorite_characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "character_name": self.character_name
        }
