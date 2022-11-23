"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from flask_migrate import Migrate
from flask_swagger import swagger
from werkzeug.utils import secure_filename

from admin import setup_admin
from models import Perfil_Tipster, Picks_Tipster, Upload, User, db
from utils import APIException, generate_sitemap

UPLOAD_FOLDER = '/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = 'JEKAROYCAR'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

jwt = JWTManager(app)

app.secret_key = "roycjs"

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_PATH'] = 'uploads'

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Handle/serialize errors like a JSON object

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code
# generate sitemap with all your endpoints

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/')
def sitemap(): 
    return generate_sitemap(app) 

@app.route('/login', methods=['POST'])
def login():
    user = request.json.get("user", None)
    password = request.json.get("password", None)
    print(user)
    print(password)
    usuario = User.query.filter_by(user=user, password=password).first()
    # valida si estan vacios los ingresos
    if usuario is None:
        return jsonify({"msg": "Bad mail or password"}), 401
    # crear token login

    access_token = create_access_token(identity=user)
    return jsonify({"token": access_token, "username": usuario.user})

# obtiene usuario----------------------------------------


@app.route("/user", methods=["GET"])
def user():
    if request.method == "GET":
        records = User.query.all()
        return jsonify([User.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------


@app.route("/perfil_tipster", methods=["GET"])
def perfil_tipster():
    if request.method == "GET":
        records = Perfil_Tipster.query.all()
        return jsonify([Perfil_Tipster.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------


@app.route("/picks_tipster", methods=["GET"])
def picks_tipster():
    if request.method == "GET":
        records = Picks_Tipster.query.all()
        return jsonify([Picks_Tipster.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------
@app.route("/upload", methods=["GET"])
def _upload():
    if request.method == "GET":
        records = Upload.query.all()
        return jsonify([Upload.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------

@app.route('/upload', methods=['POST'])
def upload():

    img = request.files['img']
    if not img:
        return "no img",400
    name = name
    mimetype = mimetype

    upload =Upload(img=img.read(),mimetype=mimetype, name=file.name)
    db.session.add(upload)
    db.session.commit()
    return jsonify({"msg": "mimetype created successfully"}), 200


    # mimetype = img.mimetype
    # name = request.json.get("name", None)
    # like = request.json.get("like", None)
    # dislike = request.json.get("dislike", None)
    # comentario = request.json.get("comentario", None)
    # usuario = request.json.get("usuario", None)

    # # busca mimetype en BBDD
    # upload = Upload.query.filter_by(
    #     name=name, mimetype=mimetype).first()
    # # the mimetype was not found on the database
    # if upload:
    #     return jsonify({"msg": "upload already exists", "name": upload.name}), 401
    # else:
    #     # crea mimetype nuevo
    #     # crea registro nuevo en BBDD de
    #     upload = Upload(
    #         name=name,
    #         img=img.read(),
    #         mimetype=mimetype,
    #         like=like,
    #         dislike=dislike,
    #         comentario=comentario,
    #         usuario=usuario,
    #     )
    # db.session.add(upload)
    # db.session.commit()
    # return jsonify({"msg": "mimetype created successfully"}), 200
            
# --------------------------post methot--------------------------------------------


@app.route('/user', methods=['POST'])
def createUser():
    name = request.json.get("name", None)
    mail = request.json.get("mail", None)
    user = request.json.get("user", None)
    country = request.json.get("country", None)
    born = request.json.get("born", None)
    password = request.json.get("password", None)
    subscription = request.json.get("subscription", None)

    # busca user en BBDD
    user_rc = User.query.filter_by(
        mail=mail, name=name, user=user).first()
    # the user was not found on the database
    if user_rc:
        return jsonify({"msg": "user_rc already exists", "name": user_rc.name}), 401
    else:
        # crea user nuevo
        # crea registro nuevo en BBDD de
        user_rc = User(
            name=name,
            mail=mail,
            user=user,
            country=country,
            born=born,
            subscription=subscription,
            password=password
        )
        db.session.add(user_rc)
        db.session.commit()
        return jsonify({"msg": "user created successfully"}), 200


# -------------------------------------------------------------------------
@app.route('/picks_tipster', methods=['POST'])
def createPicks_tipster():
    name = request.json.get("name", None)
    fecha = request.json.get("fecha", None)
    tipo = request.json.get("tipo", None)
    units = request.json.get("units", None)
    deporte = request.json.get("deporte", None)
    equipos = request.json.get("equipos", None)
    linea = request.json.get("linea", None)
    estado = request.json.get("estado", None)
    resultado = request.json.get("resultado", None)

    # busca tipo en BBDD
    picks_tipster = Picks_Tipster.query.filter_by(
        fecha=fecha, name=name, tipo=tipo).first()
    # the tipo was not found on the database
    if picks_tipster:
        return jsonify({"msg": "picks_tipster already exists", "name": picks_tipster.name}), 401
    else:
        # crea tipo nuevo
        # crea registro nuevo en BBDD de
        picks_tipster = Picks_Tipster(
            name=name,
            fecha=fecha,
            tipo=tipo,
            units=units,
            deporte=deporte,
            linea=linea,
            equipos=equipos,
            estado=estado,
            resultado=resultado,
        )
        db.session.add(picks_tipster)
        db.session.commit()
        return jsonify({"msg": "pick created successfully"}), 200
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


@app.route('/perfil_tipster', methods=['POST'])
def create_Perfil_Tipster():
    name = request.json.get("name", None)
    title = request.json.get("title", None)
    description = request.json.get("description", None)
    password = request.json.get("password", None)

    # busca description en BBDD
    perfil_tipster = Perfil_Tipster.query.filter_by(
        title=title, name=name, description=description).first()
    # the description was not found on the database
    if perfil_tipster:
        return jsonify({"msg": "perfil_tipster already exists", "name": perfil_tipster.name}), 401
    else:
        # crea description nuevo
        # crea registro nuevo en BBDD de
        perfil_tipster = Perfil_Tipster(
            name=name,
            title=title,
            description=description,
            password=password,
        )
        db.session.add(perfil_tipster)
        db.session.commit()
        return jsonify({"msg": "pick created successfully"}), 200
# -------------------------------------------------------------------------


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

# ----------------------------------------------------------------------


@app.route('/user/<id>', methods=['PUT'])
def editUser(id):
    user_rp = User.query.get(id)

    name = request.json['name']
    mail = request.json['mail']
    user = request.json['user']
    country = request.json['country']
    born = request.json['born']
    subscription = request.json['subscription']
    password = request.json['password']

    user_rp.name = name
    user_rp.mail = mail
    user_rp.user = user
    user_rp.country = country
    user_rp.born = born
    user_rp.subscription = subscription
    user_rp.password = password

    db.session.commit()
    return jsonify({"msg": "user edith successfully"}), 200

# ----------------------------------------------------------------------


@app.route('/perfil_tipster/<id>', methods=['PUT'])
def editPerfil_tipster(id):
    perfil_tipster = Perfil_Tipster.query.get(id)

    name = request.json['name']
    title = request.json['title']
    description = request.json['description']
    password = request.json['password']

    perfil_tipster.name = name
    perfil_tipster.title = title
    perfil_tipster.description = description
    perfil_tipster.password = password

    db.session.commit()
    return jsonify({"msg": "Tipster edith successfully"}), 200

# ----------------------------------------------------------------------


@app.route('/picks_tipster/<id>', methods=['PUT'])
def editPicks_tipster(id):
    picks_tipster = Picks_Tipster.query.get(id)

    name = request.json['name']
    fecha = request.json['fecha']
    tipo = request.json['tipo']
    units = request.json['units']
    deporte = request.json['deporte']
    equipos = request.json['equipos']
    linea = request.json['linea']
    estado = request.json['estado']
    resultado = request.json['resultado']

    picks_tipster.name = name
    picks_tipster.fecha = fecha
    picks_tipster.tipo = tipo
    picks_tipster.units = units
    picks_tipster.deporte = deporte
    picks_tipster.equipos = equipos
    picks_tipster.linea = linea
    picks_tipster.estado = estado
    picks_tipster.resultado = resultado

    db.session.commit()
    return jsonify({"msg": "Picks_Tipster edith successfully"}), 200


# -------- delete ----------------------------------------

@app.route("/upload/<id>", methods=["DELETE"])
def upload_delete(id):
    upload = Upload.query.get(id)
    db.session.delete(upload)
    db.session.commit()
    return "Imagen was successfully deleted"

# --------------------------------------------------------


@app.route("/picks_tipster/<id>", methods=["DELETE"])
def picks_tipster_delete(id):
    picks_tipster = Picks_Tipster.query.get(id)
    db.session.delete(picks_tipster)
    db.session.commit()
    return "pick was successfully deleted"

# --------------------------------------------------------


@app.route("/perfil_tipster/<id>", methods=["DELETE"])
def perfil_tipster_delete(id):
    perfil_tipster = Perfil_Tipster.query.get(id)
    db.session.delete(perfil_tipster)
    db.session.commit()
    return "Tipster was successfully deleted"

# --------------------------------------------------------
