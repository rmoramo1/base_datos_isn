from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.TEXT(20), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # def __repr__(self):
    #     return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "mail": self.mail,
            "name": self.name
            # do not serialize the password, its a security breach
        }

class Noticias(db.Model):
    __tablename__ = 'noticias'

    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(20), nullable=False)
    top_head_line = db.Column(db.String(5), nullable=False)
    deporte = db.Column(db.String(20), nullable=False)

    dia = db.Column(db.String(8), nullable=False)
    mes = db.Column(db.String(5), nullable=False)
    year = db.Column(db.String(5), nullable=False)

    h1 = db.Column(db.String(90), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

    h2 = db.Column(db.String(90), nullable=False)
    desarrollo1 = db.Column(db.TEXT(30000), nullable=False)
    h3 = db.Column(db.String(90), nullable=False)
    desarrollo2 = db.Column(db.TEXT(30000), nullable=False)
    h4 = db.Column(db.String(90), nullable=False)
    desarrollo3 = db.Column(db.TEXT(30000), nullable=False)
    h5 = db.Column(db.String(90), nullable=False)
    desarrollo4 = db.Column(db.TEXT(30000), nullable=False)
    h6 = db.Column(db.String(90), nullable=False)
    desarrollo5 = db.Column(db.TEXT(30000), nullable=False)
    desarrollo6 = db.Column(db.TEXT(30000), nullable=False)

    imagen_principal = db.Column(db.String(90), nullable=False)
    imagen_secundaria_1 = db.Column(db.String(90), nullable=False)
    imagen_secundaria_2 = db.Column(db.String(90), nullable=False)
    imagen_secundaria_3 = db.Column(db.String(90), nullable=False)

    video_1 = db.Column(db.String(90), nullable=False)
    video_2 = db.Column(db.String(90), nullable=False)

    enlace_1 = db.Column(db.String(150), nullable=False)
    enlace_2 = db.Column(db.String(150), nullable=False)
    enlace_3 = db.Column(db.String(150), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "autor": self.autor,
            "top_head_line":self.top_head_line,
            "deporte":self.deporte,
            "dia": self.dia,
            "mes": self.mes,
            "year": self.year,
            "h1": self.h1,
            "descripcion": self.descripcion,
            "h2": self.h2,
            "desarrollo1": self.desarrollo1,
            "h3": self.h3,
            "desarrollo2": self.desarrollo2,
            "h4": self.h4,
            "desarrollo3": self.desarrollo3,
            "h5": self.h5,
            "desarrollo4": self.desarrollo4,
            "h6": self.h6,
            "desarrollo5": self.desarrollo5,
            "desarrollo6": self.desarrollo6,
            "imagen_principal": self.imagen_principal,
            "imagen_secundaria_1": self.imagen_secundaria_1,
            "imagen_secundaria_2": self.imagen_secundaria_2,
            "imagen_secundaria_3": self.imagen_secundaria_3,
            "video_1": self.video_1,
            "video_2": self.video_2,
            "enlace_1": self.enlace_1,
            "enlace_2": self.enlace_2,
            "enlace_3": self.enlace_3,
        }
class Noticias_Skins(db.Model):
    __tablename__ = 'noticias_skins'

    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.String(8), nullable=False)
    mes = db.Column(db.String(5), nullable=False)
    year = db.Column(db.String(5), nullable=False)
    skin = db.Column(db.String(20), nullable=False)
    h1 = db.Column(db.String(90), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "dia": self.dia,
            "mes": self.mes,
            "year": self.year,
            "skin": self.skin,
            "h1": self.h1,
            "descripcion": self.descripcion
        }

class Skin(db.Model):
    __tablename__ = 'skin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
