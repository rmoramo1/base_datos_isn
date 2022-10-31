"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, render_template, redirect
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Upload, Perfil_Tipster

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

app.secret_key = "roycjs"
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower in ALLOWED_EXTENSIONS


MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code
# generate sitemap with all your endpoints


# @app.route('/')
# def sitemap():
#     return generate_sitemap(app)

# obtener usuario de base de datos y crea token

# obtener usuario de base de datos y crea token


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


# @app.route("/upload", methods=["GET"])
# def Upload_GET():
#     if request.method == "GET":
#         records = Upload.query.all()
#         return jsonify([Upload.serialize(record) for record in records])
#     else:
#         return jsonify({"msg": "no autorizado"})

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


def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def createUpload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('no image')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('upload image filename:' + filename)

        flash('image yes')
        return render_template('indexhtml', filename=filename)
    else:
        flash('allowed images')
        return redirect(request.url)

    # img = request.files("img", None)
    # name = request.json("name", None)
    # mimetype = request.json("mimetype", None)
    # like = request.json("like", None)
    # dislike = request.json("dislike", None)
    # comentario = request.json("comentario", None)
    # usuario = request.json("usuario", None)

    # upload = Upload.query.filter_by(
    #     name=name, dorsal=dorsal, birth=birth).first()
    # if Upload:
    #     return jsonify({"msg": "stats_punting_player_nfl already exists", "name": upload.name}), 401
    # else:

    #     upload = Upload(
    #         img=img,
    #         name=name,
    #         mimetype=mimetype,

    #         like=like,
    #         dislike=dislike,
    #         comentario=comentario,
    #         usuario=usuario
    #     )
    #     db.session.add(upload)
    #     db.session.commit()
    #     return jsonify({"msg": "User created successfully"}), 200


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


# -------- delete ----------------------------------------


@app.route("/upload/<id>", methods=["DELETE"])
def upload_delete(id):
    upload = Upload.query.get(id)
    db.session.delete(upload)
    db.session.commit()
    return "Noticia was successfully deleted"
