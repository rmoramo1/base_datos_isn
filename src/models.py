from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    user = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    born = db.Column(db.String(50), nullable=False)
    subscription = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # def __repr__(self):
    #     return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mail": self.mail,
            "user": self.user,
            "country": self.country,
            "born": self.born,
            "subscription": self.subscription,
            # do not serialize the password, its a security breach
        }


class Upload(db.Model):
    __tablename__ = 'upload'

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(50),unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    mimetype = db.Column(db.String(50), nullable=False)

    like = db.Column(db.String(20), nullable=False)
    dislike = db.Column(db.String(20), nullable=False)
    comentario = db.Column(db.String(1500), nullable=False)
    usuario = db.Column(db.String(20), nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mimetype": self.mimetype,
            "like": self.like,
            "dislike": self.dislike,
            "comentario": self.comentario,
            "usuario": self.usuario
        }

class Perfil_Tipster(db.Model):
    __tablename__ = 'perfil_tipster'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # def __repr__(self):

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "description": self.description,
            # do not serialize the password, its a security breach
        }

class Picks_Tipster(db.Model):
    __tablename__ = 'picks_tipster'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    units = db.Column(db.String(5), nullable=False)
    deporte = db.Column(db.String(40), nullable=False)
    equipos = db.Column(db.String(500), nullable=False)
    linea = db.Column(db.String(500), nullable=False)
    estado = db.Column(db.String(40), nullable=False)
    resultado = db.Column(db.String(40), nullable=False)

    # def __repr__(self):
    #     return '<tipo %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "fecha": self.fecha,
            "tipo": self.tipo,
            "units": self.units,
            "deporte": self.deporte,
            "equipos": self.equipos,
            "linea": self.linea,
            "estado": self.estado,
            "resultado": self.resultado,
            # do not serialize the password, its a security breach
        }