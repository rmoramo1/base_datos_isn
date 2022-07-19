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
from models import db, User, Noticias, Noticias_Skins, Skin

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
    print(mail)
    print(password)
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


@app.route("/noticias", methods=["GET"])
def noticias():
    if request.method == "GET":
        records = Noticias.query.all()
        return jsonify([Noticias.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------


@app.route("/skin", methods=["GET"])
def skins():
    if request.method == "GET":
        records = Skin.query.all()
        return jsonify([Skin.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------


@app.route("/noticias_skins", methods=["GET"])
def noticias_skins():
    if request.method == "GET":
        records = Noticias_Skins.query.all()
        return jsonify([Noticias_Skins.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

# --------------------------post methot--------------------------------------------


@app.route('/noticias', methods=['POST'])
def createNoticias():
    autor = request.json.get("autor", None)
    top_head_line = request.json.get("top_head_line", None)
    deporte = request.json.get("deporte", None)
    dia = request.json.get("dia", None)
    mes = request.json.get("mes", None)
    year = request.json.get("year", None)
    h1 = request.json.get("h1", None)
    descripcion = request.json.get("descripcion", None)
    h2 = request.json.get("h2", None)
    desarrollo1 = request.json.get("desarrollo1", None)
    h3 = request.json.get("h3", None)
    desarrollo2 = request.json.get("desarrollo2", None)
    h4 = request.json.get("h4", None)
    desarrollo3 = request.json.get("desarrollo3", None)
    h5 = request.json.get("h5", None)
    desarrollo4 = request.json.get("desarrollo4", None)
    h6 = request.json.get("h6", None)
    desarrollo5 = request.json.get("desarrollo5", None)
    desarrollo6 = request.json.get("desarrollo6", None)
    imagen_principal = request.json.get("imagen_principal", None)
    imagen_secundaria_1 = request.json.get("imagen_secundaria_1", None)
    imagen_secundaria_2 = request.json.get("imagen_secundaria_2", None)
    imagen_secundaria_3 = request.json.get("imagen_secundaria_3", None)
    video_1 = request.json.get("video_1", None)
    video_2 = request.json.get("video_2", None)
    enlace_1 = request.json.get("enlace_1", None)
    enlace_2 = request.json.get("enlace_2", None)
    enlace_3 = request.json.get("enlace_3", None)

    # valida si estan vacios los ingresos

    # busca noticias en BBDD
    noticias = Noticias.query.filter_by(h1=h1, descripcion=descripcion).first()
    # the noticias was not found on the database
    if noticias:
        return jsonify({"msg": "noticias already exists", "status": noticias.h1}), 401
    else:
        # crea noticias nuevo
        # crea registro nuevo en BBDD de
        noticias = Noticias(
            autor=autor,
            top_head_line=top_head_line,
            deporte=deporte,
            dia=dia,
            mes=mes,
            year=year,
            h1=h1,
            descripcion=descripcion,
            h2=h2,
            desarrollo1=desarrollo1,
            h3=h3,
            desarrollo2=desarrollo2,
            h4=h4,
            desarrollo3=desarrollo3,
            h5=h5,
            desarrollo4=desarrollo4,
            h6=h6,
            desarrollo5=desarrollo5,
            desarrollo6=desarrollo6,
            imagen_principal=imagen_principal,
            imagen_secundaria_1=imagen_secundaria_1,
            imagen_secundaria_2=imagen_secundaria_2,
            imagen_secundaria_3=imagen_secundaria_3,
            video_1=video_1,
            video_2=video_2,
            enlace_1=enlace_1,
            enlace_2=enlace_2,
            enlace_3=enlace_3,
        )
        db.session.add(noticias)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200


@app.route('/noticias_skins', methods=['POST'])
def createNoticias_Skins():
    dia = request.json.get("dia", None)
    mes = request.json.get("mes", None)
    year = request.json.get("year", None)
    skin = request.json.get("skin", None)
    h1 = request.json.get("h1", None)
    descripcion = request.json.get("descripcion", None)
    # valida si estan vacios los ingresos
    # busca noticias en BBDD
    noticias_skins = Noticias_Skins.query.filter_by(
        h1=h1, descripcion=descripcion, skin=skin).first()
    # the noticias was not found on the database
    if noticias:
        return jsonify({"msg": "Noticias_Skins already exists", "status": noticias_skins.h1}), 401
    else:
        # crea noticias nuevo
        # crea registro nuevo en BBDD de
        noticias_skins = Noticias_Skins(
            dia=dia,
            mes=mes,
            year=year,
            skin=skin,
            h1=h1,
            descripcion=descripcion,
        )
        db.session.add(noticias_skins)
        db.session.commit()
        return jsonify({"msg": "Noticias Skins created successfully"}), 200


@app.route('/skin', methods=['POST'])
def create_Skins():
    name = request.json.get("name", None)
    skin = Skin.query.filter_by(name=name).first()

    if noticias:
        return jsonify({"msg": "Skin already exists", "status": skin.name}), 401
    else:
        skin = Skin(
            name=name,
        )
        db.session.add(skin)
        db.session.commit()
        return jsonify({"msg": "Skin created successfully"}), 200

# -------- put ----------------------------------------


@app.route('/noticias/<id>', methods=['PUT'])
def newsNoticias(id):
    noticias = Noticias.query.get(id)
    autor = request.json['autor']
    top_head_line = request.json['top_head_line']
    deporte = request.json['deporte']
    dia = request.json['dia']
    mes = request.json['mes']
    year = request.json['year']
    h1 = request.json['h1']
    descripcion = request.json['descripcion']
    h2 = request.json['h2']
    desarrollo1 = request.json['desarrollo1']
    h3 = request.json['h3']
    desarrollo2 = request.json['desarrollo2']
    h4 = request.json['h4']
    desarrollo3 = request.json['desarrollo3']
    h5 = request.json['h5']
    desarrollo4 = request.json['desarrollo4']
    h6 = request.json['h6']
    desarrollo5 = request.json['desarrollo5']
    desarrollo6 = request.json['desarrollo6']
    imagen_principal = request.json['imagen_principal']
    imagen_secundaria_1 = request.json['imagen_secundaria_1']
    imagen_secundaria_2 = request.json['imagen_secundaria_2']
    imagen_secundaria_3 = request.json['imagen_secundaria_3']
    video_1 = request.json['video_1']
    video_2 = request.json['video_2']
    enlace_1 = request.json['enlace_1']
    enlace_2 = request.json['enlace_2']
    enlace_3 = request.json['enlace_3']
    noticias.autor = autor
    noticias.top_head_line = top_head_line
    noticias.deporte = deporte
    noticias.dia = dia
    noticias.mes = mes
    noticias.year = year
    noticias.h1 = h1
    noticias.descripcion = descripcion
    noticias.h2 = h2
    noticias.desarrollo1 = desarrollo1
    noticias.h3 = h3
    noticias.desarrollo2 = desarrollo2
    noticias.h4 = h4
    noticias.desarrollo3 = desarrollo3
    noticias.h5 = h5
    noticias.desarrollo4 = desarrollo4
    noticias.h6 = h6
    noticias.desarrollo5 = desarrollo5
    noticias.desarrollo6 = desarrollo6
    noticias.imagen_principal = imagen_principal
    noticias.imagen_secundaria_1 = imagen_secundaria_1
    noticias.imagen_secundaria_2 = imagen_secundaria_2
    noticias.imagen_secundaria_3 = imagen_secundaria_3
    noticias.video_1 = video_1
    noticias.video_2 = video_2
    noticias.enlace_1 = enlace_1
    noticias.enlace_2 = enlace_2
    noticias.enlace_3 = enlace_3

    db.session.commit()
    return jsonify({"msg": "noticias edith successfully"}), 200


@app.route('/noticias_skins/<id>', methods=['PUT'])
def newsNoticias_Skins(id):
    noticias_skins = Noticias_Skins.query.get(id)
    dia = request.json['dia']
    mes = request.json['mes']
    year = request.json['year']
    skin = request.json['skin']
    h1 = request.json['h1']
    descripcion = request.json['descripcion']
    noticias_skins.dia = dia
    noticias_skins.mes = mes
    noticias_skins.year = year
    noticias_skins.skin = skin
    noticias_skins.h1 = h1
    noticias_skins.descripcion = descripcion

    db.session.commit()
    return jsonify({"msg": "Noticias_Skins edith successfully"}), 200


@app.route('/skin/<id>', methods=['PUT'])
def Skin(id):
    skin = Skin.query.get(id)
    name = request.json['name']
    skin.name = name

    db.session.commit()
    return jsonify({"msg": "Skin edith successfully"}), 200

# -------- delete ----------------------------------------


@app.route("/noticias/<id>", methods=["DELETE"])
def noticias_delete(id):
    noticias = Noticias.query.get(id)
    db.session.delete(noticias)
    db.session.commit()
    return "Noticia was successfully deleted"


@app.route("/noticias_skins/<id>", methods=["DELETE"])
def noticias_skin_delete(id):
    noticias_skins = Noticias_Skins.query.get(id)
    db.session.delete(noticias_skins)
    db.session.commit()
    return "noticias_skins was successfully deleted"


@app.route("/skin/<id>", methods=["DELETE"])
def skin_delete(id):
    skin = Skin.query.get(id)
    db.session.delete(skin)
    db.session.commit()
    return "skin was successfully deleted"
