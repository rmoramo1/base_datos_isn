from flask_sqlalchemy import SQLAlchemy, request

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


class Upload(db.Model):
    __tablename__ = 'upload'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)
    name = db.Column(db.TEXT, nullable=False)
    mimetype = db.Column(db.TEXT, nullable=False)

    like = db.Column(db.String(20), nullable=False)
    dislike = db.Column(db.String(20), nullable=False)
    comentario = db.Column(db.String(1500), nullable=False)
    usuario = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "image": self.image,
            "name": self.name,
            "mimetype": self.mimetype,
            "like": self.like,
            "dislike": self.dislike,
            "comentario": self.comentario,
            "usuario": self.usuario
        }
