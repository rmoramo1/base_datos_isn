"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Upload

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = 'JEKAROYCAR'
jwt = JWTManager(app)

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

# obtener usuario de base de datos y crea token

# obtener usuario de base de datos y crea token


@app.route('/login', methods=['POST'])
def login():
    name = request.json.get("name", None)
    mail = request.json.get("mail", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(mail=mail, password=password).first()
    # valida si estan vacios los ingresos
    if user is None:
        return jsonify({"msg": "Bad mail or password"}), 401
    # crear token login

    access_token = create_access_token(identity=mail)
    return jsonify({"token": access_token, "username": user.name})

# obtiene usuario----------------------------------------


@app.route("/user", methods=["GET"])
def user():
    if request.method == "GET":
        records = User.query.all()
        return jsonify([User.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------


@app.route("/upload", methods=["GET"])
def Upload_GET():
    if request.method == "GET":
        records = Upload.query.all()
        return jsonify([Upload.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

# --------------------------post methot--------------------------------------------


# @app.route('/upload', methods=['POST1'])
# def createUpload():

#     file = request.files["file"]


#     name = request.json.get("name", None)
#     mimetype = request.json.get("mimetype", None)

#     like = request.json.get("like", None)
#     dislike = request.json.get("dislike", None)
#     comentario = request.json.get("comentario", None)
#     usuario = request.json.get("usuario", None)

#     upload = Upload.query.filter_by(image=image, name=name).first()
#     # the noticias was not found on the database
#     if upload:
#         return jsonify({"msg": "stats_punting_player_nfl already exists", "name": upload.name}), 401
#     else:
#         # filename = secure_filename(image.filename)
#         # mimetype = image.mimetype
#         upload = Upload(
#             name=file.filename,
#             image=file.read(),
#             mimetype=mimetype,

#             like=like,
#             dislike=dislike,
#             comentario=comentario,
#             usuario=usuario
#         )
#     db.session.add(upload)
#     db.session.commit()
#     return jsonify({"msg": "image created successfully"}), 200



@app.route('/upload', methods=['POST1'])
def createUpload():

    file = request.files["file"]

    upload = Upload(
        name=file.filename,
        image=encode(file.read()),
        mimetype=mimetype,

        like=like,
        dislike=dislike,
        comentario=comentario,
        usuario=usuario
    )
    db.session.add(upload)
    db.session.commit()
#     return jsonify({"msg": "image created successfully"}), 200


# -------- put ----------------------------------------

@app.route('/upload/<id>', methods=['PUT'])
def newsUpload(id):
    upload = Upload.query.get(id)

    image = request.json['image']
    name = request.json['name']
    mimetype = request.json['mimetype']
    like = request.json['like']
    dislike = request.json['dislike']
    comentario = request.json['comentario']
    usuario = request.json['usuario']

    upload.image = image
    upload.name = name
    upload.mimetype = mimetype
    upload.like = like
    upload.dislike = dislike
    upload.comentario = comentario
    upload.usuario = usuario

    db.session.commit()
    return jsonify({"msg": "Upload edith successfully"}), 200


# -------- delete ----------------------------------------


@app.route("/upload/<id>", methods=["DELETE"])
def upload_delete(id):
    upload = Upload.query.get(id)
    db.session.delete(upload)
    db.session.commit()
    return "Noticia was successfully deleted"
