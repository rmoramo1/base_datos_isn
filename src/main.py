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
from models import db,User,Casinos, Nfl, Mlb, Nba, Nhl , Boxeo , Mma ,Nascar ,Nascar_drivers,Match_Ups_Nacar ,Golf ,Golfer ,Ncaa_Baseball,Ncaa_Football,Ncaa_Basketball,Stats_nba_player,Stats_nba_team, Stats_mlb_team, Stats_mlb_player,Stats_nhl_team, Stats_nhl_player,Stats_box_fighter, Stats_mma_fighter,Stats_nfl_team,Stats_defensive_player_nfl, Stats_offensive_player_nfl,Stats_returning_player_nfl,Stats_kiking_player_nfl,Stats_punting_player_nfl,Soccer,Soccer_Tournament,Stats_Soccer_Team,Stats_Soccer_Player,Logos_NFL,Logos_NBA,Logos_MLB,Logos_NHL,Logos_SOCCER , Logos_Ncaa_Basketball , Logos_Ncaa_Football, Logos_Ncaa_Baseball , Props , Odds_to_win , Stats_ncaa_baseball_player ,  Stats_ncaa_baseball_team , Stats_ncaa_football_team , Stats_defensive_player_ncca_football , Stats_offensive_player_ncaa_football , Stats_returning_player_ncaa_football , Stats_kiking_player_ncaa_football , Stats_punting_player_ncaa_football , Stats_ncaa_basket_team , Stats_ncaa_basket_player,Injuries, Futures , Moto_GP, Moto_gp_drivers

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

#obtener usuario de base de datos y crea token
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
    return jsonify({"token": access_token, "username":user.name})

#obtiene usuario----------------------------------------

@app.route("/user", methods=["GET"])
def user():
    if request.method == "GET":
        records = User.query.all()
        return jsonify([User.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------
@app.route("/injuries", methods=["GET"])
def injuries():
    if request.method == "GET":
        records = Injuries.query.all()
        return jsonify([Injuries.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------

@app.route("/futures", methods=["GET"])
def futures():
    if request.method == "GET":
        records = Futures.query.all()
        return jsonify([Futures.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------

@app.route("/props", methods=["GET"])
def props():
    if request.method == "GET":
        records = Props.query.all()
        return jsonify([Props.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------
@app.route("/odds_to_win", methods=["GET"])
def odds_to_win():
    if request.method == "GET":
        records = Odds_to_win.query.all()
        return jsonify([Odds_to_win.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------
@app.route("/soccer", methods=["GET"])
def soccer():
    if request.method == "GET":
        records = Soccer.query.all()
        return jsonify([Soccer.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------

@app.route("/soccer_tournament", methods=["GET"])
def soccer_tournament():
    if request.method == "GET":
        records = Soccer_Tournament.query.all()
        return jsonify([Soccer_Tournament.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------
@app.route("/stats_soccer_player", methods=["GET"])
def stats_soccer_player():
    if request.method == "GET":
        records = Stats_Soccer_Player.query.all()
        return jsonify([Stats_Soccer_Player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------

@app.route("/stats_soccer_team", methods=["GET"])
def stats_soccer_team():
    if request.method == "GET":
        records = Stats_Soccer_Team.query.all()
        return jsonify([Stats_Soccer_Team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------
@app.route("/casinos", methods=["GET"])
def casinos():
    if request.method == "GET":
        records = Casinos.query.all()
        return jsonify([Casinos.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ----------------------------------------------------------------------------

@app.route("/mlb", methods=["GET"])
def mlb():
    if request.method == "GET":
        records = Mlb.query.all()
        return jsonify([Mlb.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/ncaa_football", methods=["GET"])
#   @limiter.limit("12 per hour")
def ncaa_football():
    if request.method == "GET":
        records = Ncaa_Football.query.all()
        return jsonify([Ncaa_Football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/stats_defensive_player_ncca_football", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_defensive_player_ncca_football():
    if request.method == "GET":
        records = Stats_defensive_player_ncca_football.query.all()
        return jsonify([Stats_defensive_player_ncca_football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_offensive_player_ncaa_football", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_offensive_player_ncaa_football():
    if request.method == "GET":
        records = Stats_offensive_player_ncaa_football.query.all()
        return jsonify([Stats_offensive_player_ncaa_football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_returning_player_ncaa_football", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_returning_player_ncaa_football():
    if request.method == "GET":
        records = Stats_returning_player_ncaa_football.query.all()
        return jsonify([Stats_returning_player_ncaa_football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_kiking_player_ncaa_football", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_kiking_player_ncaa_football():
    if request.method == "GET":
        records = Stats_kiking_player_ncaa_football.query.all()
        return jsonify([Stats_kiking_player_ncaa_football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_punting_player_ncaa_football", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_punting_player_ncaa_football():
    if request.method == "GET":
        records = Stats_punting_player_ncaa_football.query.all()
        return jsonify([Stats_punting_player_ncaa_football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_ncaa_football_team", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_ncaa_football_team():
    if request.method == "GET":
        records = Stats_ncaa_football_team.query.all()
        return jsonify([Stats_ncaa_football_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/nfl", methods=["GET"])
def nfl():
    if request.method == "GET":
        records = Nfl.query.all()
        return jsonify([Nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/ncaa_baseball", methods=["GET"])
#   @limiter.limit("12 per hour")
def ncaa_baseball():
    if request.method == "GET":
        records = Ncaa_Baseball.query.all()
        return jsonify([Ncaa_Baseball.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/stats_ncaa_baseball_player", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_ncaa_baseball_player():
    if request.method == "GET":
        records = Stats_ncaa_baseball_player.query.all()
        return jsonify([Stats_ncaa_baseball_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_ncaa_baseball_team", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_ncaa_baseball_team():
    if request.method == "GET":
        records = Stats_ncaa_baseball_team.query.all()
        return jsonify([Stats_ncaa_baseball_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/nba", methods=["GET"])
def nba():
    if request.method == "GET":
        records = Nba.query.all()
        return jsonify([Nba.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/ncaa_basketball", methods=["GET"])
#   @limiter.limit("12 per hour")
def ncaa_basketball():
    if request.method == "GET":
        records = Ncaa_Basketball.query.all()
        return jsonify([Ncaa_Basketball.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_ncaa_basket_team", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_ncaa_basket_team():
    if request.method == "GET":
        records = Stats_ncaa_basket_team.query.all()
        return jsonify([Stats_ncaa_basket_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/stats_ncaa_basket_player", methods=["GET"])
#   @limiter.limit("12 per hour")
def stats_ncaa_basket_player():
    if request.method == "GET":
        records = Stats_ncaa_basket_player.query.all()
        return jsonify([Stats_ncaa_basket_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/nhl", methods=["GET"])
def nhl():
    if request.method == "GET":
        records = Nhl.query.all()
        return jsonify([Nhl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/boxeo", methods=["GET"])
def boxeo():
    if request.method == "GET":
        records = Boxeo.query.all()
        return jsonify([Boxeo.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/mma", methods=["GET"])
def mma():
    if request.method == "GET":
        records = Mma.query.all()
        return jsonify([Mma.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/nascar", methods=["GET"])
def nascar():
    if request.method == "GET":
        records = Nascar.query.all()
        return jsonify([Nascar.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------
@app.route("/moto_gp", methods=["GET"])
def moto_gp():
    if request.method == "GET":
        records = Moto_GP.query.all()
        return jsonify([Moto_GP.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# ---------------------------------------------------------------------------

@app.route("/nascar_drivers", methods=["GET"])
def nascar_drivers():
    if request.method == "GET":
        records = Nascar_drivers.query.all()
        return jsonify([Nascar_drivers.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------
@app.route("/moto_gp_drivers", methods=["GET"])
def moto_gp_drivers():
    if request.method == "GET":
        records = Moto_gp_drivers.query.all()
        return jsonify([Moto_gp_drivers.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------

@app.route("/match_ups_nascar", methods=["GET"])
def match_ups_nascar():
    if request.method == "GET":
        records = Match_Ups_Nacar.query.all()
        return jsonify([Match_Ups_Nacar.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------

@app.route("/golf", methods=["GET"])
def golf():
    if request.method == "GET":
        records = Golf.query.all()
        return jsonify([Golf.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------


@app.route("/golfer", methods=["GET"])
def golfer():
    if request.method == "GET":
        records = Golfer.query.all()
        return jsonify([Golfer.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # ---------------------------------------------------------------------------

@app.route("/stats_nba_player", methods=["GET"])
def stats_nba_player():
    if request.method == "GET":
        records = Stats_nba_player().query.all()
        return jsonify([Stats_nba_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------
@app.route("/stats_nba_team", methods=["GET"])
def stats_nba_team():
    if request.method == "GET":
        records = Stats_nba_team().query.all()
        return jsonify([Stats_nba_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------
@app.route("/stats_mlb_team", methods=["GET"])
def stats_mlb_team():
    if request.method == "GET":
        records = Stats_mlb_team().query.all()
        return jsonify([Stats_mlb_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_mlb_player", methods=["GET"])
def stats_mlb_player():
    if request.method == "GET":
        records = Stats_mlb_player().query.all()
        return jsonify([Stats_mlb_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_nhl_team", methods=["GET"])
def stats_nhl_team():
    if request.method == "GET":
        records = Stats_nhl_team().query.all()
        return jsonify([Stats_nhl_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_nhl_player", methods=["GET"])
def stats_nhl_player():
    if request.method == "GET":
        records = Stats_nhl_player().query.all()
        return jsonify([Stats_nhl_player.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_box_fighter", methods=["GET"])
def stats_box_fighter():
    if request.method == "GET":
        records = Stats_box_fighter().query.all()
        return jsonify([Stats_box_fighter.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_mma_fighter", methods=["GET"])
def stats_mma_fighter():
    if request.method == "GET":
        records = Stats_mma_fighter().query.all()
        return jsonify([Stats_mma_fighter.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_nfl_team", methods=["GET"])
def stats_nfl_team():
    if request.method == "GET":
        records = Stats_nfl_team().query.all()
        return jsonify([Stats_nfl_team.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_defensive_player_nfl", methods=["GET"])
def stats_defensive_player_nfl():
    if request.method == "GET":
        records = Stats_defensive_player_nfl().query.all()
        return jsonify([Stats_defensive_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_offensive_player_nfl", methods=["GET"])
def stats_offensive_player_nfl():
    if request.method == "GET":
        records = Stats_offensive_player_nfl().query.all()
        return jsonify([Stats_offensive_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_returning_player_nfl", methods=["GET"])
def stats_returning_player_nfl():
    if request.method == "GET":
        records = Stats_returning_player_nfl().query.all()
        return jsonify([Stats_returning_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_kiking_player_nfl", methods=["GET"])
def stats_kiking_player_nfl():
    if request.method == "GET":
        records = Stats_kiking_player_nfl().query.all()
        return jsonify([Stats_kiking_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
 # --------------------------------------------------------------------

@app.route("/stats_punting_player_nfl", methods=["GET"])
def stats_punting_player_nfl():
    if request.method == "GET":
        records = Stats_punting_player_nfl().query.all()
        return jsonify([Stats_punting_player_nfl.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

 # --------------------------------------------------------------------

@app.route("/logos_nfl", methods=["GET"])
def logos_nfl():
    if request.method == "GET":
        records = Logos_NFL().query.all()
        return jsonify([Logos_NFL.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

 # --------------------------------------------------------------------

@app.route("/logos_nba", methods=["GET"])
def logos_nba():
    if request.method == "GET":
        records = Logos_NBA().query.all()
        return jsonify([Logos_NBA.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

 # --------------------------------------------------------------------

@app.route("/logos_nhl", methods=["GET"])
def logos_nhl():
    if request.method == "GET":
        records = Logos_NHL().query.all()
        return jsonify([Logos_NHL.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

 # --------------------------------------------------------------------

@app.route("/logos_soccer", methods=["GET"])
def logos_soccer():
    if request.method == "GET":
        records = Logos_SOCCER().query.all()
        return jsonify([Logos_SOCCER.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

 # --------------------------------------------------------------------

@app.route("/logos_mlb", methods=["GET"])
def logos_mlb():
    if request.method == "GET":
        records = Logos_MLB().query.all()
        return jsonify([Logos_MLB.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})
# --------------------------------------------------------------------

@app.route("/logos_ncaa_basketball", methods=["GET"])
def logos_ncaa_basketball():
    if request.method == "GET":
        records = Logos_Ncaa_Basketball().query.all()
        return jsonify([Logos_Ncaa_Basketball.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

# --------------------------------------------------------------------

@app.route("/logos_ncaa_football", methods=["GET"])
def logos_ncaa_football():
    if request.method == "GET":
        records = Logos_Ncaa_Football().query.all()
        return jsonify([Logos_Ncaa_Football.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

# --------------------------------------------------------------------

@app.route("/logos_ncaa_baseball", methods=["GET"])
def logos_ncaa_baseball():
    if request.method == "GET":
        records = Logos_Ncaa_Baseball().query.all()
        return jsonify([Logos_Ncaa_Baseball.serialize(record) for record in records])
    else:
        return jsonify({"msg": "no autorizado"})

# --------------------------post methot--------------------------------------------

@app.route('/casinos', methods=['POST'])
def createCasino():
    name = request.json.get("name", None)

    # busca team en BBDD
    casinos = Casinos.query.filter_by(name=name).first()
    # the team was not found on the database
    if casinos:
        return jsonify({"msg": "Casino already exists", "Casino": casinos.name}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        casinos = Casinos(
            name=name,
        )
        db.session.add(casinos)
        db.session.commit()
        return jsonify({"msg": "casino created successfully"}), 200

@app.route('/futures', methods=['POST'])
def createfutures():
    sport = request.json.get("sport", None)
    future = request.json.get("future", None)
    line = request.json.get("line", None)
    date = request.json.get("date", None)

    # busca team en BBDD
    futures = Futures.query.filter_by(future=future).first()
    # the team was not found on the database
    if futures:
        return jsonify({"msg": "futures already exists", "futures": futures.future}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        futures = Futures(
            sport=sport,
            future=future,
            line=line,
            date=date,
        )
        db.session.add(futures)
        db.session.commit()
        return jsonify({"msg": "futures created successfully"}), 200

@app.route('/injuries', methods=['POST'])
def createinjuries():
    sport = request.json.get("sport", None)
    name_player = request.json.get("name_player", None)
    team = request.json.get("team", None)
    injurie = request.json.get("injurie", None)
    time_injurie = request.json.get("time_injurie", None)
    date = request.json.get("date", None)

    # busca team en BBDD
    injuries = Injuries.query.filter_by(name_player=name_player,date=date,team=team).first()
    # the team was not found on the database
    if injuries:
        return jsonify({"msg": "injuries already exists", "Casino": injuries.name_player}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        injuries = Injuries(
            sport=sport,
            name_player=name_player,
            team=team,
            injurie=injurie,
            time_injurie=time_injurie,
            date=date,
        )
        db.session.add(injuries)
        db.session.commit()
        return jsonify({"msg": "injuries created successfully"}), 200

@app.route('/props', methods=['POST'])
def createProps():
    title = request.json.get("title", None)
    date = request.json.get("date", None)
    type_prop = request.json.get("type_prop", None)
    sport = request.json.get("sport", None)
    feature = request.json.get("feature", None)
    line = request.json.get("line", None)
    home = request.json.get("home", None)
    away = request.json.get("away", None)

    # busca team en BBDD
    props = Props.query.filter_by(title=title,line=line,type_prop=type_prop,feature=feature,home=home,away=away).first()
    # the team was not found on the database
    if props:
        return jsonify({"msg": "props already exists", "props": props.title}), 401
    else:
        # crea props nuevo
        # crea registro nuevo en BBDD de
        props = Props(
            title=title,
            date=date,
            type_prop=type_prop,
            sport=sport,
            feature=feature,
            line=line,
            home=home,
            away=away
        )
        db.session.add(props)
        db.session.commit()
        return jsonify({"msg": "Props created successfully"}), 200

@app.route('/odds_to_win', methods=['POST'])
def createOdds_to_win():
    title = request.json.get("title", None)
    sport = request.json.get("sport", None)
    type_odd = request.json.get("type_odd", None)
    line = request.json.get("line", None)
    line = request.json.get("line", None)
    team = request.json.get("team", None)
    date = request.json.get("date", None)

    # busca team en BBDD
    odds_to_win = Odds_to_win.query.filter_by(title=title,line=line,type_odd=type_odd,team=team).first()
    # the team was not found on the database
    if odds_to_win:
        return jsonify({"msg": "odds_to_win already exists", "odds_to_win": odds_to_win.title}), 401
    else:
        # crea odds_to_win nuevo
        # crea registro nuevo en BBDD de
        odds_to_win = Odds_to_win(
            title=title,
            sport=sport,
            type_odd=type_odd,
            line=line,
            team=team,
            date=date
        )
        db.session.add(odds_to_win)
        db.session.commit()
        return jsonify({"msg": "odds_to_win created successfully"}), 200

@app.route('/logos_nfl', methods=['POST'])
def createLogos_nfl():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_nfl = Logos_NFL.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_nfl:
        return jsonify({"msg": "Logos_NFL already exists", "LOGO": logos_nfl.team}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        logos_nfl = Logos_NFL(
            team=team,
            url=url
        )
        db.session.add(logos_nfl)
        db.session.commit()
        return jsonify({"msg": "logos_nfl created successfully"}), 200

@app.route('/logos_nba', methods=['POST'])
def createLogos_nba():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_nba = Logos_NBA.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_nba:
        return jsonify({"msg": "LOGO already exists", "LOGO": logos_nba.team}), 401
    else:
        # crea LOGO nuevo
        # crea registro nuevo en BBDD de
        logos_nba = Logos_NBA(
            team=team,
            url=url
        )
        db.session.add(logos_nba)
        db.session.commit()
        return jsonify({"msg": "Logos_NBA created successfully"}), 200

@app.route('/logos_mlb', methods=['POST'])
def createLogos_MLB():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_mlb = Logos_MLB.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_mlb:
        return jsonify({"msg": "LOGO already exists", "LOGO": logos_mlb.team}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        logos_mlb = Logos_MLB(
            team=team,
            url=url
        )
        db.session.add(logos_mlb)
        db.session.commit()
        return jsonify({"msg": "logos_mlb created successfully"}), 200

@app.route('/logos_nhl', methods=['POST'])
def createLogos_NHL():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_nhl = Logos_NHL.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_nhl:
        return jsonify({"msg": "LOGO already exists", "LOGO": logos_NHL.team}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        logos_nhl = Logos_NHL(
            team=team,
            url=url
        )
        db.session.add(logos_nhl)
        db.session.commit()
        return jsonify({"msg": "Logos_NHL created successfully"}), 200

@app.route('/logos_soccer', methods=['POST'])
def createLogos_SOCCER():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_soccer = Logos_SOCCER.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_soccer:
        return jsonify({"msg": "LOGO already exists", "LOGO": logos_soccer.team}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        logos_soccer = Logos_SOCCER(
            team=team,
            url=url
        )
        db.session.add(logos_soccer)
        db.session.commit()
        return jsonify({"msg": "logos_soccer created successfully"}), 200

@app.route('/logos_ncaa_basketball', methods=['POST'])
def createLogos_ncaa_basketball():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_ncaa_basketball = Logos_Ncaa_Basketball.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_ncaa_basketball:
        return jsonify({"msg": "LOGO already exists", "LOGO": logos_ncaa_basketball.team}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        logos_ncaa_basketball = Logos_Ncaa_Basketball(
            team=team,
            url=url
        )
        db.session.add(logos_ncaa_basketball)
        db.session.commit()
        return jsonify({"msg": "logos_ncaa_basketball created successfully"}), 200

@app.route('/logos_ncaa_football', methods=['POST'])
def createlogos_ncaa_football():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_ncaa_football = Logos_Ncaa_Football.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_ncaa_football:
        return jsonify({"msg": "LOGO already exists", "LOGO": logos_ncaa_football.team}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        logos_ncaa_football = Logos_Ncaa_Football(
            team=team,
            url=url
        )
        db.session.add(logos_ncaa_football)
        db.session.commit()
        return jsonify({"msg": "logos_ncaa_football created successfully"}), 200

@app.route('/logos_ncaa_baseball', methods=['POST'])
def createlogos_ncaa_baseball():
    team = request.json.get("team", None)
    url = request.json.get("url", None)

    # busca team en BBDD
    logos_ncaa_baseball = Logos_Ncaa_Baseball.query.filter_by(team=team,url=url).first()
    # the team was not found on the database
    if logos_ncaa_baseball:
        return jsonify({"msg": "LOGO already exists", "LOGO": logos_ncaa_baseball.team}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        logos_ncaa_baseball = Logos_Ncaa_Baseball(
            team=team,
            url=url
        )
        db.session.add(logos_ncaa_baseball)
        db.session.commit()
        return jsonify({"msg": "logos_ncaa_baseball created successfully"}), 200


@app.route('/soccer_tournament', methods=['POST'])
def createSoccer_Tournament():
    country = request.json.get("country", None)
    tournament = request.json.get("tournament", None)

    # busca team en BBDD
    soccer_tournament = Soccer_Tournament.query.filter_by(tournament=tournament,country=country).first()
    # the team was not found on the database
    if soccer_tournament:
        return jsonify({"msg": "tournament already exists", "tournament": soccer_tournament.tournament}), 401
    else:
        # crea casino nuevo
        # crea registro nuevo en BBDD de
        soccer_tournament = Soccer_Tournament(
            country=country,
            tournament=tournament
        )
        db.session.add(soccer_tournament)
        db.session.commit()
        return jsonify({"msg": "soccer_tournament created successfully"}), 200


@app.route('/mlb', methods=['POST'])
def createGameMlb():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_home = request.json.get("rotation_home", None)
    rotation_away = request.json.get("rotation_away", None)
    away = request.json.get("away", None)
    pitcher_a = request.json.get("pitcher_a", None)
    home = request.json.get("home", None)
    pitcher_h = request.json.get("pitcher_h", None)
    rl_away = request.json.get("rl_away", None)
    rl_home = request.json.get("rl_home", None)
    juice_rl_away = request.json.get("juice_rl_away", None)
    juice_rl_home = request.json.get("juice_rl_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    rl_away_f5 = request.json.get("rl_away_f5", None)
    rl_home_f5 = request.json.get("rl_home_f5", None)
    juice_rl_away_f5 = request.json.get("juice_rl_away_f5", None)
    juice_rl_home_f5 = request.json.get("juice_rl_home_f5", None)
    moneyLineAway_f5 = request.json.get("moneyLineAway_f5", None)
    moneyLineHome_f5 = request.json.get("moneyLineHome_f5", None)
    total_f5 = request.json.get("total_f5", None)
    juice_total_over_f5 = request.json.get("juice_total_over_f5", None)
    juice_total_under_f5 = request.json.get("juice_total_under_f5", None)
    tt_away_f5 = request.json.get("tt_away_f5", None)
    juice_over_away_f5 = request.json.get("juice_over_away_f5", None)
    juice_under_away_f5 = request.json.get("juice_under_away_f5", None)
    juice_over_home_f5 = request.json.get("juice_over_home_f5", None)
    juice_under_home_f5 = request.json.get("juice_under_home_f5", None)
    fs_away_f5 = request.json.get("fs_away_f5", None)
    fs_home_f5 = request.json.get("fs_home_f5", None)
    sa_1inning = request.json.get("sa_1inning", None)
    sh_1inning = request.json.get("sh_1inning", None)
    sa_2inning = request.json.get("sa_2inning", None)
    sh_2inning = request.json.get("sh_2inning", None)
    sa_3inning = request.json.get("sa_3inning", None)
    sh_3inning = request.json.get("sh_3inning", None)
    sa_4inning = request.json.get("sa_4inning", None)
    sh_4inning = request.json.get("sh_4inning", None)
    sa_5inning = request.json.get("sa_5inning", None)
    sh_5inning = request.json.get("sh_5inning", None)
    sa_6inning = request.json.get("sa_6inning", None)
    sh_6inning = request.json.get("sh_6inning", None)
    sa_7inning = request.json.get("sa_7inning", None)
    sh_7inning = request.json.get("sh_7inning", None)
    sa_8inning = request.json.get("sa_8inning", None)
    sh_8inning = request.json.get("sh_8inning", None)
    sa_9inning = request.json.get("sa_9inning", None)
    sh_9inning = request.json.get("sh_9inning", None)
    sa_10inning = request.json.get("sa_10inning", None)
    sh_10inning = request.json.get("sh_10inning", None)
    sa_11inning = request.json.get("sa_11inning", None)
    sh_11inning = request.json.get("sh_11inning", None)
    sa_12inning = request.json.get("sa_12inning", None)
    sh_12inning = request.json.get("sh_12inning", None)
    sa_13inning = request.json.get("sa_13inning", None)
    sh_13inning = request.json.get("sh_13inning", None)
    sa_14inning = request.json.get("sa_14inning", None)
    sh_14inning = request.json.get("sh_14inning", None)
    sa_15inning = request.json.get("sa_15inning", None)
    sh_15inning = request.json.get("sh_15inning", None)
    sa_16inning = request.json.get("sa_16inning", None)
    sh_16inning = request.json.get("sh_16inning", None)
    sa_17inning = request.json.get("sa_17inning", None)
    sh_17inning = request.json.get("sh_17inning", None)
    sa_18inning = request.json.get("sa_18inning", None)
    sh_18inning = request.json.get("sh_18inning", None)
    sa_19inning = request.json.get("sa_19inning", None)
    sh_19inning = request.json.get("sh_19inning", None)
    sa_20inning = request.json.get("sa_20inning", None)
    sh_20inning = request.json.get("sh_20inning", None)
    sa_21inning = request.json.get("sa_21inning", None)
    sh_21inning = request.json.get("sh_21inning", None)
    sa_22inning = request.json.get("sa_22inning", None)
    sh_22inning = request.json.get("sh_22inning", None)
    sa_23inning = request.json.get("sa_23inning", None)
    sh_23inning = request.json.get("sh_23inning", None)
    sa_24inning = request.json.get("sa_24inning", None)
    sh_24inning = request.json.get("sh_24inning", None)
    sa_25inning = request.json.get("sa_25inning", None)
    sh_25inning = request.json.get("sh_25inning", None)
    # valida si estan vacios los ingresos

    # busca mlb en BBDD
    mlb = Mlb.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if mlb:
        return jsonify({"msg": "Mlb already exists", "status": mlb.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        mlb = Mlb(
            date=date, 
            hour=hour, 
            status=status, 
            rotation_away=rotation_away, 
            rotation_home=rotation_home, 
            casino=casino, 
            away=away, 
            pitcher_a=pitcher_a, 
            home=home, 
            pitcher_h=pitcher_h,
            rl_away=rl_away, 
            rl_home=rl_home, 
            juice_rl_away=juice_rl_away, 
            juice_rl_home=juice_rl_home,         
            moneyLineAway=moneyLineAway, 
            moneyLineHome=moneyLineHome, 
            total=total, 
            juice_total_over=juice_total_over, 
            juice_total_under=juice_total_under, 
            tt_away=tt_away, 
            juice_over_away=juice_over_away, 
            juice_under_away=juice_under_away, 
            tt_home=tt_home, 
            juice_over_home=juice_over_home, 
            juice_under_home=juice_under_home, 
            final_score_away=final_score_away, 
            final_score_home=final_score_home, 
            rl_away_f5=rl_away_f5, 
            rl_home_f5=rl_home_f5, 
            juice_rl_away_f5=juice_rl_away_f5, 
            juice_rl_home_f5=juice_rl_home_f5, 
            moneyLineAway_f5=moneyLineAway_f5, 
            moneyLineHome_f5=moneyLineHome_f5, 
            total_f5=total_f5, 
            juice_total_over_f5=juice_total_over_f5, 
            juice_total_under_f5=juice_total_under_f5, 
            tt_away_f5=tt_away_f5, 
            juice_over_away_f5=juice_over_away_f5, 
            juice_under_away_f5=juice_under_away_f5, 
            juice_over_home_f5=juice_over_home_f5, 
            juice_under_home_f5=juice_under_home_f5, 
            fs_away_f5=fs_away_f5,
            fs_home_f5=fs_home_f5, 
            sa_1inning=sa_1inning, sh_1inning=sh_1inning, sa_2inning=sa_2inning, sh_2inning=sh_2inning, sa_3inning=sa_3inning, sh_3inning=sh_3inning, sa_4inning=sa_4inning, sh_4inning=sh_4inning, sa_5inning=sa_5inning, sh_5inning=sh_5inning, sa_6inning=sa_6inning, sh_6inning=sh_6inning, sa_7inning=sa_7inning, sh_7inning=sh_7inning, sa_8inning=sa_8inning, sh_8inning=sh_8inning, sa_9inning=sa_9inning, sh_9inning=sh_9inning, sa_10inning=sa_10inning, sh_10inning=sh_10inning, sa_11inning=sa_11inning, sh_11inning=sh_11inning, sa_12inning=sa_12inning, sh_12inning=sh_12inning, sa_13inning=sa_13inning, sh_13inning=sh_13inning, sa_14inning=sa_14inning, sh_14inning=sh_14inning, sa_15inning=sa_15inning, sh_15inning=sh_15inning, sa_16inning=sa_16inning, sh_16inning=sh_16inning, sa_17inning=sa_17inning, sa_18inning=sa_18inning, sa_19inning=sa_19inning, sa_20inning=sa_20inning, sa_21inning=sa_21inning, sa_22inning=sa_22inning, sa_23inning=sa_23inning, sa_24inning=sa_24inning, sa_25inning=sa_25inning)
        db.session.add(mlb)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200


@app.route('/nba', methods=['POST'])
def createGameNba():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_home = request.json.get("rotation_home", None)
    rotation_away = request.json.get("rotation_away", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_total_over = request.json.get("fh_juice_total_over", None)
    fh_juice_total_under = request.json.get("fh_juice_total_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    # --------------
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("second_half_total", None)
    sh_juice_total_over = request.json.get("sh_juice_total_over", None)
    sh_juice_total_under = request.json.get("sh_juice_total_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    # ------
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)
    # --------
    q2_half_spread_away = request.json.get("q2_half_spread_away", None)
    q2_half_spread_home = request.json.get("q2_half_spread_home", None)
    q2_half_juice_spread_away = request.json.get(
        "q2_half_juice_spread_away", None)
    q2_half_juice_spread_home = request.json.get(
        "q2_half_juice_spread_home", None)
    q2_half_moneyLineAway = request.json.get("q2_half_moneyLineAway", None)
    q2_half_moneyLineHome = request.json.get("q2_half_moneyLineHome", None)
    q2_half_total = request.json.get("q2_half_total", None)
    q2_juice_over = request.json.get("q2_juice_over", None)
    q2_juice_under = request.json.get("q2_juice_under", None)
    q2_half_tt_away = request.json.get("q2_half_tt_away", None)
    q2_half_juice_over_away = request.json.get("q2_half_juice_over_away", None)
    q2_half_juice_under_away = request.json.get(
        "q2_half_juice_under_away", None)
    q2_half_tt_home = request.json.get("q2_half_tt_home", None)
    q2_half_juice_over_home = request.json.get("q2_half_juice_over_home", None)
    q2_half_juice_under_home = request.json.get(
        "q2_half_juice_under_home", None)
    q2_half_final_score_away = request.json.get(
        "q2_half_final_score_away", None)
    q2_half_final_score_home = request.json.get(
        "q2_half_final_score_home", None)
    # --------------
    q3_half_spread_away = request.json.get("q3_half_spread_away", None)
    q3_half_spread_home = request.json.get("q3_half_spread_home", None)
    q3_half_juice_spread_away = request.json.get(
        "q3_half_juice_spread_away", None)
    q3_half_juice_spread_home = request.json.get(
        "q3_half_juice_spread_home", None)
    q3_half_moneyLineAway = request.json.get("q3_half_moneyLineAway", None)
    q3_half_moneyLineHome = request.json.get("q3_half_moneyLineHome", None)
    q3_half_total = request.json.get("q3_half_total", None)
    q3_juice_over = request.json.get("q3_juice_over", None)
    q3_juice_under = request.json.get("q3_juice_under", None)
    q3_half_tt_away = request.json.get("q3_half_tt_away", None)
    q3_half_juice_over_away = request.json.get("q3_half_juice_over_away", None)
    q3_half_juice_under_away = request.json.get(
        "q3_half_juice_under_away", None)
    q3_half_tt_home = request.json.get("q3_half_tt_home", None)
    q3_half_juice_over_home = request.json.get("q3_half_juice_over_home", None)
    q3_half_juice_under_home = request.json.get(
        "q3_half_juice_under_home", None)
    q3_half_final_score_away = request.json.get(
        "q3_half_final_score_away", None)
    q3_half_final_score_home = request.json.get(
        "q3_half_final_score_home", None)
    # --------------
    q4_half_spread_away = request.json.get("q4_half_spread_away", None)
    q4_half_spread_home = request.json.get("q4_half_spread_home", None)
    q4_half_juice_spread_away = request.json.get(
        "q4_half_juice_spread_away", None)
    q4_half_juice_spread_home = request.json.get(
        "q4_half_juice_spread_home", None)
    q4_half_moneyLineAway = request.json.get("q4_half_moneyLineAway", None)
    q4_half_moneyLineHome = request.json.get("q4_half_moneyLineHome", None)
    q4_half_total = request.json.get("q4_half_total", None)
    q4_juice_over = request.json.get("q4_juice_over", None)
    q4_juice_under = request.json.get("q4_juice_under", None)
    q4_half_tt_away = request.json.get("q4_half_tt_away", None)
    q4_half_juice_over_away = request.json.get("q4_half_juice_over_away", None)
    q4_half_juice_under_away = request.json.get(
        "q4_half_juice_under_away", None)
    q4_half_tt_home = request.json.get("q4_half_tt_home", None)
    q4_half_juice_over_home = request.json.get("q4_half_juice_over_home", None)
    q4_half_juice_under_home = request.json.get(
        "q4_half_juice_under_home", None)
    q4_half_final_score_away = request.json.get(
        "q4_half_final_score_away", None)
    q4_half_final_score_home = request.json.get(
        "q4_half_final_score_home", None)
    # busca mlb en BBDD
    nba = Nba.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if nba:
        return jsonify({"msg": "nba game already exists", "status": nba.home, "vrs": nba.away}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nba = Nba(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_away=rotation_away,
            rotation_home=rotation_home,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            # --
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_total_over=fh_juice_total_over,
            fh_juice_total_under=fh_juice_total_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away,
            first_half_juice_under_away=first_half_juice_under_away,
            first_half_tt_home=first_half_tt_home,
            first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home,
            # --
            second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_total_over=sh_juice_total_over,
            sh_juice_total_under=sh_juice_total_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            # --
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home,
            # ---
            q2_half_spread_away=q2_half_spread_away,
            q2_half_spread_home=q2_half_spread_home,
            q2_half_juice_spread_away=q2_half_juice_spread_away,
            q2_half_juice_spread_home=q2_half_juice_spread_home,
            q2_half_moneyLineAway=q2_half_moneyLineAway,
            q2_half_moneyLineHome=q2_half_moneyLineHome,
            q2_half_total=q2_half_total,
            q2_juice_over=q2_juice_over,
            q2_juice_under=q2_juice_under,
            q2_half_tt_away=q2_half_tt_away,
            q2_half_juice_over_away=q2_half_juice_over_away,
            q2_half_juice_under_away=q2_half_juice_under_away,
            q2_half_tt_home=q2_half_tt_home,
            q2_half_juice_over_home=q2_half_juice_over_home,
            q2_half_juice_under_home=q2_half_juice_under_home,
            q2_half_final_score_away=q2_half_final_score_away,
            q2_half_final_score_home=q2_half_final_score_home,
            # ---
            q3_half_spread_away=q3_half_spread_away,
            q3_half_spread_home=q3_half_spread_home,
            q3_half_juice_spread_away=q3_half_juice_spread_away,
            q3_half_juice_spread_home=q3_half_juice_spread_home,
            q3_half_moneyLineAway=q3_half_moneyLineAway,
            q3_half_moneyLineHome=q3_half_moneyLineHome,
            q3_half_total=q3_half_total,
            q3_juice_over=q3_juice_over,
            q3_juice_under=q3_juice_under,
            q3_half_tt_away=q3_half_tt_away,
            q3_half_juice_over_away=q3_half_juice_over_away,
            q3_half_juice_under_away=q3_half_juice_under_away,
            q3_half_tt_home=q3_half_tt_home,
            q3_half_juice_over_home=q3_half_juice_over_home,
            q3_half_juice_under_home=q3_half_juice_under_home,
            q3_half_final_score_away=q3_half_final_score_away,
            q3_half_final_score_home=q3_half_final_score_home,
            # ---
            q4_half_spread_away=q4_half_spread_away,
            q4_half_spread_home=q4_half_spread_home,
            q4_half_juice_spread_away=q4_half_juice_spread_away,
            q4_half_juice_spread_home=q4_half_juice_spread_home,
            q4_half_moneyLineAway=q4_half_moneyLineAway,
            q4_half_moneyLineHome=q4_half_moneyLineHome,
            q4_half_total=q4_half_total,
            q4_juice_over=q4_juice_over,
            q4_juice_under=q4_juice_under,
            q4_half_tt_away=q4_half_tt_away,
            q4_half_juice_over_away=q4_half_juice_over_away,
            q4_half_juice_under_away=q4_half_juice_under_away,
            q4_half_tt_home=q4_half_tt_home,
            q4_half_juice_over_home=q4_half_juice_over_home,
            q4_half_juice_under_home=q4_half_juice_under_home,
            q4_half_final_score_away=q4_half_final_score_away,
            q4_half_final_score_home=q4_half_final_score_home
        )
        db.session.add(nba)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/nhl', methods=['POST'])
def createGameNhl():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    rotation_away = request.json.get("rotation_away", None)
    rotation_home = request.json.get("rotation_home", None)
    casino = request.json.get("casino", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    puck_line_away = request.json.get("puck_line_away", None)
    puck_line_home = request.json.get("puck_line_home", None)
    juice_puck_away = request.json.get("juice_puck_away", None)
    juice_puck_home = request.json.get("juice_puck_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    puck_away_1Q = request.json.get("puck_away_1Q", None)
    puck_home_1Q = request.json.get("puck_home_1Q", None)
    juice_puck_away_1Q = request.json.get("juice_puck_away_1Q", None)
    juice_puck_home_1Q = request.json.get("juice_puck_home_1Q", None)
    moneyLineAway_1Q = request.json.get("moneyLineAway_1Q", None)
    moneyLineHome_1Q = request.json.get("moneyLineHome_1Q", None)
    total_1Q = request.json.get("total_1Q", None)
    Q1_juice_over = request.json.get("Q1_juice_over", None)
    Q1_juice_under = request.json.get("Q1_juice_under", None)
    tt_away_1Q = request.json.get("tt_away_1Q", None)
    juice_over_away_1Q = request.json.get("juice_over_away_1Q", None)
    juice_under_away_1Q = request.json.get("juice_under_away_1Q", None)
    tt_home_1Q = request.json.get("tt_home_1Q", None)
    juice_over_home_1Q = request.json.get("juice_over_home_1Q", None)
    juice_under_home_1Q = request.json.get("juice_under_home_1Q", None)
    sa_1Q = request.json.get("sa_1Q", None)
    sh_1Q = request.json.get("sh_1Q", None)
    sa_2Q = request.json.get("sa_2Q", None)
    sh_2Q = request.json.get("sh_2Q", None)
    sa_3Q = request.json.get("sa_3Q", None)
    sh_3Q = request.json.get("sh_3Q", None)

    # busca mlb en BBDD
    nhl = Nhl.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if nhl:
        return jsonify({"msg": "Mlb already exists", "status": nhl.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nhl = Nhl(
            date=date,
            hour=hour,
            status=status,
            rotation_away=rotation_away,
            rotation_home=rotation_home,
            casino=casino,
            away=away,
            home=home,
            puck_line_away=puck_line_away,
            puck_line_home=puck_line_home,
            juice_puck_away=juice_puck_away,
            juice_puck_home=juice_puck_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            puck_away_1Q=puck_away_1Q,
            puck_home_1Q=puck_home_1Q,
            juice_puck_away_1Q=juice_puck_away_1Q,
            juice_puck_home_1Q=juice_puck_home_1Q,
            moneyLineAway_1Q=moneyLineAway_1Q,
            moneyLineHome_1Q=moneyLineHome_1Q,
            total_1Q=total_1Q,
            Q1_juice_over=Q1_juice_over,
            Q1_juice_under=Q1_juice_under,
            tt_away_1Q=tt_away_1Q,
            juice_over_away_1Q=juice_over_away_1Q, 
            juice_under_away_1Q=juice_under_away_1Q,
            tt_home_1Q=tt_home_1Q,
            juice_over_home_1Q=juice_over_home_1Q,
            juice_under_home_1Q=juice_under_home_1Q,
            sa_1Q=sa_1Q,
            sh_1Q=sh_1Q,
            sa_2Q=sa_2Q,
            sh_2Q=sh_2Q,
            sa_3Q=sa_3Q,
            sh_3Q=sh_3Q,
        )
        db.session.add(nhl)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/nfl', methods=['POST'])
def createGameNfl():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_home = request.json.get("rotation_home", None)
    rotation_away = request.json.get("rotation_away", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_total_over = request.json.get("fh_juice_total_over", None)
    fh_juice_total_under = request.json.get("fh_juice_total_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    # --------------
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("second_half_total", None)
    sh_juice_total_over = request.json.get("sh_juice_total_over", None)
    sh_juice_total_under = request.json.get("sh_juice_total_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    # ------
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)
    # --------
    q2_half_spread_away = request.json.get("q2_half_spread_away", None)
    q2_half_spread_home = request.json.get("q2_half_spread_home", None)
    q2_half_juice_spread_away = request.json.get(
        "q2_half_juice_spread_away", None)
    q2_half_juice_spread_home = request.json.get(
        "q2_half_juice_spread_home", None)
    q2_half_moneyLineAway = request.json.get("q2_half_moneyLineAway", None)
    q2_half_moneyLineHome = request.json.get("q2_half_moneyLineHome", None)
    q2_half_total = request.json.get("q2_half_total", None)
    q2_juice_over = request.json.get("q2_juice_over", None)
    q2_juice_under = request.json.get("q2_juice_under", None)
    q2_half_tt_away = request.json.get("q2_half_tt_away", None)
    q2_half_juice_over_away = request.json.get("q2_half_juice_over_away", None)
    q2_half_juice_under_away = request.json.get(
        "q2_half_juice_under_away", None)
    q2_half_tt_home = request.json.get("q2_half_tt_home", None)
    q2_half_juice_over_home = request.json.get("q2_half_juice_over_home", None)
    q2_half_juice_under_home = request.json.get(
        "q2_half_juice_under_home", None)
    q2_half_final_score_away = request.json.get(
        "q2_half_final_score_away", None)
    q2_half_final_score_home = request.json.get(
        "q2_half_final_score_home", None)
    # --------------
    q3_half_spread_away = request.json.get("q3_half_spread_away", None)
    q3_half_spread_home = request.json.get("q3_half_spread_home", None)
    q3_half_juice_spread_away = request.json.get(
        "q3_half_juice_spread_away", None)
    q3_half_juice_spread_home = request.json.get(
        "q3_half_juice_spread_home", None)
    q3_half_moneyLineAway = request.json.get("q3_half_moneyLineAway", None)
    q3_half_moneyLineHome = request.json.get("q3_half_moneyLineHome", None)
    q3_half_total = request.json.get("q3_half_total", None)
    q3_juice_over = request.json.get("q3_juice_over", None)
    q3_juice_under = request.json.get("q3_juice_under", None)
    q3_half_tt_away = request.json.get("q3_half_tt_away", None)
    q3_half_juice_over_away = request.json.get("q3_half_juice_over_away", None)
    q3_half_juice_under_away = request.json.get(
        "q3_half_juice_under_away", None)
    q3_half_tt_home = request.json.get("q3_half_tt_home", None)
    q3_half_juice_over_home = request.json.get("q3_half_juice_over_home", None)
    q3_half_juice_under_home = request.json.get(
        "q3_half_juice_under_home", None)
    q3_half_final_score_away = request.json.get(
        "q3_half_final_score_away", None)
    q3_half_final_score_home = request.json.get(
        "q3_half_final_score_home", None)
    # --------------
    q4_half_spread_away = request.json.get("q4_half_spread_away", None)
    q4_half_spread_home = request.json.get("q4_half_spread_home", None)
    q4_half_juice_spread_away = request.json.get(
        "q4_half_juice_spread_away", None)
    q4_half_juice_spread_home = request.json.get(
        "q4_half_juice_spread_home", None)
    q4_half_moneyLineAway = request.json.get("q4_half_moneyLineAway", None)
    q4_half_moneyLineHome = request.json.get("q4_half_moneyLineHome", None)
    q4_half_total = request.json.get("q4_half_total", None)
    q4_juice_over = request.json.get("q4_juice_over", None)
    q4_juice_under = request.json.get("q4_juice_under", None)
    q4_half_tt_away = request.json.get("q4_half_tt_away", None)
    q4_half_juice_over_away = request.json.get("q4_half_juice_over_away", None)
    q4_half_juice_under_away = request.json.get(
        "q4_half_juice_under_away", None)
    q4_half_tt_home = request.json.get("q4_half_tt_home", None)
    q4_half_juice_over_home = request.json.get("q4_half_juice_over_home", None)
    q4_half_juice_under_home = request.json.get(
        "q4_half_juice_under_home", None)
    q4_half_final_score_away = request.json.get(
        "q4_half_final_score_away", None)
    q4_half_final_score_home = request.json.get(
        "q4_half_final_score_home", None)
    # busca mlb en BBDD
    nfl = Nfl.query.filter_by(home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if nfl:
        return jsonify({"msg": "Nfl game already exists", "status": nfl.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nfl = Nfl(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_home=rotation_home,
            rotation_away=rotation_away,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            # --
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_total_over=fh_juice_total_over,
            fh_juice_total_under=fh_juice_total_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away,
            first_half_juice_under_away=first_half_juice_under_away,
            first_half_tt_home=first_half_tt_home,
            first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home,
            # --
            second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_total_over=sh_juice_total_over,
            sh_juice_total_under=sh_juice_total_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            # --
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home,
            # ---
            q2_half_spread_away=q2_half_spread_away,
            q2_half_spread_home=q2_half_spread_home,
            q2_half_juice_spread_away=q2_half_juice_spread_away,
            q2_half_juice_spread_home=q2_half_juice_spread_home,
            q2_half_moneyLineAway=q2_half_moneyLineAway,
            q2_half_moneyLineHome=q2_half_moneyLineHome,
            q2_half_total=q2_half_total,
            q2_juice_over=q2_juice_over,
            q2_juice_under=q2_juice_under,
            q2_half_tt_away=q2_half_tt_away,
            q2_half_juice_over_away=q2_half_juice_over_away,
            q2_half_juice_under_away=q2_half_juice_under_away,
            q2_half_tt_home=q2_half_tt_home,
            q2_half_juice_over_home=q2_half_juice_over_home,
            q2_half_juice_under_home=q2_half_juice_under_home,
            q2_half_final_score_away=q2_half_final_score_away,
            q2_half_final_score_home=q2_half_final_score_home,
            # ---
            q3_half_spread_away=q3_half_spread_away,
            q3_half_spread_home=q3_half_spread_home,
            q3_half_juice_spread_away=q3_half_juice_spread_away,
            q3_half_juice_spread_home=q3_half_juice_spread_home,
            q3_half_moneyLineAway=q3_half_moneyLineAway,
            q3_half_moneyLineHome=q3_half_moneyLineHome,
            q3_half_total=q3_half_total,
            q3_juice_over=q3_juice_over,
            q3_juice_under=q3_juice_under,
            q3_half_tt_away=q3_half_tt_away,
            q3_half_juice_over_away=q3_half_juice_over_away,
            q3_half_juice_under_away=q3_half_juice_under_away,
            q3_half_tt_home=q3_half_tt_home,
            q3_half_juice_over_home=q3_half_juice_over_home,
            q3_half_juice_under_home=q3_half_juice_under_home,
            q3_half_final_score_away=q3_half_final_score_away,
            q3_half_final_score_home=q3_half_final_score_home,
            # ---
            q4_half_spread_away=q4_half_spread_away,
            q4_half_spread_home=q4_half_spread_home,
            q4_half_juice_spread_away=q4_half_juice_spread_away,
            q4_half_juice_spread_home=q4_half_juice_spread_home,
            q4_half_moneyLineAway=q4_half_moneyLineAway,
            q4_half_moneyLineHome=q4_half_moneyLineHome,
            q4_half_total=q4_half_total,
            q4_juice_over=q4_juice_over,
            q4_juice_under=q4_juice_under,
            q4_half_tt_away=q4_half_tt_away,
            q4_half_juice_over_away=q4_half_juice_over_away,
            q4_half_juice_under_away=q4_half_juice_under_away,
            q4_half_tt_home=q4_half_tt_home,
            q4_half_juice_over_home=q4_half_juice_over_home,
            q4_half_juice_under_home=q4_half_juice_under_home,
            q4_half_final_score_away=q4_half_final_score_away,
            q4_half_final_score_home=q4_half_final_score_home
        )
        db.session.add(nfl)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200


@app.route('/boxeo', methods=['POST'])
def createBoxFight():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_number = request.json.get("rotation_number", None)
    event = request.json.get("event", None)
    rounds = request.json.get("rounds", None)
    location_Fight = request.json.get("location_Fight", None)
    fighter_One = request.json.get("fighter_One", None)
    money_Line_One = request.json.get("money_Line_One", None)
    fighter_Two = request.json.get("fighter_Two", None)
    money_Line_Two = request.json.get("money_Line_Two", None)
    winner = request.json.get("winner", None)
    finish_by = request.json.get("finish_by", None)

    r1_result = request.json.get("r1_result", None)
    r2_result = request.json.get("r2_result", None)
    r3_result = request.json.get("r3_result", None)
    r4_result = request.json.get("r4_result", None)
    r5_result = request.json.get("r5_result", None)
    r6_result = request.json.get("r6_result", None)
    r7_result = request.json.get("r7_result", None)
    r8_result = request.json.get("r8_result", None)
    r9_result = request.json.get("r9_result", None)
    r10_result = request.json.get("r10_result", None)
    r11_result = request.json.get("r11_result", None)
    r12_result = request.json.get("r12_result", None)
    r13_result = request.json.get("r13_result", None)
    r14_result = request.json.get("r14_result", None)
    r15_result = request.json.get("r15_result", None)

    # busca mlb en BBDD
    boxeo = Boxeo.query.filter_by(
        fighter_One=fighter_One, fighter_Two=fighter_Two, date=date).first()
    # the mlb was not found on the database
    if boxeo:
        return jsonify({"msg": "Pelea de Box already exists", "status": boxeo.event}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        boxeo = Boxeo(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_number=rotation_number,
            event=event,
            rounds=rounds,
            location_Fight=location_Fight,
            fighter_One=fighter_One,
            money_Line_One=money_Line_One,
            fighter_Two=fighter_Two,
            money_Line_Two=money_Line_Two,
            winner=winner,
            finish_by=finish_by,
            r1_result=r1_result,
            r2_result=r2_result,
            r3_result=r3_result,
            r4_result=r4_result,
            r5_result=r5_result,
            r6_result=r6_result,
            r7_result=r7_result,
            r8_result=r8_result,
            r9_result=r9_result,
            r10_result=r10_result,
            r11_result=r11_result,
            r12_result=r12_result,
            r13_result=r13_result,
            r14_result=r14_result,
            r15_result=r15_result
        )
        db.session.add(boxeo)
        db.session.commit()
        return jsonify({"msg": "Fight created successfully"}), 200


@app.route('/mma', methods=['POST'])
def createMmaFight():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_number = request.json.get("rotation_number", None)
    event = request.json.get("event", None)
    rounds = request.json.get("rounds", None)
    location_Fight = request.json.get("location_Fight", None)
    fighter_One = request.json.get("fighter_One", None)
    money_Line_One = request.json.get("money_Line_One", None)
    fighter_Two = request.json.get("fighter_Two", None)
    money_Line_Two = request.json.get("money_Line_Two", None)
    winner = request.json.get("winner", None)
    finish_by = request.json.get("finish_by", None)

    r1_result = request.json.get("r1_result", None)
    r2_result = request.json.get("r2_result", None)
    r3_result = request.json.get("r3_result", None)
    r4_result = request.json.get("r4_result", None)
    r5_result = request.json.get("r5_result", None)
    r6_result = request.json.get("r6_result", None)
    r7_result = request.json.get("r7_result", None)
    r8_result = request.json.get("r8_result", None)
    r9_result = request.json.get("r9_result", None)
    r10_result = request.json.get("r10_result", None)
    r11_result = request.json.get("r11_result", None)
    r12_result = request.json.get("r12_result", None)
    r13_result = request.json.get("r13_result", None)
    r14_result = request.json.get("r14_result", None)
    r15_result = request.json.get("r15_result", None)

    # busca mlb en BBDD
    mma = Mma.query.filter_by(fighter_One=fighter_One,
                              fighter_Two=fighter_Two, date=date).first()
    # the mlb was not found on the database
    if mma:
        return jsonify({"msg": "Pelea de Box already exists", "status": mma.event}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        mma = Mma(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_number=rotation_number,
            event=event,
            rounds=rounds,
            location_Fight=location_Fight,
            fighter_One=fighter_One,
            money_Line_One=money_Line_One,
            fighter_Two=fighter_Two,
            money_Line_Two=money_Line_Two,
            winner=winner,
            finish_by=finish_by,
            r1_result=r1_result,
            r2_result=r2_result,
            r3_result=r3_result,
            r4_result=r4_result,
            r5_result=r5_result,
            r6_result=r6_result,
            r7_result=r7_result,
            r8_result=r8_result,
            r9_result=r9_result,
            r10_result=r10_result,
            r11_result=r11_result,
            r12_result=r12_result,
            r13_result=r13_result,
            r14_result=r14_result,
            r15_result=r15_result
        )
        db.session.add(mma)
        db.session.commit()
        return jsonify({"msg": "Fight created successfully"}), 200


@app.route('/nascar', methods=['POST'])
def createNacarRun():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_number = request.json.get("rotation_number", None)
    race = request.json.get("race", None)
    event = request.json.get("event", None)
    track = request.json.get("track", None)
    rounds = request.json.get("rounds", None)
    location = request.json.get("location", None)
    place1 = request.json.get("place1", None)
    place2 = request.json.get("place2", None)
    place3 = request.json.get("place3", None)

    # busca mlb en BBDD
    nascar = Nascar.query.filter_by(
        race=race, place1=place1, date=date).first()
    # the mlb was not found on the database
    if nascar:
        return jsonify({"msg": "Carrera de Nscar already exists", "status": nascar.race}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nascar = Nascar(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_number=rotation_number,
            race=race,
            event=event,
            track=track,
            location=location,
            place1=place1,
            place2=place2,
            place3=place3,
        )
        db.session.add(nascar)
        db.session.commit()
        return jsonify({"msg": "Fight created successfully"}), 200

@app.route('/nascar_drivers', methods=['POST'])
def createNacarDrivers():
    name = request.json.get("name", None)
    country = request.json.get("country", None)
    birth = request.json.get("birth", None)
    headshot = request.json.get("headshot", None)
    sponsor = request.json.get("sponsor", None)
    engine = request.json.get("engine", None)
    number_car = request.json.get("number_car", None)
    rank = request.json.get("rank", None)
    starts = request.json.get("starts", None)
    poles = request.json.get("poles", None)
    top5 = request.json.get("top5", None)
    top10 = request.json.get("top10", None)
    laps_lead = request.json.get("laps_lead", None)
    pts = request.json.get("pts", None)
    AVG_laps = request.json.get("AVG_laps", None)
    AVG_finish = request.json.get("AVG_finish", None)

    # busca mlb en BBDD
    nascar_drivers = Nascar_drivers.query.filter_by(
        engine=engine, number_car=number_car, name=name).first()
    # the mlb was not found on the database
    if nascar_drivers:
        return jsonify({"msg": "Nascar Driver already exists", "name": nascar_drivers.name}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        nascar_drivers = Nascar_drivers(
            name=name,
            country=country,
            birth=birth,
            headshot=headshot,
            sponsor=sponsor,
            engine=engine,
            number_car=number_car,
            rank=rank,
            starts=starts,
            poles=poles,
            top5=top5,
            top10=top10,
            laps_lead=laps_lead,
            pts=pts,
            AVG_laps=AVG_laps,
            AVG_finish=AVG_finish,
        )
        db.session.add(nascar_drivers)
        db.session.commit()
        return jsonify({"msg": "Nascar Driver created successfully"}), 200

@app.route('/moto_gp_drivers', methods=['POST'])
def createMoto_gp_drivers():
    name = request.json.get("name", None)
    country = request.json.get("country", None)
    birth = request.json.get("birth", None)
    headshot = request.json.get("headshot", None)
    sponsor = request.json.get("sponsor", None)
    engine = request.json.get("engine", None)
    number_car = request.json.get("number_car", None)
    rank = request.json.get("rank", None)
    starts = request.json.get("starts", None)
    poles = request.json.get("poles", None)
    top5 = request.json.get("top5", None)
    top10 = request.json.get("top10", None)
    laps_lead = request.json.get("laps_lead", None)
    pts = request.json.get("pts", None)
    AVG_laps = request.json.get("AVG_laps", None)
    AVG_finish = request.json.get("AVG_finish", None)

    # busca mlb en BBDD
    moto_gp_drivers = Moto_gp_drivers.query.filter_by(
        engine=engine, number_car=number_car, name=name).first()
    # the mlb was not found on the database
    if moto_gp_drivers:
        return jsonify({"msg": "Moto GP Driver already exists", "name": moto_gp_drivers.name}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        moto_gp_drivers = Moto_gp_drivers(
            name=name,
            country=country,
            birth=birth,
            headshot=headshot,
            sponsor=sponsor,
            engine=engine,
            number_car=number_car,
            rank=rank,
            starts=starts,
            poles=poles,
            top5=top5,
            top10=top10,
            laps_lead=laps_lead,
            pts=pts,
            AVG_laps=AVG_laps,
            AVG_finish=AVG_finish,
        )
        db.session.add(moto_gp_drivers)
        db.session.commit()
        return jsonify({"msg": "moto Driver created successfully"}), 200

@app.route('/moto_gp', methods=['POST'])
def createMoto_gpRun():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None) 
    rotation_number = request.json.get("rotation_number", None)
    race = request.json.get("race", None)
    track = request.json.get("track", None)
    rounds = request.json.get("rounds", None)
    location = request.json.get("location", None)
    place1 = request.json.get("place1", None)
    place2 = request.json.get("place2", None)
    place3 = request.json.get("place3", None)

    # busca mlb en BBDD
    moto_gp = Moto_GP.query.filter_by(
        race=race, place1=place1, date=date).first()
    # the mlb was not found on the database
    if moto_gp:
        return jsonify({"msg": "Carrera ya existe already exists", "status": moto_gp.race}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        moto_gp = Moto_GP(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_number=rotation_number,
            race=race,
            track=track,
            location=location,
            place1=place1,
            place2=place2,
            place3=place3,
        )
        db.session.add(moto_gp)
        db.session.commit()
        return jsonify({"msg": "moto_gp created successfully"}), 200

@app.route('/match_ups_nascar', methods=['POST'])
def createNacarMatch():
    name1 = request.json.get("name1", None)
    mu1 = request.json.get("mu1", None)
    name2 = request.json.get("name2", None)
    mu2 = request.json.get("mu2", None)

    # busca mlb en BBDD
    match_ups_nascar = Match_Ups_Nacar.query.filter_by(
        name1=name1, name2=name2).first()
    # the mlb was not found on the database
    if match_ups_nascar:
        return jsonify({"msg": "Nascar Driver already exists", "name1": match_ups_nascar.name1}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        match_ups_nascar = Match_Ups_Nacar(
            name1=name1,
            mu1=mu1,
            name2=name2,
            mu2=mu2,
        )
        db.session.add(match_ups_nascar)
        db.session.commit()
        return jsonify({"msg": "Nascar Driver created successfully"}), 200


@app.route('/golf', methods=['POST'])
def createGolfMatch():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_number = request.json.get("rotation_number", None)
    event = request.json.get("event", None)
    location = request.json.get("location", None)
    place1 = request.json.get("place1", None)
    place2 = request.json.get("place2", None)
    place3 = request.json.get("place3", None)

    # busca mlb en BBDD
    golf = Golf.query.filter_by(
        date=date, event=event).first()
    # the mlb was not found on the database
    if golf:
        return jsonify({"msg": "Golf already exists", "name1": golf.event}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        golf = Golf(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_number=rotation_number,
            event=event,
            location=location,
            place1=place1,
            place2=place2,
            place3=place3,
        )
        db.session.add(golf)
        db.session.commit()
        return jsonify({"msg": "Golf created successfully"}), 200


@app.route('/golfer', methods=['POST'])
def createGoler():
    name = request.json.get("name", None)
    country = request.json.get("country", None)
    season = request.json.get("season", None)
    swing = request.json.get("swing", None)
    birth = request.json.get("birth", None)
    headshot = request.json.get("headshot", None)
    cuts = request.json.get("cuts", None)
    top10 = request.json.get("top10", None)
    w = request.json.get("w", None)
    rnds = request.json.get("rnds", None)
    holes = request.json.get("holes", None)
    avg = request.json.get("avg", None)

    # busca mlb en BBDD
    golfer = Golfer.query.filter_by(name=name, birth=birth).first()
    # the mlb was not found on the database
    if golfer:
        return jsonify({"msg": "Golfer already exists", "name1": golfer.cuts}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        golfer = Golfer(
            name=name,
            country=country,
            season=season,
            swing=swing,
            birth=birth,
            headshot=headshot,
            cuts=cuts,
            top10=top10,
            w=w,
            rnds=rnds,
            holes=holes,
            avg=avg
        )
        db.session.add(golfer)
        db.session.commit()
        return jsonify({"msg": "Golfer created successfully"}), 200


@app.route('/ncaa_basketball', methods=['POST'])
def createGameNcaaBasket():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_home = request.json.get("rotation_home", None)
    rotation_away = request.json.get("rotation_away", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_total_over = request.json.get("fh_juice_total_over", None)
    fh_juice_total_under = request.json.get("fh_juice_total_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    # --------------
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("second_half_total", None)
    sh_juice_total_over = request.json.get("sh_juice_total_over", None)
    sh_juice_total_under = request.json.get("sh_juice_total_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    # ------
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)
    # --------
    q2_half_spread_away = request.json.get("q2_half_spread_away", None)
    q2_half_spread_home = request.json.get("q2_half_spread_home", None)
    q2_half_juice_spread_away = request.json.get(
        "q2_half_juice_spread_away", None)
    q2_half_juice_spread_home = request.json.get(
        "q2_half_juice_spread_home", None)
    q2_half_moneyLineAway = request.json.get("q2_half_moneyLineAway", None)
    q2_half_moneyLineHome = request.json.get("q2_half_moneyLineHome", None)
    q2_half_total = request.json.get("q2_half_total", None)
    q2_juice_over = request.json.get("q2_juice_over", None)
    q2_juice_under = request.json.get("q2_juice_under", None)
    q2_half_tt_away = request.json.get("q2_half_tt_away", None)
    q2_half_juice_over_away = request.json.get("q2_half_juice_over_away", None)
    q2_half_juice_under_away = request.json.get(
        "q2_half_juice_under_away", None)
    q2_half_tt_home = request.json.get("q2_half_tt_home", None)
    q2_half_juice_over_home = request.json.get("q2_half_juice_over_home", None)
    q2_half_juice_under_home = request.json.get(
        "q2_half_juice_under_home", None)
    q2_half_final_score_away = request.json.get(
        "q2_half_final_score_away", None)
    q2_half_final_score_home = request.json.get(
        "q2_half_final_score_home", None)
    # --------------
    q3_half_spread_away = request.json.get("q3_half_spread_away", None)
    q3_half_spread_home = request.json.get("q3_half_spread_home", None)
    q3_half_juice_spread_away = request.json.get(
        "q3_half_juice_spread_away", None)
    q3_half_juice_spread_home = request.json.get(
        "q3_half_juice_spread_home", None)
    q3_half_moneyLineAway = request.json.get("q3_half_moneyLineAway", None)
    q3_half_moneyLineHome = request.json.get("q3_half_moneyLineHome", None)
    q3_half_total = request.json.get("q3_half_total", None)
    q3_juice_over = request.json.get("q3_juice_over", None)
    q3_juice_under = request.json.get("q3_juice_under", None)
    q3_half_tt_away = request.json.get("q3_half_tt_away", None)
    q3_half_juice_over_away = request.json.get("q3_half_juice_over_away", None)
    q3_half_juice_under_away = request.json.get(
        "q3_half_juice_under_away", None)
    q3_half_tt_home = request.json.get("q3_half_tt_home", None)
    q3_half_juice_over_home = request.json.get("q3_half_juice_over_home", None)
    q3_half_juice_under_home = request.json.get(
        "q3_half_juice_under_home", None)
    q3_half_final_score_away = request.json.get(
        "q3_half_final_score_away", None)
    q3_half_final_score_home = request.json.get(
        "q3_half_final_score_home", None)
    # --------------
    q4_half_spread_away = request.json.get("q4_half_spread_away", None)
    q4_half_spread_home = request.json.get("q4_half_spread_home", None)
    q4_half_juice_spread_away = request.json.get(
        "q4_half_juice_spread_away", None)
    q4_half_juice_spread_home = request.json.get(
        "q4_half_juice_spread_home", None)
    q4_half_moneyLineAway = request.json.get("q4_half_moneyLineAway", None)
    q4_half_moneyLineHome = request.json.get("q4_half_moneyLineHome", None)
    q4_half_total = request.json.get("q4_half_total", None)
    q4_juice_over = request.json.get("q4_juice_over", None)
    q4_juice_under = request.json.get("q4_juice_under", None)
    q4_half_tt_away = request.json.get("q4_half_tt_away", None)
    q4_half_juice_over_away = request.json.get("q4_half_juice_over_away", None)
    q4_half_juice_under_away = request.json.get(
        "q4_half_juice_under_away", None)
    q4_half_tt_home = request.json.get("q4_half_tt_home", None)
    q4_half_juice_over_home = request.json.get("q4_half_juice_over_home", None)
    q4_half_juice_under_home = request.json.get(
        "q4_half_juice_under_home", None)
    q4_half_final_score_away = request.json.get(
        "q4_half_final_score_away", None)
    q4_half_final_score_home = request.json.get(
        "q4_half_final_score_home", None)

    # busca mlb en BBDD
    ncaa_basketball = Ncaa_Basketball.query.filter_by(
        home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if ncaa_basketball:
        return jsonify({"msg": "Mlb already exists", "status": ncaa_basketball.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        ncaa_basketball = Ncaa_Basketball(
            date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_away=rotation_away,
            rotation_home=rotation_home,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            # --
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_total_over=fh_juice_total_over,
            fh_juice_total_under=fh_juice_total_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away,
            first_half_juice_under_away=first_half_juice_under_away,
            first_half_tt_home=first_half_tt_home,
            first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home,
            # --
            second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_total_over=sh_juice_total_over,
            sh_juice_total_under=sh_juice_total_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            # --
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home,
            # ---
            q2_half_spread_away=q2_half_spread_away,
            q2_half_spread_home=q2_half_spread_home,
            q2_half_juice_spread_away=q2_half_juice_spread_away,
            q2_half_juice_spread_home=q2_half_juice_spread_home,
            q2_half_moneyLineAway=q2_half_moneyLineAway,
            q2_half_moneyLineHome=q2_half_moneyLineHome,
            q2_half_total=q2_half_total,
            q2_juice_over=q2_juice_over,
            q2_juice_under=q2_juice_under,
            q2_half_tt_away=q2_half_tt_away,
            q2_half_juice_over_away=q2_half_juice_over_away,
            q2_half_juice_under_away=q2_half_juice_under_away,
            q2_half_tt_home=q2_half_tt_home,
            q2_half_juice_over_home=q2_half_juice_over_home,
            q2_half_juice_under_home=q2_half_juice_under_home,
            q2_half_final_score_away=q2_half_final_score_away,
            q2_half_final_score_home=q2_half_final_score_home,
            # ---
            q3_half_spread_away=q3_half_spread_away,
            q3_half_spread_home=q3_half_spread_home,
            q3_half_juice_spread_away=q3_half_juice_spread_away,
            q3_half_juice_spread_home=q3_half_juice_spread_home,
            q3_half_moneyLineAway=q3_half_moneyLineAway,
            q3_half_moneyLineHome=q3_half_moneyLineHome,
            q3_half_total=q3_half_total,
            q3_juice_over=q3_juice_over,
            q3_juice_under=q3_juice_under,
            q3_half_tt_away=q3_half_tt_away,
            q3_half_juice_over_away=q3_half_juice_over_away,
            q3_half_juice_under_away=q3_half_juice_under_away,
            q3_half_tt_home=q3_half_tt_home,
            q3_half_juice_over_home=q3_half_juice_over_home,
            q3_half_juice_under_home=q3_half_juice_under_home,
            q3_half_final_score_away=q3_half_final_score_away,
            q3_half_final_score_home=q3_half_final_score_home,
            # ---
            q4_half_spread_away=q4_half_spread_away,
            q4_half_spread_home=q4_half_spread_home,
            q4_half_juice_spread_away=q4_half_juice_spread_away,
            q4_half_juice_spread_home=q4_half_juice_spread_home,
            q4_half_moneyLineAway=q4_half_moneyLineAway,
            q4_half_moneyLineHome=q4_half_moneyLineHome,
            q4_half_total=q4_half_total,
            q4_juice_over=q4_juice_over,
            q4_juice_under=q4_juice_under,
            q4_half_tt_away=q4_half_tt_away,
            q4_half_juice_over_away=q4_half_juice_over_away,
            q4_half_juice_under_away=q4_half_juice_under_away,
            q4_half_tt_home=q4_half_tt_home,
            q4_half_juice_over_home=q4_half_juice_over_home,
            q4_half_juice_under_home=q4_half_juice_under_home,
            q4_half_final_score_away=q4_half_final_score_away,
            q4_half_final_score_home=q4_half_final_score_home
        )
        db.session.add(ncaa_basketball)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200

@app.route('/stats_ncaa_basket_team', methods=['POST'])
def createstats_ncaa_basket_team():
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)

    w = request.json.get("w", None)
    L = request.json.get("L", None)
    ptc = request.json.get("ptc", None)
    gb = request.json.get("gb", None)
    home = request.json.get("home", None)
    away = request.json.get("away", None)
    div = request.json.get("div", None)
    conf = request.json.get("conf", None)
    ppg = request.json.get("ppg", None)
    opp_ppg = request.json.get("opp_ppg", None)
    diff = request.json.get("diff", None)
    strk = request.json.get("strk", None)
    l10 = request.json.get("l10", None)

    # busca team en BBDD
    stats_ncaa_basket_team = Stats_ncaa_basket_team.query.filter_by(team=team).first()
    # the team was not found on the database
    if stats_ncaa_basket_team:
        return jsonify({"msg": "stats_ncaa_basket_team already exists", "team": stats_ncaa_basket_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_ncaa_basket_team = Stats_ncaa_basket_team(
            season=season,
            team=team,
            conference=conference,
            division=division,
            w=w,
            L=L,
            ptc=ptc,
            gb=gb,
            home=home,
            away=away,
            div=div,
            conf=conf,
            ppg=ppg,
            opp_ppg=opp_ppg,
            diff=diff,
            strk=strk,
            l10=l10
        )
        db.session.add(stats_ncaa_basket_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_ncaa_basket_team created successfully"}), 200

@app.route('/stats_ncaa_basket_player', methods=['POST'])
def createstats_ncaa_basket_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    college = request.json.get("college", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)

    dorsal = request.json.get("dorsal", None)
    minutes = request.json.get("minutes", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    gp = request.json.get("gp", None)
    gs = request.json.get("gs", None)
    fg = request.json.get("fg", None)
    fg_AVG = request.json.get("fg_AVG", None)
    three_pt = request.json.get("three_pt", None)
    three_pt_AVG = request.json.get("three_pt_AVG", None)
    ft = request.json.get("ft", None)
    ft_AVG = request.json.get("ft_AVG", None)
    Or = request.json.get("Or", None)
    dr = request.json.get("dr", None)
    reb = request.json.get("reb", None)
    ast = request.json.get("ast", None)
    stl = request.json.get("stl", None)
    blk = request.json.get("blk", None)
    to = request.json.get("to", None)
    pf = request.json.get("pf", None)
    pts = request.json.get("pts", None)
    # busca team en BBDD
    stats_ncaa_basket_player = Stats_ncaa_basket_player.query.filter_by(
        name=name, dorsal=dorsal, team=team).first()
    # the team was not found on the database
    if stats_ncaa_basket_player:
        return jsonify({"msg": "stats_ncaa_basket_player already exists", "name": stats_ncaa_basket_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_ncaa_basket_player = Stats_ncaa_basket_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            college=college,
            season=season,
            team=team,

            dorsal=dorsal,
            minutes=minutes,
            position=position,
            headshot=headshot,
            gp=gp,
            gs=gs,
            fg=fg,
            fg_AVG=fg_AVG,
            three_pt=three_pt,
            three_pt_AVG=three_pt_AVG,
            ft=ft,
            ft_AVG=ft_AVG,
            Or=Or,
            dr=dr,
            reb=reb,
            ast=ast,
            stl=stl,
            blk=blk,
            to=to,
            pf=pf,
            pts=pts
        )
        db.session.add(stats_ncaa_basket_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_ncaa_basket_player created successfully"}), 200


@app.route('/ncaa_baseball', methods=['POST'])
def createGameNcaaBaseBall():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_home = request.json.get("rotation_home", None)
    rotation_away = request.json.get("rotation_away", None)
    away = request.json.get("away", None)
    pitcher_a = request.json.get("pitcher_a", None)
    home = request.json.get("home", None)
    pitcher_h = request.json.get("pitcher_h", None)
    rl_away = request.json.get("rl_away", None)
    rl_home = request.json.get("rl_home", None)
    juice_rl_away = request.json.get("juice_rl_away", None)
    juice_rl_home = request.json.get("juice_rl_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    rl_away_f5 = request.json.get("rl_away_f5", None)
    rl_home_f5 = request.json.get("rl_home_f5", None)
    juice_rl_away_f5 = request.json.get("juice_rl_away_f5", None)
    juice_rl_home_f5 = request.json.get("juice_rl_home_f5", None)
    moneyLineAway_f5 = request.json.get("moneyLineAway_f5", None)
    moneyLineHome_f5 = request.json.get("moneyLineHome_f5", None)
    total_f5 = request.json.get("total_f5", None)
    juice_total_over_f5 = request.json.get("juice_total_over_f5", None)
    juice_total_under_f5 = request.json.get("juice_total_under_f5", None)
    tt_away_f5 = request.json.get("tt_away_f5", None)
    juice_over_away_f5 = request.json.get("juice_over_away_f5", None)
    juice_under_away_f5 = request.json.get("juice_under_away_f5", None)
    juice_over_home_f5 = request.json.get("juice_over_home_f5", None)
    juice_under_home_f5 = request.json.get("juice_under_home_f5", None)
    fs_away_f5 = request.json.get("fs_away_f5", None)
    fs_home_f5 = request.json.get("fs_home_f5", None)
    sa_1inning = request.json.get("sa_1inning", None)
    sh_1inning = request.json.get("sh_1inning", None)
    sa_2inning = request.json.get("sa_2inning", None)
    sh_2inning = request.json.get("sh_2inning", None)
    sa_3inning = request.json.get("sa_3inning", None)
    sh_3inning = request.json.get("sh_3inning", None)
    sa_4inning = request.json.get("sa_4inning", None)
    sh_4inning = request.json.get("sh_4inning", None)
    sa_5inning = request.json.get("sa_5inning", None)
    sh_5inning = request.json.get("sh_5inning", None)
    sa_6inning = request.json.get("sa_6inning", None)
    sh_6inning = request.json.get("sh_6inning", None)
    sa_7inning = request.json.get("sa_7inning", None)
    sh_7inning = request.json.get("sh_7inning", None)
    sa_8inning = request.json.get("sa_8inning", None)
    sh_8inning = request.json.get("sh_8inning", None)
    sa_9inning = request.json.get("sa_9inning", None)
    sh_9inning = request.json.get("sh_9inning", None)
    sa_10inning = request.json.get("sa_10inning", None)
    sh_10inning = request.json.get("sh_10inning", None)
    sa_11inning = request.json.get("sa_11inning", None)
    sh_11inning = request.json.get("sh_11inning", None)
    sa_12inning = request.json.get("sa_12inning", None)
    sh_12inning = request.json.get("sh_12inning", None)
    sa_13inning = request.json.get("sa_13inning", None)
    sh_13inning = request.json.get("sh_13inning", None)
    sa_14inning = request.json.get("sa_14inning", None)
    sh_14inning = request.json.get("sh_14inning", None)
    sa_15inning = request.json.get("sa_15inning", None)
    sh_15inning = request.json.get("sh_15inning", None)
    sa_16inning = request.json.get("sa_16inning", None)
    sh_16inning = request.json.get("sh_16inning", None)
    sa_17inning = request.json.get("sa_17inning", None)
    sh_17inning = request.json.get("sh_17inning", None)
    sa_18inning = request.json.get("sa_18inning", None)
    sh_18inning = request.json.get("sh_18inning", None)
    sa_19inning = request.json.get("sa_19inning", None)
    sh_19inning = request.json.get("sh_19inning", None)
    sa_20inning = request.json.get("sa_20inning", None)
    sh_20inning = request.json.get("sh_20inning", None)
    sa_21inning = request.json.get("sa_21inning", None)
    sh_21inning = request.json.get("sh_21inning", None)
    sa_22inning = request.json.get("sa_22inning", None)
    sh_22inning = request.json.get("sh_22inning", None)
    sa_23inning = request.json.get("sa_23inning", None)
    sh_23inning = request.json.get("sh_23inning", None)
    sa_24inning = request.json.get("sa_24inning", None)
    sh_24inning = request.json.get("sh_24inning", None)
    sa_25inning = request.json.get("sa_25inning", None)
    sh_25inning = request.json.get("sh_25inning", None)

    # busca mlb en BBDD
    ncaa_baseball = Ncaa_Baseball.query.filter_by(
        home=home, away=away, date=date).first()
    # the ncaa_baseball was not found on the database
    if ncaa_baseball:
        return jsonify({"msg": "ncaa_baseball already exists", "status": ncaa_baseball.status}), 401
    else:
        # crea ncaa_baseball nuevo
        # crea registro nuevo en BBDD de
        ncaa_baseball = Ncaa_Baseball(
            date=date, 
            hour=hour, 
            status=status, 
            rotation_away=rotation_away, 
            rotation_home=rotation_home, 
            casino=casino, 
            away=away, 
            pitcher_a=pitcher_a, 
            home=home, 
            pitcher_h=pitcher_h,
            rl_away=rl_away, 
            rl_home=rl_home, 
            juice_rl_away=juice_rl_away, 
            juice_rl_home=juice_rl_home,         
            moneyLineAway=moneyLineAway, 
            moneyLineHome=moneyLineHome, 
            total=total, 
            juice_total_over=juice_total_over, 
            juice_total_under=juice_total_under, 
            tt_away=tt_away, 
            juice_over_away=juice_over_away, 
            juice_under_away=juice_under_away, 
            tt_home=tt_home, 
            juice_over_home=juice_over_home, 
            juice_under_home=juice_under_home, 
            final_score_away=final_score_away, 
            final_score_home=final_score_home, 
            rl_away_f5=rl_away_f5, 
            rl_home_f5=rl_home_f5, 
            juice_rl_away_f5=juice_rl_away_f5, 
            juice_rl_home_f5=juice_rl_home_f5, 
            moneyLineAway_f5=moneyLineAway_f5, 
            moneyLineHome_f5=moneyLineHome_f5, 
            total_f5=total_f5, 
            juice_total_over_f5=juice_total_over_f5, 
            juice_total_under_f5=juice_total_under_f5, 
            tt_away_f5=tt_away_f5, 
            juice_over_away_f5=juice_over_away_f5, 
            juice_under_away_f5=juice_under_away_f5, 
            juice_over_home_f5=juice_over_home_f5, 
            juice_under_home_f5=juice_under_home_f5, 
            fs_away_f5=fs_away_f5,
            fs_home_f5=fs_home_f5, 
            sa_1inning=sa_1inning, sh_1inning=sh_1inning, sa_2inning=sa_2inning, sh_2inning=sh_2inning, sa_3inning=sa_3inning, sh_3inning=sh_3inning, sa_4inning=sa_4inning, sh_4inning=sh_4inning, sa_5inning=sa_5inning, sh_5inning=sh_5inning, sa_6inning=sa_6inning, sh_6inning=sh_6inning, sa_7inning=sa_7inning, sh_7inning=sh_7inning, sa_8inning=sa_8inning, sh_8inning=sh_8inning, sa_9inning=sa_9inning, sh_9inning=sh_9inning, sa_10inning=sa_10inning, sh_10inning=sh_10inning, sa_11inning=sa_11inning, sh_11inning=sh_11inning, sa_12inning=sa_12inning, sh_12inning=sh_12inning, sa_13inning=sa_13inning, sh_13inning=sh_13inning, sa_14inning=sa_14inning, sh_14inning=sh_14inning, sa_15inning=sa_15inning, sh_15inning=sh_15inning, sa_16inning=sa_16inning, sh_16inning=sh_16inning, sa_17inning=sa_17inning, sa_18inning=sa_18inning, sa_19inning=sa_19inning, sa_20inning=sa_20inning, sa_21inning=sa_21inning, sa_22inning=sa_22inning, sa_23inning=sa_23inning, sa_24inning=sa_24inning, sa_25inning=sa_25inning)
        db.session.add(ncaa_baseball)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200

@app.route('/stats_ncaa_baseball_team', methods=['POST'])
def createstats_ncaa_baseball_team():
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    league = request.json.get("league", None)
    division = request.json.get("division", None)
    w = request.json.get("w", None)
    L = request.json.get("L", None)
    pct = request.json.get("pct", None)
    gb = request.json.get("gb", None)
    home = request.json.get("home", None)
    away = request.json.get("away", None)
    rs = request.json.get("rs", None)
    ra = request.json.get("ra", None)
    diff = request.json.get("diff", None)
    strk = request.json.get("strk", None)
    L10 = request.json.get("L10", None)
    poff = request.json.get("poff", None)

    # busca team en BBDD
    stats_ncaa_baseball_team = Stats_ncaa_baseball_team.query.filter_by(
        team=team, league=league, division=division).first()
    # the team was not found on the database
    if stats_ncaa_baseball_team:
        return jsonify({"msg": "stats_ncaa_baseball_team already exists", "team": stats_ncaa_baseball_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_ncaa_baseball_team = Stats_ncaa_baseball_team(
            season=season,
            team=team,
            league=league,
            division=division,
            w=w,
            L=L,
            pct=pct,
            gb=gb,
            home=home,
            away=away,
            rs=rs,
            ra=ra,
            diff=diff,
            strk=strk,
            L10=L10,
            poff=poff
        )
        db.session.add(stats_ncaa_baseball_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_ncaa_baseball_team created successfully"}), 200

@app.route('/stats_ncaa_baseball_player', methods=['POST'])
def createstats_ncaa_baseball_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    dorsal = request.json.get("dorsal", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)

    gp = request.json.get("gp", None)
    ab = request.json.get("ab", None)
    r = request.json.get("r", None)
    h = request.json.get("h", None)
    two_b = request.json.get("two_b", None)
    three_b = request.json.get("three_b", None)
    hb = request.json.get("hb", None)
    rbi = request.json.get("rbi", None)
    tb = request.json.get("tb", None)
    bb = request.json.get("bb", None)
    so = request.json.get("so", None)
    sb = request.json.get("sb", None)
    avg = request.json.get("avg", None)
    obp = request.json.get("obp", None)
    slg = request.json.get("slg", None)
    ops = request.json.get("ops", None)
    war = request.json.get("war", None)

    # busca team en BBDD
    stats_ncaa_baseball_player = Stats_ncaa_baseball_player.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_ncaa_baseball_player:
        return jsonify({"msg": "stats_ncaa_baseball_player already exists", "name": stats_ncaa_baseball_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_ncaa_baseball_player = Stats_ncaa_baseball_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            season=season,
            team=team,
            dorsal=dorsal,
            position=position,
            headshot=headshot,
            gp=gp,
            ab=ab,
            r=r,
            h=h,
            two_b=two_b,
            three_b=three_b,
            hb=hb,
            rbi=rbi,
            tb=tb,
            bb=bb,
            so=so,
            sb=sb,
            avg=avg,
            obp=obp,
            slg=slg,
            ops=ops,
            war=war
        )
        db.session.add(stats_ncaa_baseball_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_ncaa_baseball_player created successfully"}), 200

@app.route('/stats_ncaa_baseball_player/<id>', methods=['PUT'])
def stats_ncaa_baseball_playerEdit(id):
    stats_ncaa_baseball_player = Stats_ncaa_baseball_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    position = request.json['position']
    headshot = request.json['headshot']
    gp = request.json['gp']
    ab = request.json['ab']
    r = request.json['r']
    h = request.json['h']
    two_b = request.json['two_b']
    three_b = request.json['three_b']
    hb = request.json['hb']
    rbi = request.json['rbi']
    tb = request.json['tb']
    bb = request.json['bb']
    so = request.json['so']
    sb = request.json['sb']
    avg = request.json['avg']
    obp = request.json['obp']
    slg = request.json['slg']
    ops = request.json['ops']
    war = request.json['war']

    stats_ncaa_baseball_player.name = name
    stats_ncaa_baseball_player.height = height
    stats_ncaa_baseball_player.weight = weight
    stats_ncaa_baseball_player.birth = birth
    stats_ncaa_baseball_player.season = season
    stats_ncaa_baseball_player.team = team
    stats_ncaa_baseball_player.dorsal = dorsal
    stats_ncaa_baseball_player.position = position
    stats_ncaa_baseball_player.headshot = headshot
    stats_ncaa_baseball_player.gp = gp
    stats_ncaa_baseball_player.ab = ab
    stats_ncaa_baseball_player.r = r
    stats_ncaa_baseball_player.h = h
    stats_ncaa_baseball_player.two_b = two_b
    stats_ncaa_baseball_player.three_b = three_b
    stats_ncaa_baseball_player.hb = hb
    stats_ncaa_baseball_player.rbi = rbi
    stats_ncaa_baseball_player.tb = tb
    stats_ncaa_baseball_player.bb = bb
    stats_ncaa_baseball_player.so = so
    stats_ncaa_baseball_player.sb = sb
    stats_ncaa_baseball_player.avg = avg
    stats_ncaa_baseball_player.obp = obp
    stats_ncaa_baseball_player.slg = slg
    stats_ncaa_baseball_player.ops = ops
    stats_ncaa_baseball_player.war = war

    db.session.commit()
    return jsonify({"msg": "stats_ncaa_baseball_player edith successfully"}), 200


@app.route('/ncaa_football', methods=['POST'])
def createGameNcaa_football():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    week = request.json.get("week", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    rotation_home = request.json.get("rotation_home", None)
    rotation_away = request.json.get("rotation_away", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    spread_away = request.json.get("spread_away", None)
    spread_home = request.json.get("spread_home", None)
    juice_spread_away = request.json.get("juice_spread_away", None)
    juice_spread_home = request.json.get("juice_spread_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)
    # --------------------------------------------------------------
    first_half_spread_away = request.json.get("first_half_spread_away", None)
    first_half_spread_home = request.json.get("first_half_spread_home", None)
    first_half_juice_spread_away = request.json.get(
        "first_half_juice_spread_away", None)
    first_half_juice_spread_home = request.json.get(
        "first_half_juice_spread_home", None)
    first_half_moneyLineAway = request.json.get(
        "first_half_moneyLineAway", None)
    first_half_moneyLineHome = request.json.get(
        "first_half_moneyLineHome", None)
    first_half_total = request.json.get("first_half_total", None)
    fh_juice_total_over = request.json.get("fh_juice_total_over", None)
    fh_juice_total_under = request.json.get("fh_juice_total_under", None)
    first_half_tt_away = request.json.get("first_half_tt_away", None)
    first_half_juice_over_away = request.json.get(
        "first_half_juice_over_away", None)
    first_half_juice_under_away = request.json.get(
        "first_half_juice_under_away", None)
    first_half_tt_home = request.json.get("first_half_tt_home", None)
    first_half_juice_over_home = request.json.get(
        "first_half_juice_over_home", None)
    first_half_juice_under_home = request.json.get(
        "first_half_juice_under_home", None)
    first_half_final_score_away = request.json.get(
        "first_half_final_score_away", None)
    first_half_final_score_home = request.json.get(
        "first_half_final_score_home", None)
    # --------------
    second_half_spread_away = request.json.get("second_half_spread_away", None)
    second_half_spread_home = request.json.get("second_half_spread_home", None)
    second_half_juice_spread_away = request.json.get(
        "second_half_juice_spread_away", None)
    second_half_juice_spread_home = request.json.get(
        "second_half_juice_spread_home", None)
    second_half_moneyLineAway = request.json.get(
        "second_half_moneyLineAway", None)
    second_half_moneyLineHome = request.json.get(
        "second_half_moneyLineHome", None)
    second_half_total = request.json.get("second_half_total", None)
    sh_juice_total_over = request.json.get("sh_juice_total_over", None)
    sh_juice_total_under = request.json.get("sh_juice_total_under", None)
    second_half_tt_away = request.json.get("second_half_tt_away", None)
    second_half_juice_over_away = request.json.get(
        "second_half_juice_over_away", None)
    second_half_juice_under_away = request.json.get(
        "second_half_juice_under_away", None)
    second_half_tt_home = request.json.get("second_half_tt_home", None)
    second_half_juice_over_home = request.json.get(
        "second_half_juice_over_home", None)
    second_half_juice_under_home = request.json.get(
        "second_half_juice_under_home", None)
    second_half_final_score_away = request.json.get(
        "second_half_final_score_away", None)
    second_half_final_score_home = request.json.get(
        "second_half_final_score_home", None)
    # ------
    q1_half_spread_away = request.json.get("q1_half_spread_away", None)
    q1_half_spread_home = request.json.get("q1_half_spread_home", None)
    q1_half_juice_spread_away = request.json.get(
        "q1_half_juice_spread_away", None)
    q1_half_juice_spread_home = request.json.get(
        "q1_half_juice_spread_home", None)
    q1_half_moneyLineAway = request.json.get("q1_half_moneyLineAway", None)
    q1_half_moneyLineHome = request.json.get("q1_half_moneyLineHome", None)
    q1_half_total = request.json.get("q1_half_total", None)
    q1_juice_over = request.json.get("q1_juice_over", None)
    q1_juice_under = request.json.get("q1_juice_under", None)
    q1_half_tt_away = request.json.get("q1_half_tt_away", None)
    q1_half_juice_over_away = request.json.get("q1_half_juice_over_away", None)
    q1_half_juice_under_away = request.json.get(
        "q1_half_juice_under_away", None)
    q1_half_tt_home = request.json.get("q1_half_tt_home", None)
    q1_half_juice_over_home = request.json.get("q1_half_juice_over_home", None)
    q1_half_juice_under_home = request.json.get(
        "q1_half_juice_under_home", None)
    q1_half_final_score_away = request.json.get(
        "q1_half_final_score_away", None)
    q1_half_final_score_home = request.json.get(
        "q1_half_final_score_home", None)
    # --------
    q2_half_spread_away = request.json.get("q2_half_spread_away", None)
    q2_half_spread_home = request.json.get("q2_half_spread_home", None)
    q2_half_juice_spread_away = request.json.get(
        "q2_half_juice_spread_away", None)
    q2_half_juice_spread_home = request.json.get(
        "q2_half_juice_spread_home", None)
    q2_half_moneyLineAway = request.json.get("q2_half_moneyLineAway", None)
    q2_half_moneyLineHome = request.json.get("q2_half_moneyLineHome", None)
    q2_half_total = request.json.get("q2_half_total", None)
    q2_juice_over = request.json.get("q2_juice_over", None)
    q2_juice_under = request.json.get("q2_juice_under", None)
    q2_half_tt_away = request.json.get("q2_half_tt_away", None)
    q2_half_juice_over_away = request.json.get("q2_half_juice_over_away", None)
    q2_half_juice_under_away = request.json.get(
        "q2_half_juice_under_away", None)
    q2_half_tt_home = request.json.get("q2_half_tt_home", None)
    q2_half_juice_over_home = request.json.get("q2_half_juice_over_home", None)
    q2_half_juice_under_home = request.json.get(
        "q2_half_juice_under_home", None)
    q2_half_final_score_away = request.json.get(
        "q2_half_final_score_away", None)
    q2_half_final_score_home = request.json.get(
        "q2_half_final_score_home", None)
    # --------------
    q3_half_spread_away = request.json.get("q3_half_spread_away", None)
    q3_half_spread_home = request.json.get("q3_half_spread_home", None)
    q3_half_juice_spread_away = request.json.get(
        "q3_half_juice_spread_away", None)
    q3_half_juice_spread_home = request.json.get(
        "q3_half_juice_spread_home", None)
    q3_half_moneyLineAway = request.json.get("q3_half_moneyLineAway", None)
    q3_half_moneyLineHome = request.json.get("q3_half_moneyLineHome", None)
    q3_half_total = request.json.get("q3_half_total", None)
    q3_juice_over = request.json.get("q3_juice_over", None)
    q3_juice_under = request.json.get("q3_juice_under", None)
    q3_half_tt_away = request.json.get("q3_half_tt_away", None)
    q3_half_juice_over_away = request.json.get("q3_half_juice_over_away", None)
    q3_half_juice_under_away = request.json.get(
        "q3_half_juice_under_away", None)
    q3_half_tt_home = request.json.get("q3_half_tt_home", None)
    q3_half_juice_over_home = request.json.get("q3_half_juice_over_home", None)
    q3_half_juice_under_home = request.json.get(
        "q3_half_juice_under_home", None)
    q3_half_final_score_away = request.json.get(
        "q3_half_final_score_away", None)
    q3_half_final_score_home = request.json.get(
        "q3_half_final_score_home", None)
    # --------------
    q4_half_spread_away = request.json.get("q4_half_spread_away", None)
    q4_half_spread_home = request.json.get("q4_half_spread_home", None)
    q4_half_juice_spread_away = request.json.get(
        "q4_half_juice_spread_away", None)
    q4_half_juice_spread_home = request.json.get(
        "q4_half_juice_spread_home", None)
    q4_half_moneyLineAway = request.json.get("q4_half_moneyLineAway", None)
    q4_half_moneyLineHome = request.json.get("q4_half_moneyLineHome", None)
    q4_half_total = request.json.get("q4_half_total", None)
    q4_juice_over = request.json.get("q4_juice_over", None)
    q4_juice_under = request.json.get("q4_juice_under", None)
    q4_half_tt_away = request.json.get("q4_half_tt_away", None)
    q4_half_juice_over_away = request.json.get("q4_half_juice_over_away", None)
    q4_half_juice_under_away = request.json.get(
        "q4_half_juice_under_away", None)
    q4_half_tt_home = request.json.get("q4_half_tt_home", None)
    q4_half_juice_over_home = request.json.get("q4_half_juice_over_home", None)
    q4_half_juice_under_home = request.json.get(
        "q4_half_juice_under_home", None)
    q4_half_final_score_away = request.json.get(
        "q4_half_final_score_away", None)
    q4_half_final_score_home = request.json.get(
        "q4_half_final_score_home", None)

    # busca mlb en BBDD
    ncaa_football = Ncaa_Football.query.filter_by(
        home=home, away=away, date=date).first()
    # the mlb was not found on the database
    if ncaa_football:
        return jsonify({"msg": "Ncaa_Football game already exists", "status": ncaa_football.status}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        ncaa_football = Ncaa_Football(
             date=date,
            hour=hour,
            week=week,
            status=status,
            casino=casino,
            rotation_home=rotation_home,
            rotation_away=rotation_away,
            away=away,
            home=home,
            spread_away=spread_away,
            spread_home=spread_home,
            juice_spread_away=juice_spread_away,
            juice_spread_home=juice_spread_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,
            # --
            first_half_spread_away=first_half_spread_away,
            first_half_spread_home=first_half_spread_home,
            first_half_juice_spread_away=first_half_juice_spread_away,
            first_half_juice_spread_home=first_half_juice_spread_home,
            first_half_moneyLineAway=first_half_moneyLineAway,
            first_half_moneyLineHome=first_half_moneyLineHome,
            first_half_total=first_half_total,
            fh_juice_total_over=fh_juice_total_over,
            fh_juice_total_under=fh_juice_total_under,
            first_half_tt_away=first_half_tt_away,
            first_half_juice_over_away=first_half_juice_over_away,
            first_half_juice_under_away=first_half_juice_under_away,
            first_half_tt_home=first_half_tt_home,
            first_half_juice_over_home=first_half_juice_over_home,
            first_half_juice_under_home=first_half_juice_under_home,
            first_half_final_score_away=first_half_final_score_away,
            first_half_final_score_home=first_half_final_score_home,
            # --
            second_half_spread_away=second_half_spread_away,
            second_half_spread_home=second_half_spread_home,
            second_half_juice_spread_away=second_half_juice_spread_away,
            second_half_juice_spread_home=second_half_juice_spread_home,
            second_half_moneyLineAway=second_half_moneyLineAway,
            second_half_moneyLineHome=second_half_moneyLineHome,
            second_half_total=second_half_total,
            sh_juice_total_over=sh_juice_total_over,
            sh_juice_total_under=sh_juice_total_under,
            second_half_tt_away=second_half_tt_away,
            second_half_juice_over_away=second_half_juice_over_away,
            second_half_juice_under_away=second_half_juice_under_away,
            second_half_tt_home=second_half_tt_home,
            second_half_juice_over_home=second_half_juice_over_home,
            second_half_juice_under_home=second_half_juice_under_home,
            second_half_final_score_away=second_half_final_score_away,
            second_half_final_score_home=second_half_final_score_home,
            # --
            q1_half_spread_away=q1_half_spread_away,
            q1_half_spread_home=q1_half_spread_home,
            q1_half_juice_spread_away=q1_half_juice_spread_away,
            q1_half_juice_spread_home=q1_half_juice_spread_home,
            q1_half_moneyLineAway=q1_half_moneyLineAway,
            q1_half_moneyLineHome=q1_half_moneyLineHome,
            q1_half_total=q1_half_total,
            q1_juice_over=q1_juice_over,
            q1_juice_under=q1_juice_under,
            q1_half_tt_away=q1_half_tt_away,
            q1_half_juice_over_away=q1_half_juice_over_away,
            q1_half_juice_under_away=q1_half_juice_under_away,
            q1_half_tt_home=q1_half_tt_home,
            q1_half_juice_over_home=q1_half_juice_over_home,
            q1_half_juice_under_home=q1_half_juice_under_home,
            q1_half_final_score_away=q1_half_final_score_away,
            q1_half_final_score_home=q1_half_final_score_home,
            # ---
            q2_half_spread_away=q2_half_spread_away,
            q2_half_spread_home=q2_half_spread_home,
            q2_half_juice_spread_away=q2_half_juice_spread_away,
            q2_half_juice_spread_home=q2_half_juice_spread_home,
            q2_half_moneyLineAway=q2_half_moneyLineAway,
            q2_half_moneyLineHome=q2_half_moneyLineHome,
            q2_half_total=q2_half_total,
            q2_juice_over=q2_juice_over,
            q2_juice_under=q2_juice_under,
            q2_half_tt_away=q2_half_tt_away,
            q2_half_juice_over_away=q2_half_juice_over_away,
            q2_half_juice_under_away=q2_half_juice_under_away,
            q2_half_tt_home=q2_half_tt_home,
            q2_half_juice_over_home=q2_half_juice_over_home,
            q2_half_juice_under_home=q2_half_juice_under_home,
            q2_half_final_score_away=q2_half_final_score_away,
            q2_half_final_score_home=q2_half_final_score_home,
            # ---
            q3_half_spread_away=q3_half_spread_away,
            q3_half_spread_home=q3_half_spread_home,
            q3_half_juice_spread_away=q3_half_juice_spread_away,
            q3_half_juice_spread_home=q3_half_juice_spread_home,
            q3_half_moneyLineAway=q3_half_moneyLineAway,
            q3_half_moneyLineHome=q3_half_moneyLineHome,
            q3_half_total=q3_half_total,
            q3_juice_over=q3_juice_over,
            q3_juice_under=q3_juice_under,
            q3_half_tt_away=q3_half_tt_away,
            q3_half_juice_over_away=q3_half_juice_over_away,
            q3_half_juice_under_away=q3_half_juice_under_away,
            q3_half_tt_home=q3_half_tt_home,
            q3_half_juice_over_home=q3_half_juice_over_home,
            q3_half_juice_under_home=q3_half_juice_under_home,
            q3_half_final_score_away=q3_half_final_score_away,
            q3_half_final_score_home=q3_half_final_score_home,
            # ---
            q4_half_spread_away=q4_half_spread_away,
            q4_half_spread_home=q4_half_spread_home,
            q4_half_juice_spread_away=q4_half_juice_spread_away,
            q4_half_juice_spread_home=q4_half_juice_spread_home,
            q4_half_moneyLineAway=q4_half_moneyLineAway,
            q4_half_moneyLineHome=q4_half_moneyLineHome,
            q4_half_total=q4_half_total,
            q4_juice_over=q4_juice_over,
            q4_juice_under=q4_juice_under,
            q4_half_tt_away=q4_half_tt_away,
            q4_half_juice_over_away=q4_half_juice_over_away,
            q4_half_juice_under_away=q4_half_juice_under_away,
            q4_half_tt_home=q4_half_tt_home,
            q4_half_juice_over_home=q4_half_juice_over_home,
            q4_half_juice_under_home=q4_half_juice_under_home,
            q4_half_final_score_away=q4_half_final_score_away,
            q4_half_final_score_home=q4_half_final_score_home
        )

        db.session.add(ncaa_football)
        db.session.commit()
        return jsonify({"msg": "Game created successfully"}), 200

@app.route('/stats_ncaa_football_team', methods=['POST'])
def createstats_ncaa_football_team():
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)
    TP = request.json.get("TP", None)
    ttpg = request.json.get("ttpg", None)
    t_td = request.json.get("t_td", None)
    t_1_down = request.json.get("t_1_down", None)
    Russ_1_d = request.json.get("Russ_1_d", None)
    pass_1_d = request.json.get("pass_1_d", None)
    down_1_penal = request.json.get("down_1_penal", None)
    down_3_eff = request.json.get("down_3_eff", None)
    down_3_AVG = request.json.get("down_3_AVG", None)
    down_4_eff = request.json.get("down_4_eff", None)
    down_4_AVG = request.json.get("down_4_AVG", None)
    comp_att = request.json.get("comp_att", None)
    net_pass_y = request.json.get("net_pass_y", None)
    y_p_pas_attps = request.json.get("y_p_pas_attps", None)
    net_pass_y_pg = request.json.get("net_pass_y_pg", None)
    pass_td = request.json.get("pass_td", None)
    interceptions = request.json.get("interceptions", None)
    sacks_y_lost = request.json.get("sacks_y_lost", None)
    russ_attps = request.json.get("russ_attps", None)
    russ_y = request.json.get("russ_y", None)
    y_p_russ_attp = request.json.get("y_p_russ_attp", None)
    russ_y_pg = request.json.get("russ_y_pg", None)
    russ_td = request.json.get("russ_td", None)
    total_of_plays = request.json.get("total_of_plays", None)
    total_y = request.json.get("total_y", None)
    y_pg = request.json.get("y_pg", None)
    kickoffs_t = request.json.get("kickoffs_t", None)
    AVG_kickoff_return_y = request.json.get("AVG_kickoff_return_y", None)
    punt_t = request.json.get("punt_t", None)
    AVG_punt_ruturn_y = request.json.get("AVG_punt_ruturn_y", None)
    int_t = request.json.get("int_t", None)
    AVG_intercept_y = request.json.get("AVG_intercept_y", None)
    net_AVG_punt_y = request.json.get("net_AVG_punt_y", None)
    punt_ty = request.json.get("punt_ty", None)
    fg_goog_attps = request.json.get("fg_goog_attps", None)
    touchback_percent = request.json.get("touchback_percent", None)
    penal_ty = request.json.get("penal_ty", None)
    penal_y_AVG_pg = request.json.get("penal_y_AVG_pg", None)
    possesion_time = request.json.get("possesion_time", None)
    fumbles_lost = request.json.get("fumbles_lost", None)
    turnover_ratio = request.json.get("turnover_ratio", None)

    # valida si estan vacios los ingresos
    # busca team en BBDD
    stats_ncaa_football_team = Stats_ncaa_football_team.query.filter_by(
        team=team, season=season, conference=conference, division=division).first()
    # the team was not found on the database
    if stats_ncaa_football_team:
        return jsonify({"msg": "stats_ncaa_football_team already exists", "team": stats_ncaa_football_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_ncaa_football_team = Stats_ncaa_football_team(
            season=season,
            team=team,
            conference=conference,
            division=division,
            TP=TP,
            ttpg=ttpg,
            t_td=t_td,
            t_1_down=t_1_down,
            Russ_1_d=Russ_1_d,
            pass_1_d=pass_1_d,
            down_1_penal=down_1_penal,
            down_3_eff=down_3_eff,
            down_3_AVG=down_3_AVG,
            down_4_eff=down_4_eff,
            down_4_AVG=down_4_AVG,
            comp_att=comp_att,
            net_pass_y=net_pass_y,
            y_p_pas_attps=y_p_pas_attps,
            net_pass_y_pg=net_pass_y_pg,
            pass_td=pass_td,
            interceptions=interceptions,
            sacks_y_lost=sacks_y_lost,
            russ_attps=russ_attps,
            russ_y=russ_y,
            y_p_russ_attp=y_p_russ_attp,
            russ_y_pg=russ_y_pg,
            russ_td=russ_td,
            total_of_plays=total_of_plays,
            total_y=total_y,
            y_pg=y_pg,
            kickoffs_t=kickoffs_t,
            AVG_kickoff_return_y=AVG_kickoff_return_y,
            punt_t=punt_t,
            AVG_punt_ruturn_y=AVG_punt_ruturn_y,
            int_t=int_t,
            AVG_intercept_y=AVG_intercept_y,
            net_AVG_punt_y=net_AVG_punt_y,
            punt_ty=punt_ty,
            fg_goog_attps=fg_goog_attps,
            touchback_percent=touchback_percent,
            penal_ty=penal_ty,
            penal_y_AVG_pg=penal_y_AVG_pg,
            possesion_time=possesion_time,
            fumbles_lost=fumbles_lost,
            turnover_ratio=turnover_ratio
        )
        db.session.add(stats_ncaa_football_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_ncaa_football_team created successfully"}), 200

@app.route('/stats_defensive_player_ncca_football', methods=['POST'])
def createstats_defensive_player_ncca_football():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    tack_solo = request.json.get("tack_solo", None)
    tack_ast = request.json.get("tack_ast", None)
    tack_total = request.json.get("tack_total", None)
    sacks = request.json.get("sacks", None)
    sacks_yards = request.json.get("sacks_yards", None)
    tfl = request.json.get("tfl", None)
    pd = request.json.get("pd", None)
    Int = request.json.get("Int", None)
    yds = request.json.get("yds", None)
    ing = request.json.get("ing", None)
    td = request.json.get("td", None)
    ff = request.json.get("ff", None)
    fr = request.json.get("fr", None)
    ftd = request.json.get("ftd", None)
    kb = request.json.get("kb", None)

    # busca team en BBDD
    stats_defensive_player_ncca_football = Stats_defensive_player_ncca_football.query.filter_by(name=name, height=height, birth=birth, season=season).first()
    # the team was not found on the database
    if stats_defensive_player_ncca_football:
        return jsonify({"msg": "stats_defensive_player_ncca_football already exists", "name": stats_defensive_player_ncca_football.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_defensive_player_ncca_football = Stats_defensive_player_ncca_football(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            tack_solo=tack_solo,
            tack_ast=tack_ast,
            tack_total=tack_total,
            sacks=sacks,
            sacks_yards=sacks_yards,
            tfl=tfl,
            pd=pd,
            Int=Int,
            yds=yds,
            ing=ing,
            td=td,
            ff=ff,
            fr=fr,
            ftd=ftd,
            kb=kb
        )
        db.session.add(stats_defensive_player_ncca_football)
        db.session.commit()
        return jsonify({"msg": "Game stats_defensive_player_ncca_football created successfully"}), 200

@app.route('/stats_offensive_player_ncaa_football', methods=['POST'])
def createstats_offensive_player_ncaa_football():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    Cmp = request.json.get("Cmp", None)
    pass_att = request.json.get("pass_att", None)
    cmp_AVG = request.json.get("cmp_AVG", None)
    yards = request.json.get("yards", None)
    yards_AVG = request.json.get("yards_AVG", None)
    yards_pg = request.json.get("yards_pg", None)
    pass_td = request.json.get("pass_td", None)
    Int = request.json.get("Int", None)
    asck = request.json.get("asck", None)
    syl = request.json.get("syl", None)
    rtg = request.json.get("rtg", None)
    russ_att = request.json.get("russ_att", None)
    russ_yards = request.json.get("russ_yards", None)
    yards_p_russ = request.json.get("yards_p_russ", None)
    big = request.json.get("big", None)
    rush_tt = request.json.get("rush_tt", None)
    rush_yard_pg = request.json.get("rush_yard_pg", None)
    fum = request.json.get("fum", None)
    lst = request.json.get("lst", None)
    long_pass = request.json.get("long_pass", None)
    fd = request.json.get("fd", None)
    rec = request.json.get("rec", None)
    r_tgts = request.json.get("r_tgts", None)
    r_yards = request.json.get("r_yards", None)
    yards_p_r = request.json.get("yards_p_r", None)
    r_td = request.json.get("r_td", None)
    lr = request.json.get("lr", None)
    r_big = request.json.get("r_big", None)
    r_ypg = request.json.get("r_ypg", None)
    r_fl = request.json.get("r_fl", None)
    r_yac = request.json.get("r_yac", None)
    r_fd = request.json.get("r_fd", None)
    pts = request.json.get("pts", None)

    # valida si estan vacios los ingresos

    # busca team en BBDD
    stats_offensive_player_ncaa_football = Stats_offensive_player_ncaa_football.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_offensive_player_ncaa_football:
        return jsonify({"msg": "stats_offensive_player_ncaa_football already exists", "name": stats_offensive_player_ncaa_football.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_offensive_player_ncaa_football = Stats_offensive_player_ncaa_football(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            Cmp=Cmp,
            pass_att=pass_att,
            cmp_AVG=cmp_AVG,
            yards=yards,
            yards_AVG=yards_AVG,
            yards_pg=yards_pg,
            pass_td=pass_td,
            Int=Int,
            asck=asck,
            syl=syl,
            rtg=rtg,
            russ_att=russ_att,
            russ_yards=russ_yards,
            yards_p_russ=yards_p_russ,
            big=big,
            rush_tt=rush_tt,
            rush_yard_pg=rush_yard_pg,
            fum=fum,
            lst=lst,
            long_pass=long_pass,
            fd=fd,
            rec=rec,
            r_tgts=r_tgts,
            r_yards=r_yards,
            yards_p_r=yards_p_r,
            r_td=r_td,
            lr=lr,
            r_big=r_big,
            r_ypg=r_ypg,
            r_fl=r_fl,
            r_yac=r_yac,
            r_fd=r_fd,
            pts=pts
        )
        db.session.add(stats_offensive_player_ncaa_football)
        db.session.commit()
        return jsonify({"msg": "Game stats_offensive_player_ncaa_football created successfully"}), 200

@app.route('/stats_returning_player_ncaa_football', methods=['POST'])
def createstats_returning_player_ncaa_football():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    kick_returns = request.json.get("kick_returns", None)
    kick_returns_yards = request.json.get("kick_returns_yards", None)
    yards_p_k_p = request.json.get("yards_p_k_p", None)
    l_k_r = request.json.get("l_k_r", None)
    k_r_td = request.json.get("k_r_td", None)
    punt_r = request.json.get("punt_r", None)
    punt_r_y = request.json.get("punt_r_y", None)
    y_ppr = request.json.get("y_ppr", None)
    lpr = request.json.get("lpr", None)
    pr_td = request.json.get("pr_td", None)
    punt_r_fair_carches = request.json.get("punt_r_fair_carches", None)

    # busca team en BBDD
    stats_returning_player_ncaa_football = Stats_returning_player_ncaa_football.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_returning_player_ncaa_football:
        return jsonify({"msg": "stats_returning_player_ncaa_football already exists", "name": stats_returning_player_ncaa_football.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_returning_player_ncaa_football = Stats_returning_player_ncaa_football(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            kick_returns=kick_returns,
            kick_returns_yards=kick_returns_yards,
            yards_p_k_p=yards_p_k_p,
            l_k_r=l_k_r,
            k_r_td=k_r_td,
            punt_r=punt_r,
            punt_r_y=punt_r_y,
            y_ppr=y_ppr,
            lpr=lpr,
            pr_td=pr_td,
            punt_r_fair_carches=punt_r_fair_carches,
        )
        db.session.add(stats_returning_player_ncaa_football)
        db.session.commit()
        return jsonify({"msg": "Game stats_returning_player_ncaa_football created successfully"}), 200

@app.route('/stats_kiking_player_ncaa_football', methods=['POST'])
def createstats_kiking_player_ncaa_football():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    fgm = request.json.get("fgm", None)
    fga = request.json.get("fga", None)
    fg_AVG = request.json.get("fg_AVG", None)
    lng = request.json.get("lng", None)
    yars_f_goals_1_19 = request.json.get("yars_f_goals_1_19", None)
    yars_f_goals_20_29 = request.json.get("yars_f_goals_20_29", None)
    yars_f_goals_30_49 = request.json.get("yars_f_goals_30_49", None)
    yars_f_goals_40_49 = request.json.get("yars_f_goals_40_49", None)
    more_50 = request.json.get("more_50", None)
    xpm = request.json.get("xpm", None)
    xpa = request.json.get("xpa", None)
    xp_AVG = request.json.get("xp_AVG", None)

    # busca team en BBDD
    stats_kiking_player_ncaa_football = Stats_kiking_player_ncaa_football.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_kiking_player_ncaa_football:
        return jsonify({"msg": "stats_kiking_player_ncaa_football already exists", "name": stats_kiking_player_ncaa_football.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_kiking_player_ncaa_football = Stats_kiking_player_ncaa_football(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            fgm=fgm,
            fga=fga,
            fg_AVG=fg_AVG,
            lng=lng,
            yars_f_goals_1_19=yars_f_goals_1_19,
            yars_f_goals_20_29=yars_f_goals_20_29,
            yars_f_goals_30_49=yars_f_goals_30_49,
            yars_f_goals_40_49=yars_f_goals_40_49,
            more_50=more_50,
            xpm=xpm,
            xpa=xpa,
            xp_AVG=xp_AVG
        )
        db.session.add(stats_kiking_player_ncaa_football)
        db.session.commit()
        return jsonify({"msg": "Game stats_kiking_player_ncaa_football created successfully"}), 200

@app.route('/stats_punting_player_ncaa_football', methods=['POST'])
def createstats_punting_player_ncaa_football():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)

    punts = request.json.get("punts", None)
    yards = request.json.get("yards", None)
    lng = request.json.get("lng", None)
    AVG = request.json.get("AVG", None)
    net = request.json.get("net", None)
    p_blk = request.json.get("p_blk", None)
    IN_20 = request.json.get("IN_20", None)
    tb = request.json.get("tb", None)
    fc = request.json.get("fc", None)
    att = request.json.get("att", None)
    punt_return_yds = request.json.get("punt_return_yds", None)
    AVG_punt_retun_yards = request.json.get("AVG_punt_retun_yards", None)

    # busca team en BBDD
    stats_punting_player_ncaa_football = Stats_punting_player_ncaa_football.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_punting_player_ncaa_football:
        return jsonify({"msg": "stats_punting_player_ncaa_football already exists", "name": stats_punting_player_ncaa_football.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_punting_player_ncaa_football = Stats_punting_player_ncaa_football(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            punts=punts,
            yards=yards,
            lng=lng,
            AVG=AVG,
            net=net,
            p_blk=p_blk,
            IN_20=IN_20,
            tb=tb,
            fc=fc,
            att=att,
            punt_return_yds=punt_return_yds,
            AVG_punt_retun_yards=AVG_punt_retun_yards
        )
        db.session.add(stats_punting_player_ncaa_football)
        db.session.commit()
        return jsonify({"msg": "Game stats_punting_player_ncaa_football created successfully"}), 200



@app.route('/soccer', methods=['POST'])
def createSoccer():
    date = request.json.get("date", None)
    hour = request.json.get("hour", None)
    status = request.json.get("status", None)
    casino = request.json.get("casino", None)
    country = request.json.get("country", None)
    tournament = request.json.get("tournament", None)
    away = request.json.get("away", None)
    home = request.json.get("home", None)
    rotation_away = request.json.get("rotation_away", None)
    rotation_home = request.json.get("rotation_home", None)
    goal_line_away = request.json.get("goal_line_away", None)
    goal_line_home = request.json.get("goal_line_home", None)
    juice_goal_away = request.json.get("juice_goal_away", None)
    juice_goal_home = request.json.get("juice_goal_home", None)
    moneyLineAway = request.json.get("moneyLineAway", None)
    moneyLineHome = request.json.get("moneyLineHome", None)
    total = request.json.get("total", None)
    juice_total_over = request.json.get("juice_total_over", None)
    juice_total_under = request.json.get("juice_total_under", None)
    tt_away = request.json.get("tt_away", None)
    juice_over_away = request.json.get("juice_over_away", None)
    juice_under_away = request.json.get("juice_under_away", None)
    tt_home = request.json.get("tt_home", None)
    juice_over_home = request.json.get("juice_over_home", None)
    juice_under_home = request.json.get("juice_under_home", None)
    final_score_away = request.json.get("final_score_away", None)
    final_score_home = request.json.get("final_score_home", None)

    # --------------------------------------------------------------
    goal_away_1H = request.json.get("goal_away_1H", None)
    goal_home_1H = request.json.get("goal_home_1H", None)
    juice_goal_away_1H = request.json.get("juice_goal_away_1H", None)
    juice_goal_home_1H = request.json.get("juice_goal_home_1H", None)
    moneyLineAway_1H = request.json.get("moneyLineAway_1H", None)
    moneyLineHome_1H = request.json.get("moneyLineHome_1H", None)
    total_1H = request.json.get("total_1H", None)
    H1_juice_over = request.json.get("H1_juice_over", None)
    H1_juice_under = request.json.get("H1_juice_under", None)
    tt_away_1H = request.json.get("tt_away_1H", None)
    juice_over_away_1H = request.json.get("juice_over_away_1H", None)
    juice_under_away_1H = request.json.get("juice_under_away_1H", None)
    tt_home_1H = request.json.get("tt_home_1H", None)
    juice_over_home_1H = request.json.get("juice_over_home_1H", None)
    juice_under_home_1H = request.json.get("juice_under_home_1H", None)

    # busca mlb en BBDD
    soccer = Soccer.query.filter_by(
        home=home, away=away, date=date,tournament=tournament).first()
    # the mlb was not found on the database
    if soccer:
        return jsonify({"msg": "soccer match already exists", "team away": soccer.away, "team home": soccer.home}), 401
    else:
        # crea mlb nuevo
        # crea registro nuevo en BBDD de
        soccer = Soccer(
            date=date,
            hour=hour,
            status=status,
            casino=casino,
            country=country,
            tournament=tournament,
            away=away,
            home=home,
            rotation_away=rotation_away,
            rotation_home=rotation_home,
            goal_line_away=goal_line_away,
            goal_line_home=goal_line_home,
            juice_goal_away=juice_goal_away,
            juice_goal_home=juice_goal_home,
            moneyLineAway=moneyLineAway,
            moneyLineHome=moneyLineHome,
            total=total,
            juice_total_over=juice_total_over,
            juice_total_under=juice_total_under,
            tt_away=tt_away,
            juice_over_away=juice_over_away,
            juice_under_away=juice_under_away,
            tt_home=tt_home,
            juice_over_home=juice_over_home,
            juice_under_home=juice_under_home,
            final_score_away=final_score_away,
            final_score_home=final_score_home,

            goal_away_1H=goal_away_1H,
            goal_home_1H=goal_home_1H,
            juice_goal_away_1H=juice_goal_away_1H,
            juice_goal_home_1H=juice_goal_home_1H,
            moneyLineAway_1H=moneyLineAway_1H,
            moneyLineHome_1H=moneyLineHome_1H,
            total_1H=total_1H,
            H1_juice_over=H1_juice_over,
            H1_juice_under=H1_juice_under,
            tt_away_1H=tt_away_1H,
            juice_over_away_1H=juice_over_away_1H,
            juice_under_away_1H=juice_under_away_1H,
            tt_home_1H=tt_home_1H,
            juice_over_home_1H=juice_over_home_1H,
            juice_under_home_1H=juice_under_home_1H
        )
        db.session.add(soccer)
        db.session.commit()
        return jsonify({"msg": "Game soccer created successfully"}), 200

@app.route('/stats_soccer_team', methods=['POST'])
def createStats_soccer_team():
    season = request.json.get("season", None)
    name = request.json.get("name", None)
    league = request.json.get("league", None)
    position = request.json.get("position", None)
    matches = request.json.get("matches", None)
    win = request.json.get("win", None)
    loss = request.json.get("loss", None)
    pts = request.json.get("pts", None)
    goals_for = request.json.get("goals_for", None)
    goals_against = request.json.get("goals_against", None)
    more_2_5_goals = request.json.get("more_2_5_goals", None)
    less_2_5_goals = request.json.get("less_2_5_goals", None)
    zero_goal_against = request.json.get("zero_goal_against", None)
    zero_goals_for = request.json.get("zero_goals_for", None)
    ties = request.json.get("ties", None)
    # busca team en BBDD
    stats_soccer_team = Stats_Soccer_Team.query.filter_by(name=name,season=season).first()
    # the team was not found on the database
    if stats_soccer_team:
        return jsonify({"msg": "stats_soccer_team already exists", "team": stats_soccer_team.name,"team": stats_soccer_team.season}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_soccer_team = Stats_Soccer_Team(
            season=season,
            name=name,
            league=league,
            position=position,
            matches=matches,
            win=win,
            loss=loss,
            pts=pts,
            goals_for=goals_for,
            goals_against=goals_against,
            more_2_5_goals=more_2_5_goals,
            less_2_5_goals=less_2_5_goals,
            zero_goal_against=zero_goal_against,
            zero_goals_for=zero_goals_for,
            ties=ties
        )
        db.session.add(stats_soccer_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_soccer_team created successfully"}), 200

@app.route('/stats_soccer_player', methods=['POST'])
def createStats_Soccer_Player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)

    strt = request.json.get("strt", None)
    fc = request.json.get("fc", None)
    fa = request.json.get("fa", None)
    yc = request.json.get("yc", None)
    rc = request.json.get("rc", None)
    goals = request.json.get("goals", None)
    ast = request.json.get("ast", None)
    sh = request.json.get("sh", None)
    st = request.json.get("st", None)
    off = request.json.get("off", None)

    # busca team en BBDD
    stats_soccer_player = Stats_Soccer_Player.query.filter_by(
        name=name, dorsal=dorsal, birth=birth, season=season).first()
    # the team was not found on the database
    if stats_soccer_player:
        return jsonify({"msg": "stats_soccer_player already exists", "name": stats_soccer_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_soccer_player = Stats_Soccer_Player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,

            strt=strt,
            fc=fc,
            fa=fa,
            yc=yc,
            rc=rc,
            goals=goals,
            ast=ast,
            sh=sh,
            st=st,
            off=off,
        )
        db.session.add(stats_soccer_player)
        db.session.commit()
        return jsonify({"msg": "Stats_soccer_player created successfully"}), 200

@app.route('/stats_nba_team', methods=['POST'])
def createStats_nba_team():
    season = request.json.get("season", None)
    season_type = request.json.get("season_type", None)
    group_type_comparation = request.json.get("group_type_comparation", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)

    w = request.json.get("w", None)
    L = request.json.get("L", None)
    ptc = request.json.get("ptc", None)
    gb = request.json.get("gb", None)
    home = request.json.get("home", None)
    away = request.json.get("away", None)
    div = request.json.get("div", None)
    conf = request.json.get("conf", None)
    ppg = request.json.get("ppg", None)
    opp_ppg = request.json.get("opp_ppg", None)
    diff = request.json.get("diff", None)
    strk = request.json.get("strk", None)
    l10 = request.json.get("l10", None)

    # busca team en BBDD
    stats_nba_team = Stats_nba_team.query.filter_by(team=team).first()
    # the team was not found on the database
    if stats_nba_team:
        return jsonify({"msg": "stats_nba_team already exists", "team": stats_nba_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nba_team = Stats_nba_team(
            season=season,
            season_type=season_type,
            group_type_comparation=group_type_comparation,
            team=team,
            conference=conference,
            division=division,
            w=w,
            L=L,
            ptc=ptc,
            gb=gb,
            home=home,
            away=away,
            div=div,
            conf=conf,
            ppg=ppg,
            opp_ppg=opp_ppg,
            diff=diff,
            strk=strk,
            l10=l10
        )
        db.session.add(stats_nba_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_nba_team created successfully"}), 200


@app.route('/stats_nba_player', methods=['POST'])
def createStats_nba_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    college = request.json.get("college", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)

    dorsal = request.json.get("dorsal", None)
    minutes = request.json.get("minutes", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    gp = request.json.get("gp", None)
    gs = request.json.get("gs", None)
    fg = request.json.get("fg", None)
    fg_AVG = request.json.get("fg_AVG", None)
    three_pt = request.json.get("three_pt", None)
    three_pt_AVG = request.json.get("three_pt_AVG", None)
    ft = request.json.get("ft", None)
    ft_AVG = request.json.get("ft_AVG", None)
    Or = request.json.get("Or", None)
    dr = request.json.get("dr", None)
    reb = request.json.get("reb", None)
    ast = request.json.get("ast", None)
    stl = request.json.get("stl", None)
    blk = request.json.get("blk", None)
    to = request.json.get("to", None)
    pf = request.json.get("pf", None)
    pts = request.json.get("pts", None)
    # busca team en BBDD
    stats_nba_player = Stats_nba_player.query.filter_by(
        name=name, dorsal=dorsal, team=team).first()
    # the team was not found on the database
    if stats_nba_player:
        return jsonify({"msg": "stats_nba_player already exists", "name": stats_nba_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nba_player = Stats_nba_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            college=college,
            season=season,
            team=team,

            dorsal=dorsal,
            minutes=minutes,
            position=position,
            headshot=headshot,
            gp=gp,
            gs=gs,
            fg=fg,
            fg_AVG=fg_AVG,
            three_pt=three_pt,
            three_pt_AVG=three_pt_AVG,
            ft=ft,
            ft_AVG=ft_AVG,
            Or=Or,
            dr=dr,
            reb=reb,
            ast=ast,
            stl=stl,
            blk=blk,
            to=to,
            pf=pf,
            pts=pts
        )
        db.session.add(stats_nba_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_nba_player created successfully"}), 200


@app.route('/stats_nhl_team', methods=['POST'])
def createStats_nhl_team():
    season = request.json.get("season", None)
    season_type = request.json.get("season_type", None)
    group_type_comparation = request.json.get("group_type_comparation", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)
    gp = request.json.get("gp", None)
    w = request.json.get("w", None)
    L = request.json.get("L", None)

    otl = request.json.get("otl", None)
    pts = request.json.get("pts", None)
    rw = request.json.get("rw", None)
    row = request.json.get("row", None)
    sow = request.json.get("sow", None)
    sol = request.json.get("sol", None)
    home = request.json.get("home", None)
    away = request.json.get("away", None)
    gf = request.json.get("gf", None)
    ga = request.json.get("ga", None)
    diff = request.json.get("diff", None)
    l10 = request.json.get("l10", None)
    strk = request.json.get("strk", None)

    # busca team en BBDD
    stats_nhl_team = Stats_nhl_team.query.filter_by(
        team=team, conference=conference, division=division).first()
    # the team was not found on the database
    if stats_nhl_team:
        return jsonify({"msg": "stats_nhl_team already exists", "team": stats_nhl_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nhl_team = Stats_nhl_team(
            season=season,
            season_type=season_type,
            group_type_comparation=group_type_comparation,
            team=team,
            conference=conference,
            division=division,
            gp=gp,
            w=w,
            L=L,
            otl=otl,
            pts=pts,
            rw=rw,
            row=row,
            sow=sow,
            sol=sol,
            home=home,
            away=away,
            gf=gf,
            ga=ga,
            diff=diff,
            l10=l10,
            strk=strk,
        )
        db.session.add(stats_nhl_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_nhl_team created successfully"}), 200


@app.route('/stats_nhl_player', methods=['POST'])
def createStats_nhl_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    dorsal = request.json.get("dorsal", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    gp = request.json.get("gp", None)
    g = request.json.get("g", None)
    a = request.json.get("a", None)
    pts = request.json.get("pts", None)
    p_m_rating = request.json.get("p_m_rating", None)
    pim = request.json.get("pim", None)
    sog = request.json.get("sog", None)
    spct = request.json.get("spct", None)
    ppg = request.json.get("ppg", None)
    ppa = request.json.get("ppa", None)
    shg = request.json.get("shg", None)
    sha = request.json.get("sha", None)
    gwg = request.json.get("gwg", None)
    gtg = request.json.get("gtg", None)
    toi_g = request.json.get("toi_g", None)
    prod = request.json.get("prod", None)
    # busca team en BBDD
    stats_nhl_player = Stats_nhl_player.query.filter_by(
        name=name, dorsal=dorsal, team=team).first()
    # the team was not found on the database
    if stats_nhl_player:
        return jsonify({"msg": "stats_nhl_player already exists", "name": stats_nhl_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nhl_player = Stats_nhl_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            season=season,
            team=team,
            dorsal=dorsal,
            position=position,
            headshot=headshot,
            gp=gp,
            g=g,
            a=a,
            pts=pts,
            p_m_rating=p_m_rating,
            pim=pim,
            sog=sog,
            spct=spct,
            ppg=ppg,
            ppa=ppa,
            shg=shg,
            sha=sha,
            gwg=gwg,
            gtg=gtg,
            toi_g=toi_g,
            prod=prod
        )
        db.session.add(stats_nhl_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_nhl_player created successfully"}), 200


@app.route('/stats_mlb_team', methods=['POST'])
def createStats_mlb_team():
    season = request.json.get("season", None)
    season_type = request.json.get("season_type", None)
    group_type_comparation = request.json.get("group_type_comparation", None)
    team = request.json.get("team", None)
    league = request.json.get("league", None)
    division = request.json.get("division", None)
    w = request.json.get("w", None)
    L = request.json.get("L", None)
    pct = request.json.get("pct", None)
    gb = request.json.get("gb", None)
    home = request.json.get("home", None)
    away = request.json.get("away", None)
    rs = request.json.get("rs", None)
    ra = request.json.get("ra", None)
    diff = request.json.get("diff", None)
    strk = request.json.get("strk", None)
    L10 = request.json.get("L10", None)

    # busca team en BBDD
    stats_mlb_team = Stats_mlb_team.query.filter_by(
        team=team, league=league, division=division).first()
    # the team was not found on the database
    if stats_mlb_team:
        return jsonify({"msg": "stats_mlb_team already exists", "team": stats_mlb_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_mlb_team = Stats_mlb_team(
            season=season,
            season_type=season_type,
            group_type_comparation=group_type_comparation,
            team=team,
            league=league,
            division=division,
            w=w,
            L=L,
            pct=pct,
            gb=gb,
            home=home,
            away=away,
            rs=rs,
            ra=ra,
            diff=diff,
            strk=strk,
            L10=L10
        )
        db.session.add(stats_mlb_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_mlb_team created successfully"}), 200


@app.route('/stats_mlb_player', methods=['POST'])
def createStats_mlb_player():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    dorsal = request.json.get("dorsal", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)

    gp = request.json.get("gp", None)
    ab = request.json.get("ab", None)
    r = request.json.get("r", None)
    h = request.json.get("h", None)
    two_b = request.json.get("two_b", None)
    three_b = request.json.get("three_b", None)
    hb = request.json.get("hb", None)
    rbi = request.json.get("rbi", None)
    tb = request.json.get("tb", None)
    bb = request.json.get("bb", None)
    so = request.json.get("so", None)
    sb = request.json.get("sb", None)
    avg = request.json.get("avg", None)
    obp = request.json.get("obp", None)
    slg = request.json.get("slg", None)
    ops = request.json.get("ops", None)
    war = request.json.get("war", None)

    # busca team en BBDD
    stats_mlb_player = Stats_mlb_player.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_mlb_player:
        return jsonify({"msg": "stats_mlb_player already exists", "name": stats_mlb_player.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_mlb_player = Stats_mlb_player(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            season=season,
            team=team,
            dorsal=dorsal,
            position=position,
            headshot=headshot,
            gp=gp,
            ab=ab,
            r=r,
            h=h,
            two_b=two_b,
            three_b=three_b,
            hb=hb,
            rbi=rbi,
            tb=tb,
            bb=bb,
            so=so,
            sb=sb,
            avg=avg,
            obp=obp,
            slg=slg,
            ops=ops,
            war=war
        )
        db.session.add(stats_mlb_player)
        db.session.commit()
        return jsonify({"msg": "Game stats_mlb_player created successfully"}), 200


@app.route('/stats_box_fighter', methods=['POST'])
def createStats_box_fighter():
    name = request.json.get("name", None)
    nickname = request.json.get("nickname", None)
    headshot = request.json.get("headshot", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    country = request.json.get("country", None)
    season = request.json.get("season", None)
    association = request.json.get("association", None)
    category = request.json.get("category", None)
    w = request.json.get("w", None)
    w_by = request.json.get("w_by", None)
    L = request.json.get("L", None)
    L_by = request.json.get("L_by", None)

    # busca team en BBDD
    stats_box_fighter = Stats_box_fighter.query.filter_by(
        name=name, nickname=nickname, birth=birth).first()
    # the team was not found on the database
    if stats_box_fighter:
        return jsonify({"msg": "stats box fighter already exists", "name": stats_box_fighter.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_box_fighter = Stats_box_fighter(
            name=name,
            nickname=nickname,
            headshot=headshot,
            height=height,
            weight=weight,
            birth=birth,
            country=country,
            season=season,
            association=association,
            category=category,
            w=w,
            w_by=w_by,
            L=L,
            L_by=L_by
        )
        db.session.add(stats_box_fighter)
        db.session.commit()
        return jsonify({"msg": "Game stats box fighter created successfully"}), 200


@app.route('/stats_mma_fighter', methods=['POST'])
def createStats_mma_fighter():
    name = request.json.get("name", None)
    nickname = request.json.get("nickname", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    headshot = request.json.get("headshot", None)
    country = request.json.get("country", None)
    season = request.json.get("season", None)
    association = request.json.get("association", None)
    category = request.json.get("category", None)
    w = request.json.get("w", None)
    w_by = request.json.get("w_by", None)
    L = request.json.get("L", None)
    L_by = request.json.get("L_by", None)

    # busca team en BBDD
    stats_mma_fighter = Stats_mma_fighter.query.filter_by(
        name=name, nickname=nickname, birth=birth).first()
    # the team was not found on the database
    if stats_mma_fighter:
        return jsonify({"msg": "stats_mma_fighter already exists", "team": stats_mma_fighter.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_mma_fighter = Stats_mma_fighter(
            name=name,
            nickname=nickname,
            height=height,
            weight=weight,
            headshot=headshot,
            birth=birth,
            country=country,
            season=season,
            association=association,
            category=category,
            w=w,
            w_by=w_by,
            L=L,
            L_by=L_by
        )
        db.session.add(stats_mma_fighter)
        db.session.commit()
        return jsonify({"msg": "Game stats_mma_fighter created successfully"}), 200


@app.route('/stats_nfl_team', methods=['POST'])
def createStats_nfl_team():
    season = request.json.get("season", None)
    season_type = request.json.get("season_type", None)
    team = request.json.get("team", None)
    conference = request.json.get("conference", None)
    division = request.json.get("division", None)
    TP = request.json.get("TP", None)
    ttpg = request.json.get("ttpg", None)
    t_td = request.json.get("t_td", None)
    t_1_down = request.json.get("t_1_down", None)
    Russ_1_d = request.json.get("Russ_1_d", None)
    pass_1_d = request.json.get("pass_1_d", None)
    down_1_penal = request.json.get("down_1_penal", None)
    down_3_eff = request.json.get("down_3_eff", None)
    down_3_AVG = request.json.get("down_3_AVG", None)
    down_4_eff = request.json.get("down_4_eff", None)
    down_4_AVG = request.json.get("down_4_AVG", None)
    comp_att = request.json.get("comp_att", None)
    net_pass_y = request.json.get("net_pass_y", None)
    y_p_pas_attps = request.json.get("y_p_pas_attps", None)
    net_pass_y_pg = request.json.get("net_pass_y_pg", None)
    pass_td = request.json.get("pass_td", None)
    interceptions = request.json.get("interceptions", None)
    sacks_y_lost = request.json.get("sacks_y_lost", None)
    russ_attps = request.json.get("russ_attps", None)
    russ_y = request.json.get("russ_y", None)
    y_p_russ_attp = request.json.get("y_p_russ_attp", None)
    russ_y_pg = request.json.get("russ_y_pg", None)
    russ_td = request.json.get("russ_td", None)
    total_of_plays = request.json.get("total_of_plays", None)
    total_y = request.json.get("total_y", None)
    y_pg = request.json.get("y_pg", None)
    kickoffs_t = request.json.get("kickoffs_t", None)
    AVG_kickoff_return_y = request.json.get("AVG_kickoff_return_y", None)
    punt_t = request.json.get("punt_t", None)
    AVG_punt_ruturn_y = request.json.get("AVG_punt_ruturn_y", None)
    int_t = request.json.get("int_t", None)
    AVG_intercept_y = request.json.get("AVG_intercept_y", None)
    net_AVG_punt_y = request.json.get("net_AVG_punt_y", None)
    punt_ty = request.json.get("punt_ty", None)
    fg_goog_attps = request.json.get("fg_goog_attps", None)
    touchback_percent = request.json.get("touchback_percent", None)
    penal_ty = request.json.get("penal_ty", None)
    penal_y_AVG_pg = request.json.get("penal_y_AVG_pg", None)
    possesion_time = request.json.get("possesion_time", None)
    fumbles_lost = request.json.get("fumbles_lost", None)
    turnover_ratio = request.json.get("turnover_ratio", None)

    # valida si estan vacios los ingresos
    # busca team en BBDD
    stats_nfl_team = Stats_nfl_team.query.filter_by(
        team=team, season=season, conference=conference, division=division).first()
    # the team was not found on the database
    if stats_nfl_team:
        return jsonify({"msg": "stats_nfl_team already exists", "team": stats_nfl_team.team}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_nfl_team = Stats_nfl_team(
            season=season,
            season_type=season_type,
            team=team,
            conference=conference,
            division=division,
            TP=TP,
            ttpg=ttpg,
            t_td=t_td,
            t_1_down=t_1_down,
            Russ_1_d=Russ_1_d,
            pass_1_d=pass_1_d,
            down_1_penal=down_1_penal,
            down_3_eff=down_3_eff,
            down_3_AVG=down_3_AVG,
            down_4_eff=down_4_eff,
            down_4_AVG=down_4_AVG,
            comp_att=comp_att,
            net_pass_y=net_pass_y,
            y_p_pas_attps=y_p_pas_attps,
            net_pass_y_pg=net_pass_y_pg,
            pass_td=pass_td,
            interceptions=interceptions,
            sacks_y_lost=sacks_y_lost,
            russ_attps=russ_attps,
            russ_y=russ_y,
            y_p_russ_attp=y_p_russ_attp,
            russ_y_pg=russ_y_pg,
            russ_td=russ_td,
            total_of_plays=total_of_plays,
            total_y=total_y,
            y_pg=y_pg,
            kickoffs_t=kickoffs_t,
            AVG_kickoff_return_y=AVG_kickoff_return_y,
            punt_t=punt_t,
            AVG_punt_ruturn_y=AVG_punt_ruturn_y,
            int_t=int_t,
            AVG_intercept_y=AVG_intercept_y,
            net_AVG_punt_y=net_AVG_punt_y,
            punt_ty=punt_ty,
            fg_goog_attps=fg_goog_attps,
            touchback_percent=touchback_percent,
            penal_ty=penal_ty,
            penal_y_AVG_pg=penal_y_AVG_pg,
            possesion_time=possesion_time,
            fumbles_lost=fumbles_lost,
            turnover_ratio=turnover_ratio
        )
        db.session.add(stats_nfl_team)
        db.session.commit()
        return jsonify({"msg": "Game stats_nfl_team created successfully"}), 200


@app.route('/stats_defensive_player_nfl', methods=['POST'])
def createStats_defensive_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    tack_solo = request.json.get("tack_solo", None)
    tack_ast = request.json.get("tack_ast", None)
    tack_total = request.json.get("tack_total", None)
    sacks = request.json.get("sacks", None)
    sacks_yards = request.json.get("sacks_yards", None)
    tfl = request.json.get("tfl", None)
    pd = request.json.get("pd", None)
    Int = request.json.get("Int", None)
    yds = request.json.get("yds", None)
    ing = request.json.get("ing", None)
    td = request.json.get("td", None)
    ff = request.json.get("ff", None)
    fr = request.json.get("fr", None)
    ftd = request.json.get("ftd", None)
    kb = request.json.get("kb", None)

    # busca team en BBDD
    stats_defensive_player_nfl = Stats_defensive_player_nfl.query.filter_by(name=name, height=height, birth=birth, season=season).first()
    # the team was not found on the database
    if stats_defensive_player_nfl:
        return jsonify({"msg": "stats_defensive_player_nfl already exists", "name": stats_defensive_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_defensive_player_nfl = Stats_defensive_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            tack_solo=tack_solo,
            tack_ast=tack_ast,
            tack_total=tack_total,
            sacks=sacks,
            sacks_yards=sacks_yards,
            tfl=tfl,
            pd=pd,
            Int=Int,
            yds=yds,
            ing=ing,
            td=td,
            ff=ff,
            fr=fr,
            ftd=ftd,
            kb=kb
        )
        db.session.add(stats_defensive_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_defensive_player_nfl created successfully"}), 200


@app.route('/stats_offensive_player_nfl', methods=['POST'])
def createStats_offensive_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    Cmp = request.json.get("Cmp", None)
    pass_att = request.json.get("pass_att", None)
    cmp_AVG = request.json.get("cmp_AVG", None)
    yards = request.json.get("yards", None)
    yards_AVG = request.json.get("yards_AVG", None)
    yards_pg = request.json.get("yards_pg", None)
    pass_td = request.json.get("pass_td", None)
    Int = request.json.get("Int", None)
    asck = request.json.get("asck", None)
    syl = request.json.get("syl", None)
    rtg = request.json.get("rtg", None)
    russ_att = request.json.get("russ_att", None)
    russ_yards = request.json.get("russ_yards", None)
    yards_p_russ = request.json.get("yards_p_russ", None)
    big = request.json.get("big", None)
    rush_tt = request.json.get("rush_tt", None)
    rush_yard_pg = request.json.get("rush_yard_pg", None)
    fum = request.json.get("fum", None)
    lst = request.json.get("lst", None)
    fd = request.json.get("fd", None)
    rec = request.json.get("rec", None)
    r_tgts = request.json.get("r_tgts", None)
    r_yards = request.json.get("r_yards", None)
    yards_p_r = request.json.get("yards_p_r", None)
    r_td = request.json.get("r_td", None)
    lr = request.json.get("lr", None)
    r_big = request.json.get("r_big", None)
    r_ypg = request.json.get("r_ypg", None)
    r_fl = request.json.get("r_fl", None)
    r_yac = request.json.get("r_yac", None)
    r_fd = request.json.get("r_fd", None)
    pts = request.json.get("pts", None)

    # valida si estan vacios los ingresos

    # busca team en BBDD
    stats_offensive_player_nfl = Stats_offensive_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_offensive_player_nfl:
        return jsonify({"msg": "stats_offensive_player_nfl already exists", "name": stats_offensive_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_offensive_player_nfl = Stats_offensive_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            Cmp=Cmp,
            pass_att=pass_att,
            cmp_AVG=cmp_AVG,
            yards=yards,
            yards_AVG=yards_AVG,
            yards_pg=yards_pg,
            pass_td=pass_td,
            Int=Int,
            asck=asck,
            syl=syl,
            rtg=rtg,
            russ_att=russ_att,
            russ_yards=russ_yards,
            yards_p_russ=yards_p_russ,
            big=big,
            rush_tt=rush_tt,
            rush_yard_pg=rush_yard_pg,
            fum=fum,
            lst=lst,
            fd=fd,
            rec=rec,
            r_tgts=r_tgts,
            r_yards=r_yards,
            yards_p_r=yards_p_r,
            r_td=r_td,
            lr=lr,
            r_big=r_big,
            r_ypg=r_ypg,
            r_fl=r_fl,
            r_yac=r_yac,
            r_fd=r_fd,
            pts=pts
        )
        db.session.add(stats_offensive_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_offensive_player_nfl created successfully"}), 200


@app.route('/stats_returning_player_nfl', methods=['POST'])
def createStats_returning_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    kick_returns = request.json.get("kick_returns", None)
    kick_returns_yards = request.json.get("kick_returns_yards", None)
    yards_p_k_p = request.json.get("yards_p_k_p", None)
    l_k_r = request.json.get("l_k_r", None)
    k_r_td = request.json.get("k_r_td", None)
    punt_r = request.json.get("punt_r", None)
    punt_r_y = request.json.get("punt_r_y", None)
    y_ppr = request.json.get("y_ppr", None)
    lpr = request.json.get("lpr", None)
    pr_td = request.json.get("pr_td", None)
    punt_r_fair_carches = request.json.get("punt_r_fair_carches", None)

    # busca team en BBDD
    stats_returning_player_nfl = Stats_returning_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_returning_player_nfl:
        return jsonify({"msg": "stats_returning_player_nfl already exists", "name": stats_returning_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_returning_player_nfl = Stats_returning_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            kick_returns=kick_returns,
            kick_returns_yards=kick_returns_yards,
            yards_p_k_p=yards_p_k_p,
            l_k_r=l_k_r,
            k_r_td=k_r_td,
            punt_r=punt_r,
            punt_r_y=punt_r_y,
            y_ppr=y_ppr,
            lpr=lpr,
            pr_td=pr_td,
            punt_r_fair_carches=punt_r_fair_carches,
        )
        db.session.add(stats_returning_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_returning_player_nfl created successfully"}), 200


@app.route('/stats_kiking_player_nfl', methods=['POST'])
def createStats_kiking_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)
    fgm = request.json.get("fgm", None)
    fga = request.json.get("fga", None)
    fg_AVG = request.json.get("fg_AVG", None)
    lng = request.json.get("lng", None)
    yars_f_goals_1_19 = request.json.get("yars_f_goals_1_19", None)
    yars_f_goals_20_29 = request.json.get("yars_f_goals_20_29", None)
    yars_f_goals_30_49 = request.json.get("yars_f_goals_30_49", None)
    yars_f_goals_40_49 = request.json.get("yars_f_goals_40_49", None)
    more_50 = request.json.get("more_50", None)
    xpm = request.json.get("xpm", None)
    xpa = request.json.get("xpa", None)
    xp_AVG = request.json.get("xp_AVG", None)

    # busca team en BBDD
    stats_kiking_player_nfl = Stats_kiking_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_kiking_player_nfl:
        return jsonify({"msg": "stats_kiking_player_nfl already exists", "name": stats_kiking_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_kiking_player_nfl = Stats_kiking_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            fgm=fgm,
            fga=fga,
            fg_AVG=fg_AVG,
            lng=lng,
            yars_f_goals_1_19=yars_f_goals_1_19,
            yars_f_goals_20_29=yars_f_goals_20_29,
            yars_f_goals_30_49=yars_f_goals_30_49,
            yars_f_goals_40_49=yars_f_goals_40_49,
            more_50=more_50,
            xpm=xpm,
            xpa=xpa,
            xp_AVG=xp_AVG
        )
        db.session.add(stats_kiking_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_kiking_player_nfl created successfully"}), 200


@app.route('/stats_punting_player_nfl', methods=['POST'])
def createStats_punting_player_nfl():
    name = request.json.get("name", None)
    height = request.json.get("height", None)
    weight = request.json.get("weight", None)
    birth = request.json.get("birth", None)
    position = request.json.get("position", None)
    headshot = request.json.get("headshot", None)
    dorsal = request.json.get("dorsal", None)
    season = request.json.get("season", None)
    team = request.json.get("team", None)
    games = request.json.get("games", None)

    punts = request.json.get("punts", None)
    yards = request.json.get("yards", None)
    lng = request.json.get("lng", None)
    AVG = request.json.get("AVG", None)
    net = request.json.get("net", None)
    p_blk = request.json.get("p_blk", None)
    IN_20 = request.json.get("IN_20", None)
    tb = request.json.get("tb", None)
    fc = request.json.get("fc", None)
    att = request.json.get("att", None)
    punt_return_yds = request.json.get("punt_return_yds", None)
    AVG_punt_retun_yards = request.json.get("AVG_punt_retun_yards", None)

    # busca team en BBDD
    stats_punting_player_nfl = Stats_punting_player_nfl.query.filter_by(
        name=name, dorsal=dorsal, birth=birth).first()
    # the team was not found on the database
    if stats_punting_player_nfl:
        return jsonify({"msg": "stats_punting_player_nfl already exists", "name": stats_punting_player_nfl.name}), 401
    else:
        # crea encuentro nuevo
        # crea registro nuevo en BBDD de
        stats_punting_player_nfl = Stats_punting_player_nfl(
            name=name,
            height=height,
            weight=weight,
            birth=birth,
            position=position,
            headshot=headshot,
            dorsal=dorsal,
            season=season,
            team=team,
            games=games,
            punts=punts,
            yards=yards,
            lng=lng,
            AVG=AVG,
            net=net,
            p_blk=p_blk,
            IN_20=IN_20,
            tb=tb,
            fc=fc,
            att=att,
            punt_return_yds=punt_return_yds,
            AVG_punt_retun_yards=AVG_punt_retun_yards
        )
        db.session.add(stats_punting_player_nfl)
        db.session.commit()
        return jsonify({"msg": "Game stats_punting_player_nfl created successfully"}), 200


# ------------put-------------------------------------------------------------------------------

@app.route('/props/<id>', methods=['PUT'])
def newsProps(id):
    props = Props.query.get(id)
    title = request.json['title']
    date = request.json['date']
    type_prop = request.json['type_prop']
    sport = request.json['sport']
    feature = request.json['feature']
    line = request.json['line']
    home = request.json['home']
    away = request.json['away']
    props.title = title
    props.date = date
    props.type_prop = type_prop
    props.sport = sport
    props.feature = feature
    props.line = line
    props.home = home
    props.away = away

    db.session.commit()
    return jsonify({"msg": "Props edith successfully"}), 200

@app.route('/odds_to_win/<id>', methods=['PUT'])
def newsodds_to_win(id):
    odds_to_win = Odds_to_win.query.get(id)
    title = request.json['title']
    sport = request.json['sport']
    type_odd = request.json['type_odd']
    line = request.json['line']
    team = request.json['team']
    date = request.json['date']
    odds_to_win.title = title
    odds_to_win.sport = sport
    odds_to_win.type_odd = type_odd
    odds_to_win.line = line
    odds_to_win.team = team
    odds_to_win.date = date

    db.session.commit()
    return jsonify({"msg": "odds_to_win edith successfully"}), 200

@app.route('/injuries/<id>', methods=['PUT'])
def newsinjuries(id):
    injuries = Injuries.query.get(id)
    sport = request.json['sport']
    name_player = request.json['name_player']
    team = request.json['team']
    injurie = request.json['injurie']
    time_injurie = request.json['time_injurie']
    date = request.json['date']
    injuries.sport = sport
    injuries.name_player = name_player
    injuries.team = team
    injuries.injurie = injurie
    injuries.time_injurie = time_injurie
    injuries.date = date

    db.session.commit()
    return jsonify({"msg": "injuries edith successfully"}), 200

@app.route('/casinos/<id>', methods=['PUT'])
def newsCasinos(id):
    casinos = Casinos.query.get(id)
    name = request.json['name']
    casinos.name = name

    db.session.commit()
    return jsonify({"msg": "casino edith successfully"}), 200

@app.route('/futures/<id>', methods=['PUT'])
def newsfutures(id):
    futures = Futures.query.get(id)
    sport = request.json['sport']
    future = request.json['future']
    line = request.json['line']
    date = request.json['date']
    futures.sport = sport
    futures.future = future
    futures.line = line
    futures.date = date

    db.session.commit()
    return jsonify({"msg": "futures edith successfully"}), 200

@app.route('/logos_nfl/<id>', methods=['PUT'])
def newslogos_nfl(id):
    logos_nfl = Logos_NFL.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_nfl.team = team
    logos_nfl.url = url

    db.session.commit()
    return jsonify({"msg": "logos_nfl edith successfully"}), 200

@app.route('/logos_nba/<id>', methods=['PUT'])
def newslogos_nba(id):
    logos_nba = Logos_NBA.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_nba.team = team
    logos_nba.url = url

    db.session.commit()
    return jsonify({"msg": "logos_nba edith successfully"}), 200

@app.route('/logos_mlb/<id>', methods=['PUT'])
def newslogos_mlb(id):
    logos_mlb = Logos_MLB.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_mlb.team = team
    logos_mlb.url = url

    db.session.commit()
    return jsonify({"msg": "logos_mlb edith successfully"}), 200

@app.route('/logos_nhl/<id>', methods=['PUT'])
def newslogos_nhl(id):
    logos_nhl = Logos_NHL.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_nhl.team = team
    logos_nhl.url = url

    db.session.commit()
    return jsonify({"msg": "logos_nhl edith successfully"}), 200

@app.route('/logos_soccer/<id>', methods=['PUT'])
def newslogos_soccer(id):
    logos_soccer = Logos_SOCCER.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_soccer.team = team
    logos_soccer.url = url

    db.session.commit()
    return jsonify({"msg": "logos_soccer edith successfully"}), 200

@app.route('/logos_ncaa_basketball/<id>', methods=['PUT'])
def newslogos_ncaa_basketball(id):
    logos_ncaa_basketball = Logos_Ncaa_Basketball.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_ncaa_basketball.team = team
    logos_ncaa_basketball.url = url

    db.session.commit()
    return jsonify({"msg": "logos_ncaa_basketball edith successfully"}), 200

@app.route('/logos_ncaa_football/<id>', methods=['PUT'])
def newslogos_ncaa_football(id):
    logos_ncaa_football = Logos_Ncaa_Football.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_ncaa_football.team = team
    logos_ncaa_football.url = url

    db.session.commit()
    return jsonify({"msg": "logos_ncaa_football edith successfully"}), 200

@app.route('/logos_ncaa_baseball/<id>', methods=['PUT'])
def newslogos_ncaa_baseball(id):
    logos_ncaa_baseball = Logos_Ncaa_Baseball.query.get(id)
    team = request.json['team']
    url = request.json['url']
    logos_ncaa_baseball.team = team
    logos_ncaa_baseball.url = url

    db.session.commit()
    return jsonify({"msg": "logos_ncaa_baseball edith successfully"}), 200

@app.route('/soccer_tournament/<id>', methods=['PUT'])
def newTournament(id):
    soccer_tournament = Soccer_Tournament.query.get(id)
    tournament = request.json['tournament']
    country = request.json['country']

    soccer_tournament.tournament = tournament
    soccer_tournament.country = country

    db.session.commit()
    return jsonify({"msg": "soccer tournament edith successfully"}), 200


@app.route('/mlb/<id>', methods=['PUT'])
def mlbEdit(id):
    mlb = Mlb.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    casino = request.json['casino']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    away = request.json['away']
    pitcher_a = request.json['pitcher_a']
    home = request.json['home']
    pitcher_h = request.json['pitcher_h']
    rl_away = request.json['rl_away']
    rl_home = request.json['rl_home']
    juice_rl_away = request.json['juice_rl_away']
    juice_rl_home = request.json['juice_rl_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']

    rl_away_f5 = request.json['rl_away_f5']
    rl_home_f5 = request.json['rl_home_f5']
    juice_rl_away_f5 = request.json['juice_rl_away_f5']
    juice_rl_home_f5 = request.json['juice_rl_home_f5']
    moneyLineAway_f5 = request.json['moneyLineAway_f5']
    moneyLineHome_f5 = request.json['moneyLineHome_f5']
    total_f5 = request.json['total_f5']
    juice_total_over_f5 = request.json['juice_total_over_f5']
    juice_total_under_f5 = request.json['juice_total_under_f5']
    tt_away_f5 = request.json['tt_away_f5']
    juice_over_away_f5 = request.json['juice_over_away_f5']
    juice_under_away_f5 = request.json['juice_under_away_f5']
    tt_home_f5 = request.json['tt_home_f5']
    juice_over_home_f5 = request.json['juice_over_home_f5']
    juice_under_home_f5 = request.json['juice_under_home_f5']
    fs_away_f5 = request.json['fs_away_f5']
    fs_home_f5 = request.json['fs_home_f5']
    sa_1inning = request.json['sa_1inning']
    sh_1inning = request.json['sh_1inning']
    sa_2inning = request.json['sa_2inning']
    sh_2inning = request.json['sh_2inning']
    sa_3inning = request.json['sa_3inning']
    sh_3inning = request.json['sh_3inning']
    sa_4inning = request.json['sa_4inning']
    sh_4inning = request.json['sh_4inning']
    sa_5inning = request.json['sa_5inning']
    sh_5inning = request.json['sh_5inning']
    sa_6inning = request.json['sa_6inning']
    sh_6inning = request.json['sh_6inning']
    sa_7inning = request.json['sa_7inning']
    sh_7inning = request.json['sh_7inning']
    sa_8inning = request.json['sa_8inning']
    sh_8inning = request.json['sh_8inning']
    sa_9inning = request.json['sa_9inning']
    sh_9inning = request.json['sh_9inning']
    sa_10inning = request.json['sa_10inning']
    sh_10inning = request.json['sh_10inning']
    sa_11inning = request.json['sa_11inning']
    sh_11inning = request.json['sh_11inning']
    sa_12inning = request.json['sa_12inning']
    sh_12inning = request.json['sh_12inning']
    sa_13inning = request.json['sa_13inning']
    sh_13inning = request.json['sh_13inning']
    sa_14inning = request.json['sa_14inning']
    sh_14inning = request.json['sh_14inning']
    sa_15inning = request.json['sa_15inning']
    sh_15inning = request.json['sh_15inning']
    sa_16inning = request.json['sa_16inning']
    sh_16inning = request.json['sh_16inning']
    sa_17inning = request.json['sa_17inning']
    sh_17inning = request.json['sh_17inning']
    sa_18inning = request.json['sa_18inning']
    sh_18inning = request.json['sh_18inning']
    sa_19inning = request.json['sa_19inning']
    sh_19inning = request.json['sh_19inning']
    sa_20inning = request.json['sa_20inning']
    sh_20inning = request.json['sh_20inning']
    sa_21inning = request.json['sa_21inning']
    sh_21inning = request.json['sh_21inning']
    sa_22inning = request.json['sa_22inning']
    sh_22inning = request.json['sh_22inning']
    sa_23inning = request.json['sa_23inning']
    sh_23inning = request.json['sh_23inning']
    sa_24inning = request.json['sa_24inning']
    sh_24inning = request.json['sh_24inning']
    sa_25inning = request.json['sa_25inning']
    sh_25inning = request.json['sh_25inning']
    mlb.date = date
    mlb.hour = hour
    mlb.status = status
    mlb.rotation_away = rotation_away
    mlb.rotation_home = rotation_home
    mlb.casino = casino
    mlb.away = away
    mlb.pitcher_a = pitcher_a
    mlb.home = home
    mlb.pitcher_h = pitcher_h
    mlb.rl_away = rl_away
    mlb.rl_home = rl_home
    mlb.juice_rl_away = juice_rl_away
    mlb.juice_rl_home = juice_rl_home
    mlb.moneyLineAway = moneyLineAway
    mlb.moneyLineHome = moneyLineHome
    mlb.total = total
    mlb.juice_total_over = juice_total_over
    mlb.juice_total_under = juice_total_under
    mlb.tt_away = tt_away
    mlb.juice_over_away = juice_over_away
    mlb.juice_under_away = juice_under_away
    mlb.tt_home = tt_home
    mlb.juice_over_home = juice_over_home
    mlb.juice_under_home = juice_under_home
    mlb.final_score_away = final_score_away
    mlb.final_score_home = final_score_home
    mlb.final_score_home = final_score_home
    mlb.rl_home_f5 = rl_home_f5
    mlb.juice_rl_away_f5 = juice_rl_away_f5
    mlb.juice_rl_home_f5 = juice_rl_home_f5
    mlb.moneyLineAway_f5 = moneyLineAway_f5
    mlb.moneyLineHome_f5 = moneyLineHome_f5
    mlb.total_f5 = total_f5
    mlb.juice_total_over_f5 = juice_total_over_f5
    mlb.juice_total_under_f5 = juice_total_under_f5
    mlb.tt_away_f5 = tt_away_f5
    mlb.juice_over_away_f5 = juice_over_away_f5
    mlb.juice_under_away_f5 = juice_under_away_f5
    mlb.tt_home_f5 = tt_home_f5
    mlb.juice_over_home_f5 = juice_over_home_f5
    mlb.juice_under_home_f5 = juice_under_home_f5
    mlb.fs_away_f5 = fs_away_f5
    mlb.fs_home_f5 = fs_home_f5
    mlb.sa_1inning = sa_1inning
    mlb.sh_1inning = sh_1inning
    mlb.sa_2inning = sa_2inning
    mlb.sh_2inning = sh_2inning
    mlb.sa_3inning = sa_3inning
    mlb.sh_3inning = sh_3inning
    mlb.sa_4inning = sa_4inning
    mlb.sh_4inning = sh_4inning
    mlb.sa_5inning = sa_5inning
    mlb.sh_5inning = sh_5inning
    mlb.sa_6inning = sa_6inning
    mlb.sh_6inning = sh_6inning
    mlb.sa_7inning = sa_7inning
    mlb.sh_7inning = sh_7inning
    mlb.sa_8inning = sa_8inning
    mlb.sh_8inning = sh_8inning
    mlb.sa_9inning = sa_9inning
    mlb.sh_9inning = sh_9inning
    mlb.sa_10inning = sa_10inning
    mlb.sh_10inning = sh_10inning
    mlb.sa_11inning = sa_11inning
    mlb.sh_11inning = sh_11inning
    mlb.sa_12inning = sa_12inning
    mlb.sh_12inning = sh_12inning
    mlb.sa_13inning = sa_13inning
    mlb.sh_13inning = sh_13inning
    mlb.sa_14inning = sa_14inning
    mlb.sh_14inning = sh_14inning
    mlb.sa_15inning = sa_15inning
    mlb.sh_15inning = sh_15inning
    mlb.sa_16inning = sa_16inning
    mlb.sh_16inning = sh_16inning
    mlb.sa_17inning = sa_17inning
    mlb.sh_17inning = sh_17inning
    mlb.sa_18inning = sa_18inning
    mlb.sh_18inning = sh_18inning
    mlb.sa_19inning = sa_19inning
    mlb.sh_19inning = sh_19inning
    mlb.sa_20inning = sa_20inning
    mlb.sh_20inning = sh_20inning
    mlb.sa_21inning = sa_21inning
    mlb.sh_21inning = sh_21inning
    mlb.sa_22inning = sa_22inning
    mlb.sh_22inning = sh_22inning
    mlb.sa_23inning = sa_23inning
    mlb.sh_23inning = sh_23inning
    mlb.sa_24inning = sa_24inning
    mlb.sh_24inning = sh_24inning
    mlb.sa_25inning = sa_25inning
    mlb.sh_25inning = sh_25inning
    db.session.commit()
    return jsonify({"msg": "Mlb match edith successfully"}), 200


@app.route('/ncaa_baseball/<id>', methods=['PUT'])
def ncaa_baseballEdit(id):
    ncaa_baseball = Ncaa_Baseball.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    casino = request.json['casino']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    away = request.json['away']
    pitcher_a = request.json['pitcher_a']
    home = request.json['home']
    pitcher_h = request.json['pitcher_h']
    rl_away = request.json['rl_away']
    rl_home = request.json['rl_home']
    juice_rl_away = request.json['juice_rl_away']
    juice_rl_home = request.json['juice_rl_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']

    rl_away_f5 = request.json['rl_away_f5']
    rl_home_f5 = request.json['rl_home_f5']
    juice_rl_away_f5 = request.json['juice_rl_away_f5']
    juice_rl_home_f5 = request.json['juice_rl_home_f5']
    moneyLineAway_f5 = request.json['moneyLineAway_f5']
    moneyLineHome_f5 = request.json['moneyLineHome_f5']
    total_f5 = request.json['total_f5']
    juice_total_over_f5 = request.json['juice_total_over_f5']
    juice_total_under_f5 = request.json['juice_total_under_f5']
    tt_away_f5 = request.json['tt_away_f5']
    juice_over_away_f5 = request.json['juice_over_away_f5']
    juice_under_away_f5 = request.json['juice_under_away_f5']
    tt_home_f5 = request.json['tt_home_f5']
    juice_over_home_f5 = request.json['juice_over_home_f5']
    juice_under_home_f5 = request.json['juice_under_home_f5']
    fs_away_f5 = request.json['fs_away_f5']
    fs_home_f5 = request.json['fs_home_f5']
    sa_1inning = request.json['sa_1inning']
    sh_1inning = request.json['sh_1inning']
    sa_2inning = request.json['sa_2inning']
    sh_2inning = request.json['sh_2inning']
    sa_3inning = request.json['sa_3inning']
    sh_3inning = request.json['sh_3inning']
    sa_4inning = request.json['sa_4inning']
    sh_4inning = request.json['sh_4inning']
    sa_5inning = request.json['sa_5inning']
    sh_5inning = request.json['sh_5inning']
    sa_6inning = request.json['sa_6inning']
    sh_6inning = request.json['sh_6inning']
    sa_7inning = request.json['sa_7inning']
    sh_7inning = request.json['sh_7inning']
    sa_8inning = request.json['sa_8inning']
    sh_8inning = request.json['sh_8inning']
    sa_9inning = request.json['sa_9inning']
    sh_9inning = request.json['sh_9inning']
    sa_10inning = request.json['sa_10inning']
    sh_10inning = request.json['sh_10inning']
    sa_11inning = request.json['sa_11inning']
    sh_11inning = request.json['sh_11inning']
    sa_12inning = request.json['sa_12inning']
    sh_12inning = request.json['sh_12inning']
    sa_13inning = request.json['sa_13inning']
    sh_13inning = request.json['sh_13inning']
    sa_14inning = request.json['sa_14inning']
    sh_14inning = request.json['sh_14inning']
    sa_15inning = request.json['sa_15inning']
    sh_15inning = request.json['sh_15inning']
    sa_16inning = request.json['sa_16inning']
    sh_16inning = request.json['sh_16inning']
    sa_17inning = request.json['sa_17inning']
    sh_17inning = request.json['sh_17inning']
    sa_18inning = request.json['sa_18inning']
    sh_18inning = request.json['sh_18inning']
    sa_19inning = request.json['sa_19inning']
    sh_19inning = request.json['sh_19inning']
    sa_20inning = request.json['sa_20inning']
    sh_20inning = request.json['sh_20inning']
    sa_21inning = request.json['sa_21inning']
    sh_21inning = request.json['sh_21inning']
    sa_22inning = request.json['sa_22inning']
    sh_22inning = request.json['sh_22inning']
    sa_23inning = request.json['sa_23inning']
    sh_23inning = request.json['sh_23inning']
    sa_24inning = request.json['sa_24inning']
    sh_24inning = request.json['sh_24inning']
    sa_25inning = request.json['sa_25inning']
    sh_25inning = request.json['sh_25inning']
    ncaa_baseball.date = date
    ncaa_baseball.hour = hour
    ncaa_baseball.status = status
    ncaa_baseball.rotation_away = rotation_away
    ncaa_baseball.rotation_home = rotation_home
    ncaa_baseball.casino = casino
    ncaa_baseball.away = away
    ncaa_baseball.pitcher_a = pitcher_a
    ncaa_baseball.home = home
    ncaa_baseball.pitcher_h = pitcher_h
    ncaa_baseball.rl_away = rl_away
    ncaa_baseball.rl_home = rl_home
    ncaa_baseball.juice_rl_away = juice_rl_away
    ncaa_baseball.juice_rl_home = juice_rl_home
    ncaa_baseball.moneyLineAway = moneyLineAway
    ncaa_baseball.moneyLineHome = moneyLineHome
    ncaa_baseball.total = total
    ncaa_baseball.juice_total_over = juice_total_over
    ncaa_baseball.juice_total_under = juice_total_under
    ncaa_baseball.tt_away = tt_away
    ncaa_baseball.juice_over_away = juice_over_away
    ncaa_baseball.juice_under_away = juice_under_away
    ncaa_baseball.tt_home = tt_home
    ncaa_baseball.juice_over_home = juice_over_home
    ncaa_baseball.juice_under_home = juice_under_home
    ncaa_baseball.final_score_away = final_score_away
    ncaa_baseball.final_score_home = final_score_home
    ncaa_baseball.final_score_home = final_score_home
    ncaa_baseball.rl_home_f5 = rl_home_f5
    ncaa_baseball.juice_rl_away_f5 = juice_rl_away_f5
    ncaa_baseball.juice_rl_home_f5 = juice_rl_home_f5
    ncaa_baseball.moneyLineAway_f5 = moneyLineAway_f5
    ncaa_baseball.moneyLineHome_f5 = moneyLineHome_f5
    ncaa_baseball.total_f5 = total_f5
    ncaa_baseball.juice_total_over_f5 = juice_total_over_f5
    ncaa_baseball.juice_total_under_f5 = juice_total_under_f5
    ncaa_baseball.tt_away_f5 = tt_away_f5
    ncaa_baseball.juice_over_away_f5 = juice_over_away_f5
    ncaa_baseball.juice_under_away_f5 = juice_under_away_f5
    ncaa_baseball.tt_home_f5 = tt_home_f5
    ncaa_baseball.juice_over_home_f5 = juice_over_home_f5
    ncaa_baseball.juice_under_home_f5 = juice_under_home_f5
    ncaa_baseball.fs_away_f5 = fs_away_f5
    ncaa_baseball.fs_home_f5 = fs_home_f5
    ncaa_baseball.sa_1inning = sa_1inning
    ncaa_baseball.sh_1inning = sh_1inning
    ncaa_baseball.sa_2inning = sa_2inning
    ncaa_baseball.sh_2inning = sh_2inning
    ncaa_baseball.sa_3inning = sa_3inning
    ncaa_baseball.sh_3inning = sh_3inning
    ncaa_baseball.sa_4inning = sa_4inning
    ncaa_baseball.sh_4inning = sh_4inning
    ncaa_baseball.sa_5inning = sa_5inning
    ncaa_baseball.sh_5inning = sh_5inning
    ncaa_baseball.sa_6inning = sa_6inning
    ncaa_baseball.sh_6inning = sh_6inning
    ncaa_baseball.sa_7inning = sa_7inning
    ncaa_baseball.sh_7inning = sh_7inning
    ncaa_baseball.sa_8inning = sa_8inning
    ncaa_baseball.sh_8inning = sh_8inning
    ncaa_baseball.sa_9inning = sa_9inning
    ncaa_baseball.sh_9inning = sh_9inning
    ncaa_baseball.sa_10inning = sa_10inning
    ncaa_baseball.sh_10inning = sh_10inning
    ncaa_baseball.sa_11inning = sa_11inning
    ncaa_baseball.sh_11inning = sh_11inning
    ncaa_baseball.sa_12inning = sa_12inning
    ncaa_baseball.sh_12inning = sh_12inning
    ncaa_baseball.sa_13inning = sa_13inning
    ncaa_baseball.sh_13inning = sh_13inning
    ncaa_baseball.sa_14inning = sa_14inning
    ncaa_baseball.sh_14inning = sh_14inning
    ncaa_baseball.sa_15inning = sa_15inning
    ncaa_baseball.sh_15inning = sh_15inning
    ncaa_baseball.sa_16inning = sa_16inning
    ncaa_baseball.sh_16inning = sh_16inning
    ncaa_baseball.sa_17inning = sa_17inning
    ncaa_baseball.sh_17inning = sh_17inning
    ncaa_baseball.sa_18inning = sa_18inning
    ncaa_baseball.sh_18inning = sh_18inning
    ncaa_baseball.sa_19inning = sa_19inning
    ncaa_baseball.sh_19inning = sh_19inning
    ncaa_baseball.sa_20inning = sa_20inning
    ncaa_baseball.sh_20inning = sh_20inning
    ncaa_baseball.sa_21inning = sa_21inning
    ncaa_baseball.sh_21inning = sh_21inning
    ncaa_baseball.sa_22inning = sa_22inning
    ncaa_baseball.sh_22inning = sh_22inning
    ncaa_baseball.sa_23inning = sa_23inning
    ncaa_baseball.sh_23inning = sh_23inning
    ncaa_baseball.sa_24inning = sa_24inning
    ncaa_baseball.sh_24inning = sh_24inning
    ncaa_baseball.sa_25inning = sa_25inning
    ncaa_baseball.sh_25inning = sh_25inning
    db.session.commit()
    return jsonify({"msg": "ncaa_baseball edith successfully"}), 200

@app.route('/stats_ncaa_baseball_team/<id>', methods=['PUT'])
def stats_ncaa_baseball_teamEdit(id):
    stats_ncaa_baseball_team = Stats_ncaa_baseball_team.query.get(id)
    season = request.json['season']
    team = request.json['team']
    league = request.json['league']
    division = request.json['division']
    w = request.json['w']
    L = request.json['L']
    pct = request.json['pct']
    gb = request.json['gb']
    home = request.json['home']
    away = request.json['away']
    rs = request.json['rs']
    ra = request.json['ra']
    diff = request.json['diff']
    strk = request.json['strk']
    L10 = request.json['L10']
    poff = request.json['poff']

    stats_ncaa_baseball_team.season = season
    stats_ncaa_baseball_team.team = team
    stats_ncaa_baseball_team.league = league
    stats_ncaa_baseball_team.division = division
    stats_ncaa_baseball_team.w = w
    stats_ncaa_baseball_team.L = L
    stats_ncaa_baseball_team.pct = pct
    stats_ncaa_baseball_team.gb = gb
    stats_ncaa_baseball_team.home = home
    stats_ncaa_baseball_team.away = away
    stats_ncaa_baseball_team.rs = rs
    stats_ncaa_baseball_team.ra = ra
    stats_ncaa_baseball_team.diff = diff
    stats_ncaa_baseball_team.strk = strk
    stats_ncaa_baseball_team.L10 = L10
    stats_ncaa_baseball_team.poff = poff

    db.session.commit()
    return jsonify({"msg": "stats_ncaa_baseball_team edith successfully"}), 200


@app.route('/nfl/<id>', methods=['PUT'])
def nflEdit(id):
    nfl = Nfl.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    # --
    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_total = request.json['first_half_total']
    fh_juice_total_over = request.json['fh_juice_total_over']
    fh_juice_total_under = request.json['fh_juice_total_under']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    # --
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_total = request.json['second_half_total']
    sh_juice_total_over = request.json['sh_juice_total_over']
    sh_juice_total_under = request.json['sh_juice_total_under']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    # --
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_under_away = request.json['q1_half_juice_under_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_juice_under_home = request.json['q1_half_juice_under_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']
    # --
    q2_half_spread_away = request.json['q2_half_spread_away']
    q2_half_spread_home = request.json['q2_half_spread_home']
    q2_half_juice_spread_away = request.json['q2_half_juice_spread_away']
    q2_half_juice_spread_home = request.json['q2_half_juice_spread_home']
    q2_half_moneyLineAway = request.json['q2_half_moneyLineAway']
    q2_half_moneyLineHome = request.json['q2_half_moneyLineHome']
    q2_half_total = request.json['q2_half_total']
    q2_juice_over = request.json['q2_juice_over']
    q2_juice_under = request.json['q2_juice_under']
    q2_half_tt_away = request.json['q2_half_tt_away']
    q2_half_juice_over_away = request.json['q2_half_juice_over_away']
    q2_half_juice_under_away = request.json['q2_half_juice_under_away']
    q2_half_tt_home = request.json['q2_half_tt_home']
    q2_half_juice_over_home = request.json['q2_half_juice_over_home']
    q2_half_juice_under_home = request.json['q2_half_juice_under_home']
    q2_half_final_score_away = request.json['q2_half_final_score_away']
    q2_half_final_score_home = request.json['q2_half_final_score_home']
    # --
    q3_half_spread_away = request.json['q3_half_spread_away']
    q3_half_spread_home = request.json['q3_half_spread_home']
    q3_half_juice_spread_away = request.json['q3_half_juice_spread_away']
    q3_half_juice_spread_home = request.json['q3_half_juice_spread_home']
    q3_half_moneyLineAway = request.json['q3_half_moneyLineAway']
    q3_half_moneyLineHome = request.json['q3_half_moneyLineHome']
    q3_half_total = request.json['q3_half_total']
    q3_juice_over = request.json['q3_juice_over']
    q3_juice_under = request.json['q3_juice_under']
    q3_half_tt_away = request.json['q3_half_tt_away']
    q3_half_juice_over_away = request.json['q3_half_juice_over_away']
    q3_half_juice_under_away = request.json['q3_half_juice_under_away']
    q3_half_tt_home = request.json['q3_half_tt_home']
    q3_half_juice_over_home = request.json['q3_half_juice_over_home']
    q3_half_juice_under_home = request.json['q3_half_juice_under_home']
    q3_half_final_score_away = request.json['q3_half_final_score_away']
    q3_half_final_score_home = request.json['q3_half_final_score_home']
    # --
    q4_half_spread_away = request.json['q4_half_spread_away']
    q4_half_spread_home = request.json['q4_half_spread_home']
    q4_half_juice_spread_away = request.json['q4_half_juice_spread_away']
    q4_half_juice_spread_home = request.json['q4_half_juice_spread_home']
    q4_half_moneyLineAway = request.json['q4_half_moneyLineAway']
    q4_half_moneyLineHome = request.json['q4_half_moneyLineHome']
    q4_half_total = request.json['q4_half_total']
    q4_juice_over = request.json['q4_juice_over']
    q4_juice_under = request.json['q4_juice_under']
    q4_half_tt_away = request.json['q4_half_tt_away']
    q4_half_juice_over_away = request.json['q4_half_juice_over_away']
    q4_half_juice_under_away = request.json['q4_half_juice_under_away']
    q4_half_tt_home = request.json['q4_half_tt_home']
    q4_half_juice_over_home = request.json['q4_half_juice_over_home']
    q4_half_juice_under_home = request.json['q4_half_juice_under_home']
    q4_half_final_score_away = request.json['q4_half_final_score_away']
    q4_half_final_score_home = request.json['q4_half_final_score_home']

    nfl.date = date
    nfl.hour = hour
    nfl.week = week
    nfl.status = status
    nfl.casino = casino
    nfl.rotation_away = rotation_away
    nfl.rotation_home = rotation_home
    nfl.away = away
    nfl.home = home
    nfl.spread_away = spread_away
    nfl.spread_home = spread_home
    nfl.juice_spread_away = juice_spread_away
    nfl.juice_spread_home = juice_spread_home
    nfl.moneyLineAway = moneyLineAway
    nfl.moneyLineHome = moneyLineHome
    nfl.total = total
    nfl.juice_total_over = juice_total_over
    nfl.juice_total_under = juice_total_under
    nfl.tt_away = tt_away
    nfl.juice_over_away = juice_over_away
    nfl.juice_under_away = juice_under_away
    nfl.tt_home = tt_home
    nfl.juice_over_home = juice_over_home
    nfl.juice_under_home = juice_under_home
    nfl.final_score_away = final_score_away
    nfl.final_score_home = final_score_home

    nfl.first_half_spread_away = first_half_spread_away
    nfl.first_half_spread_home = first_half_spread_home
    nfl.first_half_juice_spread_away = first_half_juice_spread_away
    nfl.first_half_juice_spread_home = first_half_juice_spread_home
    nfl.first_half_moneyLineAway = first_half_moneyLineAway
    nfl.first_half_moneyLineHome = first_half_moneyLineHome
    nfl.first_half_total = first_half_total
    nfl.fh_juice_total_over = fh_juice_total_over
    nfl.fh_juice_total_under = fh_juice_total_under
    nfl.first_half_tt_away = first_half_tt_away
    nfl.first_half_juice_over_away = first_half_juice_over_away
    nfl.first_half_juice_under_away = first_half_juice_under_away
    nfl.first_half_tt_home = first_half_tt_home
    nfl.first_half_juice_over_home = first_half_juice_over_home
    nfl.first_half_juice_under_home = first_half_juice_under_home
    nfl.first_half_final_score_away = first_half_final_score_away
    nfl.first_half_final_score_home = first_half_final_score_home
    # --
    nfl.second_half_spread_away = second_half_spread_away
    nfl.second_half_spread_home = second_half_spread_home
    nfl.second_half_juice_spread_away = second_half_juice_spread_away
    nfl.second_half_juice_spread_home = second_half_juice_spread_home
    nfl.second_half_moneyLineAway = second_half_moneyLineAway
    nfl.second_half_moneyLineHome = second_half_moneyLineHome
    nfl.second_half_total = second_half_total
    nfl.sh_juice_total_over = sh_juice_total_over
    nfl.sh_juice_total_under = sh_juice_total_under
    nfl.second_half_tt_away = second_half_tt_away
    nfl.second_half_juice_over_away = second_half_juice_over_away
    nfl.second_half_juice_under_away = second_half_juice_under_away
    nfl.second_half_tt_home = second_half_tt_home
    nfl.second_half_juice_over_home = second_half_juice_over_home
    nfl.second_half_juice_under_home = second_half_juice_under_home
    nfl.second_half_final_score_away = second_half_final_score_away
    nfl.second_half_final_score_home = second_half_final_score_home
    # --
    nfl.q1_half_spread_away = q1_half_spread_away
    nfl.q1_half_spread_home = q1_half_spread_home
    nfl.q1_half_juice_spread_away = q1_half_juice_spread_away
    nfl.q1_half_juice_spread_home = q1_half_juice_spread_home
    nfl.q1_half_moneyLineAway = q1_half_moneyLineAway
    nfl.q1_half_moneyLineHome = q1_half_moneyLineHome
    nfl.q1_half_total = q1_half_total
    nfl.q1_juice_over = q1_juice_over
    nfl.q1_juice_under = q1_juice_under
    nfl.q1_half_tt_away = q1_half_tt_away
    nfl.q1_half_juice_over_away = q1_half_juice_over_away
    nfl.q1_half_juice_under_away = q1_half_juice_under_away
    nfl.q1_half_tt_home = q1_half_tt_home
    nfl.q1_half_juice_over_home = q1_half_juice_over_home
    nfl.q1_half_juice_under_home = q1_half_juice_under_home
    nfl.q1_half_final_score_away = q1_half_final_score_away
    nfl.q1_half_final_score_home = q1_half_final_score_home
    # --
    nfl.q2_half_spread_away = q2_half_spread_away
    nfl.q2_half_spread_home = q2_half_spread_home
    nfl.q2_half_juice_spread_away = q2_half_juice_spread_away
    nfl.q2_half_juice_spread_home = q2_half_juice_spread_home
    nfl.q2_half_moneyLineAway = q2_half_moneyLineAway
    nfl.q2_half_moneyLineHome = q2_half_moneyLineHome
    nfl.q2_half_total = q2_half_total
    nfl.q2_juice_over = q2_juice_over
    nfl.q2_juice_under = q2_juice_under
    nfl.q2_half_tt_away = q2_half_tt_away
    nfl.q2_half_juice_over_away = q2_half_juice_over_away
    nfl.q2_half_juice_under_away = q2_half_juice_under_away
    nfl.q2_half_tt_home = q2_half_tt_home
    nfl.q2_half_juice_over_home = q2_half_juice_over_home
    nfl.q2_half_juice_under_home = q2_half_juice_under_home
    nfl.q2_half_final_score_away = q2_half_final_score_away
    nfl.q2_half_final_score_home = q2_half_final_score_home
    # --
    nfl.q3_half_spread_away = q3_half_spread_away
    nfl.q3_half_spread_home = q3_half_spread_home
    nfl.q3_half_juice_spread_away = q3_half_juice_spread_away
    nfl.q3_half_juice_spread_home = q3_half_juice_spread_home
    nfl.q3_half_moneyLineAway = q3_half_moneyLineAway
    nfl.q3_half_moneyLineHome = q3_half_moneyLineHome
    nfl.q3_half_total = q3_half_total
    nfl.q3_juice_over = q3_juice_over
    nfl.q3_juice_under = q3_juice_under
    nfl.q3_half_tt_away = q3_half_tt_away
    nfl.q3_half_juice_over_away = q3_half_juice_over_away
    nfl.q3_half_juice_under_away = q3_half_juice_under_away
    nfl.q3_half_tt_home = q3_half_tt_home
    nfl.q3_half_juice_over_home = q3_half_juice_over_home
    nfl.q3_half_juice_under_home = q3_half_juice_under_home
    nfl.q3_half_final_score_away = q3_half_final_score_away
    nfl.q3_half_final_score_home = q3_half_final_score_home
    # --
    nfl.q4_half_spread_away = q4_half_spread_away
    nfl.q4_half_spread_home = q4_half_spread_home
    nfl.q4_half_juice_spread_away = q4_half_juice_spread_away
    nfl.q4_half_juice_spread_home = q4_half_juice_spread_home
    nfl.q4_half_moneyLineAway = q4_half_moneyLineAway
    nfl.q4_half_moneyLineHome = q4_half_moneyLineHome
    nfl.q4_half_total = q4_half_total
    nfl.q4_juice_over = q4_juice_over
    nfl.q4_juice_under = q4_juice_under
    nfl.q4_half_tt_away = q4_half_tt_away
    nfl.q4_half_juice_over_away = q4_half_juice_over_away
    nfl.q4_half_juice_under_away = q4_half_juice_under_away
    nfl.q4_half_tt_home = q4_half_tt_home
    nfl.q4_half_juice_over_home = q4_half_juice_over_home
    nfl.q4_half_juice_under_home = q4_half_juice_under_home
    nfl.q4_half_final_score_away = q4_half_final_score_away
    nfl.q4_half_final_score_home = q4_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "nfl edith successfully"}), 200


@app.route('/ncaa_football/<id>', methods=['PUT'])
def ncaa_footballEdit(id):
    ncaa_football = Ncaa_Football.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    # --
    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_total = request.json['first_half_total']
    fh_juice_total_over = request.json['fh_juice_total_over']
    fh_juice_total_under = request.json['fh_juice_total_under']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    # --
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_total = request.json['second_half_total']
    sh_juice_total_over = request.json['sh_juice_total_over']
    sh_juice_total_under = request.json['sh_juice_total_under']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    # --
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_under_away = request.json['q1_half_juice_under_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_juice_under_home = request.json['q1_half_juice_under_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']
    # --
    q2_half_spread_away = request.json['q2_half_spread_away']
    q2_half_spread_home = request.json['q2_half_spread_home']
    q2_half_juice_spread_away = request.json['q2_half_juice_spread_away']
    q2_half_juice_spread_home = request.json['q2_half_juice_spread_home']
    q2_half_moneyLineAway = request.json['q2_half_moneyLineAway']
    q2_half_moneyLineHome = request.json['q2_half_moneyLineHome']
    q2_half_total = request.json['q2_half_total']
    q2_juice_over = request.json['q2_juice_over']
    q2_juice_under = request.json['q2_juice_under']
    q2_half_tt_away = request.json['q2_half_tt_away']
    q2_half_juice_over_away = request.json['q2_half_juice_over_away']
    q2_half_juice_under_away = request.json['q2_half_juice_under_away']
    q2_half_tt_home = request.json['q2_half_tt_home']
    q2_half_juice_over_home = request.json['q2_half_juice_over_home']
    q2_half_juice_under_home = request.json['q2_half_juice_under_home']
    q2_half_final_score_away = request.json['q2_half_final_score_away']
    q2_half_final_score_home = request.json['q2_half_final_score_home']
    # --
    q3_half_spread_away = request.json['q3_half_spread_away']
    q3_half_spread_home = request.json['q3_half_spread_home']
    q3_half_juice_spread_away = request.json['q3_half_juice_spread_away']
    q3_half_juice_spread_home = request.json['q3_half_juice_spread_home']
    q3_half_moneyLineAway = request.json['q3_half_moneyLineAway']
    q3_half_moneyLineHome = request.json['q3_half_moneyLineHome']
    q3_half_total = request.json['q3_half_total']
    q3_juice_over = request.json['q3_juice_over']
    q3_juice_under = request.json['q3_juice_under']
    q3_half_tt_away = request.json['q3_half_tt_away']
    q3_half_juice_over_away = request.json['q3_half_juice_over_away']
    q3_half_juice_under_away = request.json['q3_half_juice_under_away']
    q3_half_tt_home = request.json['q3_half_tt_home']
    q3_half_juice_over_home = request.json['q3_half_juice_over_home']
    q3_half_juice_under_home = request.json['q3_half_juice_under_home']
    q3_half_final_score_away = request.json['q3_half_final_score_away']
    q3_half_final_score_home = request.json['q3_half_final_score_home']
    # --
    q4_half_spread_away = request.json['q4_half_spread_away']
    q4_half_spread_home = request.json['q4_half_spread_home']
    q4_half_juice_spread_away = request.json['q4_half_juice_spread_away']
    q4_half_juice_spread_home = request.json['q4_half_juice_spread_home']
    q4_half_moneyLineAway = request.json['q4_half_moneyLineAway']
    q4_half_moneyLineHome = request.json['q4_half_moneyLineHome']
    q4_half_total = request.json['q4_half_total']
    q4_juice_over = request.json['q4_juice_over']
    q4_juice_under = request.json['q4_juice_under']
    q4_half_tt_away = request.json['q4_half_tt_away']
    q4_half_juice_over_away = request.json['q4_half_juice_over_away']
    q4_half_juice_under_away = request.json['q4_half_juice_under_away']
    q4_half_tt_home = request.json['q4_half_tt_home']
    q4_half_juice_over_home = request.json['q4_half_juice_over_home']
    q4_half_juice_under_home = request.json['q4_half_juice_under_home']
    q4_half_final_score_away = request.json['q4_half_final_score_away']
    q4_half_final_score_home = request.json['q4_half_final_score_home']

    ncaa_football.date = date
    ncaa_football.hour = hour
    ncaa_football.week = week
    ncaa_football.status = status
    ncaa_football.casino = casino
    ncaa_football.rotation_away = rotation_away
    ncaa_football.rotation_home = rotation_home
    ncaa_football.away = away
    ncaa_football.home = home
    ncaa_football.spread_away = spread_away
    ncaa_football.spread_home = spread_home
    ncaa_football.juice_spread_away = juice_spread_away
    ncaa_football.juice_spread_home = juice_spread_home
    ncaa_football.moneyLineAway = moneyLineAway
    ncaa_football.moneyLineHome = moneyLineHome
    ncaa_football.total = total
    ncaa_football.juice_total_over = juice_total_over
    ncaa_football.juice_total_under = juice_total_under
    ncaa_football.tt_away = tt_away
    ncaa_football.juice_over_away = juice_over_away
    ncaa_football.juice_under_away = juice_under_away
    ncaa_football.tt_home = tt_home
    ncaa_football.juice_over_home = juice_over_home
    ncaa_football.juice_under_home = juice_under_home
    ncaa_football.final_score_away = final_score_away
    ncaa_football.final_score_home = final_score_home

    ncaa_football.first_half_spread_away = first_half_spread_away
    ncaa_football.first_half_spread_home = first_half_spread_home
    ncaa_football.first_half_juice_spread_away = first_half_juice_spread_away
    ncaa_football.first_half_juice_spread_home = first_half_juice_spread_home
    ncaa_football.first_half_moneyLineAway = first_half_moneyLineAway
    ncaa_football.first_half_moneyLineHome = first_half_moneyLineHome
    ncaa_football.first_half_total = first_half_total
    ncaa_football.fh_juice_total_over = fh_juice_total_over
    ncaa_football.fh_juice_total_under = fh_juice_total_under
    ncaa_football.first_half_tt_away = first_half_tt_away
    ncaa_football.first_half_juice_over_away = first_half_juice_over_away
    ncaa_football.first_half_juice_under_away = first_half_juice_under_away
    ncaa_football.first_half_tt_home = first_half_tt_home
    ncaa_football.first_half_juice_over_home = first_half_juice_over_home
    ncaa_football.first_half_juice_under_home = first_half_juice_under_home
    ncaa_football.first_half_final_score_away = first_half_final_score_away
    ncaa_football.first_half_final_score_home = first_half_final_score_home
    # --
    ncaa_football.second_half_spread_away = second_half_spread_away
    ncaa_football.second_half_spread_home = second_half_spread_home
    ncaa_football.second_half_juice_spread_away = second_half_juice_spread_away
    ncaa_football.second_half_juice_spread_home = second_half_juice_spread_home
    ncaa_football.second_half_moneyLineAway = second_half_moneyLineAway
    ncaa_football.second_half_moneyLineHome = second_half_moneyLineHome
    ncaa_football.second_half_total = second_half_total
    ncaa_football.sh_juice_total_over = sh_juice_total_over
    ncaa_football.sh_juice_total_under = sh_juice_total_under
    ncaa_football.second_half_tt_away = second_half_tt_away
    ncaa_football.second_half_juice_over_away = second_half_juice_over_away
    ncaa_football.second_half_juice_under_away = second_half_juice_under_away
    ncaa_football.second_half_tt_home = second_half_tt_home
    ncaa_football.second_half_juice_over_home = second_half_juice_over_home
    ncaa_football.second_half_juice_under_home = second_half_juice_under_home
    ncaa_football.second_half_final_score_away = second_half_final_score_away
    ncaa_football.second_half_final_score_home = second_half_final_score_home
    # --
    ncaa_football.q1_half_spread_away = q1_half_spread_away
    ncaa_football.q1_half_spread_home = q1_half_spread_home
    ncaa_football.q1_half_juice_spread_away = q1_half_juice_spread_away
    ncaa_football.q1_half_juice_spread_home = q1_half_juice_spread_home
    ncaa_football.q1_half_moneyLineAway = q1_half_moneyLineAway
    ncaa_football.q1_half_moneyLineHome = q1_half_moneyLineHome
    ncaa_football.q1_half_total = q1_half_total
    ncaa_football.q1_juice_over = q1_juice_over
    ncaa_football.q1_juice_under = q1_juice_under
    ncaa_football.q1_half_tt_away = q1_half_tt_away
    ncaa_football.q1_half_juice_over_away = q1_half_juice_over_away
    ncaa_football.q1_half_juice_under_away = q1_half_juice_under_away
    ncaa_football.q1_half_tt_home = q1_half_tt_home
    ncaa_football.q1_half_juice_over_home = q1_half_juice_over_home
    ncaa_football.q1_half_juice_under_home = q1_half_juice_under_home
    ncaa_football.q1_half_final_score_away = q1_half_final_score_away
    ncaa_football.q1_half_final_score_home = q1_half_final_score_home
    # --
    ncaa_football.q2_half_spread_away = q2_half_spread_away
    ncaa_football.q2_half_spread_home = q2_half_spread_home
    ncaa_football.q2_half_juice_spread_away = q2_half_juice_spread_away
    ncaa_football.q2_half_juice_spread_home = q2_half_juice_spread_home
    ncaa_football.q2_half_moneyLineAway = q2_half_moneyLineAway
    ncaa_football.q2_half_moneyLineHome = q2_half_moneyLineHome
    ncaa_football.q2_half_total = q2_half_total
    ncaa_football.q2_juice_over = q2_juice_over
    ncaa_football.q2_juice_under = q2_juice_under
    ncaa_football.q2_half_tt_away = q2_half_tt_away
    ncaa_football.q2_half_juice_over_away = q2_half_juice_over_away
    ncaa_football.q2_half_juice_under_away = q2_half_juice_under_away
    ncaa_football.q2_half_tt_home = q2_half_tt_home
    ncaa_football.q2_half_juice_over_home = q2_half_juice_over_home
    ncaa_football.q2_half_juice_under_home = q2_half_juice_under_home
    ncaa_football.q2_half_final_score_away = q2_half_final_score_away
    ncaa_football.q2_half_final_score_home = q2_half_final_score_home
    # --
    ncaa_football.q3_half_spread_away = q3_half_spread_away
    ncaa_football.q3_half_spread_home = q3_half_spread_home
    ncaa_football.q3_half_juice_spread_away = q3_half_juice_spread_away
    ncaa_football.q3_half_juice_spread_home = q3_half_juice_spread_home
    ncaa_football.q3_half_moneyLineAway = q3_half_moneyLineAway
    ncaa_football.q3_half_moneyLineHome = q3_half_moneyLineHome
    ncaa_football.q3_half_total = q3_half_total
    ncaa_football.q3_juice_over = q3_juice_over
    ncaa_football.q3_juice_under = q3_juice_under
    ncaa_football.q3_half_tt_away = q3_half_tt_away
    ncaa_football.q3_half_juice_over_away = q3_half_juice_over_away
    ncaa_football.q3_half_juice_under_away = q3_half_juice_under_away
    ncaa_football.q3_half_tt_home = q3_half_tt_home
    ncaa_football.q3_half_juice_over_home = q3_half_juice_over_home
    ncaa_football.q3_half_juice_under_home = q3_half_juice_under_home
    ncaa_football.q3_half_final_score_away = q3_half_final_score_away
    ncaa_football.q3_half_final_score_home = q3_half_final_score_home
    # --
    ncaa_football.q4_half_spread_away = q4_half_spread_away
    ncaa_football.q4_half_spread_home = q4_half_spread_home
    ncaa_football.q4_half_juice_spread_away = q4_half_juice_spread_away
    ncaa_football.q4_half_juice_spread_home = q4_half_juice_spread_home
    ncaa_football.q4_half_moneyLineAway = q4_half_moneyLineAway
    ncaa_football.q4_half_moneyLineHome = q4_half_moneyLineHome
    ncaa_football.q4_half_total = q4_half_total
    ncaa_football.q4_juice_over = q4_juice_over
    ncaa_football.q4_juice_under = q4_juice_under
    ncaa_football.q4_half_tt_away = q4_half_tt_away
    ncaa_football.q4_half_juice_over_away = q4_half_juice_over_away
    ncaa_football.q4_half_juice_under_away = q4_half_juice_under_away
    ncaa_football.q4_half_tt_home = q4_half_tt_home
    ncaa_football.q4_half_juice_over_home = q4_half_juice_over_home
    ncaa_football.q4_half_juice_under_home = q4_half_juice_under_home
    ncaa_football.q4_half_final_score_away = q4_half_final_score_away
    ncaa_football.q4_half_final_score_home = q4_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "nfl edith successfully"}), 200

@app.route('/stats_ncaa_football_team/<id>', methods=['PUT'])
def stats_ncaa_football_teamEdit(id):
    stats_ncaa_football_team = Stats_ncaa_football_team.query.get(id)
    season = request.json['season']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']
    TP = request.json['TP']
    ttpg = request.json['ttpg']
    t_td = request.json['t_td']
    t_1_down = request.json['t_1_down']
    Russ_1_d = request.json['Russ_1_d']
    pass_1_d = request.json['pass_1_d']
    down_1_penal = request.json['down_1_penal']
    down_3_eff = request.json['down_3_eff']
    down_3_AVG = request.json['down_3_AVG']
    down_4_eff = request.json['down_4_eff']
    down_4_AVG = request.json['down_4_AVG']
    comp_att = request.json['comp_att']
    net_pass_y = request.json['net_pass_y']
    y_p_pas_attps = request.json['y_p_pas_attps']
    net_pass_y_pg = request.json['net_pass_y_pg']
    pass_td = request.json['pass_td']
    interceptions = request.json['interceptions']
    sacks_y_lost = request.json['sacks_y_lost']
    russ_attps = request.json['russ_attps']
    russ_y = request.json['russ_y']
    y_p_russ_attp = request.json['y_p_russ_attp']
    russ_y_pg = request.json['russ_y_pg']
    russ_td = request.json['russ_td']
    total_of_plays = request.json['total_of_plays']
    total_y = request.json['total_y']
    y_pg = request.json['y_pg']
    kickoffs_t = request.json['kickoffs_t']
    AVG_kickoff_return_y = request.json['AVG_kickoff_return_y']
    punt_t = request.json['punt_t']
    AVG_punt_ruturn_y = request.json['AVG_punt_ruturn_y']
    int_t = request.json['int_t']
    AVG_intercept_y = request.json['AVG_intercept_y']
    net_AVG_punt_y = request.json['net_AVG_punt_y']
    punt_ty = request.json['punt_ty']
    fg_goog_attps = request.json['fg_goog_attps']
    touchback_percent = request.json['touchback_percent']
    penal_ty = request.json['penal_ty']
    penal_y_AVG_pg = request.json['penal_y_AVG_pg']
    possesion_time = request.json['possesion_time']
    fumbles_lost = request.json['fumbles_lost']
    turnover_ratio = request.json['turnover_ratio']

    stats_ncaa_football_team.season = season
    stats_ncaa_football_team.team = team
    stats_ncaa_football_team.conference = conference
    stats_ncaa_football_team.division = division
    stats_ncaa_football_team.TP = TP
    stats_ncaa_football_team.ttpg = ttpg
    stats_ncaa_football_team.t_td = t_td
    stats_ncaa_football_team.t_1_down = t_1_down
    stats_ncaa_football_team.Russ_1_d = Russ_1_d
    stats_ncaa_football_team.pass_1_d = pass_1_d
    stats_ncaa_football_team.down_1_penal = down_1_penal
    stats_ncaa_football_team.down_3_eff = down_3_eff
    stats_ncaa_football_team.down_3_AVG = down_3_AVG
    stats_ncaa_football_team.down_4_eff = down_4_eff
    stats_ncaa_football_team.down_4_AVG = down_4_AVG
    stats_ncaa_football_team.comp_att = comp_att
    stats_ncaa_football_team.net_pass_y = net_pass_y
    stats_ncaa_football_team.y_p_pas_attps = y_p_pas_attps
    stats_ncaa_football_team.net_pass_y_pg = net_pass_y_pg
    stats_ncaa_football_team.pass_td = pass_td
    stats_ncaa_football_team.interceptions = interceptions
    stats_ncaa_football_team.sacks_y_lost = sacks_y_lost
    stats_ncaa_football_team.russ_attps = russ_attps
    stats_ncaa_football_team.russ_y = russ_y
    stats_ncaa_football_team.y_p_russ_attp = y_p_russ_attp
    stats_ncaa_football_team.russ_y_pg = russ_y_pg
    stats_ncaa_football_team.russ_td = russ_td
    stats_ncaa_football_team.total_of_plays = total_of_plays
    stats_ncaa_football_team.total_y = total_y
    stats_ncaa_football_team.y_pg = y_pg
    stats_ncaa_football_team.kickoffs_t = kickoffs_t
    stats_ncaa_football_team.AVG_kickoff_return_y = AVG_kickoff_return_y
    stats_ncaa_football_team.punt_t = punt_t
    stats_ncaa_football_team.AVG_punt_ruturn_y = AVG_punt_ruturn_y
    stats_ncaa_football_team.int_t = int_t
    stats_ncaa_football_team.AVG_intercept_y = AVG_intercept_y
    stats_ncaa_football_team.net_AVG_punt_y = net_AVG_punt_y
    stats_ncaa_football_team.punt_ty = punt_ty
    stats_ncaa_football_team.fg_goog_attps = fg_goog_attps
    stats_ncaa_football_team.touchback_percent = touchback_percent
    stats_ncaa_football_team.penal_ty = penal_ty
    stats_ncaa_football_team.penal_y_AVG_pg = penal_y_AVG_pg
    stats_ncaa_football_team.possesion_time = possesion_time
    stats_ncaa_football_team.fumbles_lost = fumbles_lost
    stats_ncaa_football_team.turnover_ratio = turnover_ratio

    db.session.commit()
    return jsonify({"msg": "stats_ncaa_football_team edith successfully"}), 200

@app.route('/stats_offensive_player_ncaa_football/<id>', methods=['PUT'])
def stats_offensive_player_ncaa_footballEdit(id):
    stats_offensive_player_ncaa_football = Stats_offensive_player_ncaa_football.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']

    Cmp = request.json['Cmp']
    pass_att = request.json['pass_att']
    cmp_AVG = request.json['cmp_AVG']
    yards = request.json['yards']
    yards_AVG = request.json['yards_AVG']
    yards_pg = request.json['yards_pg']
    pass_td = request.json['pass_td']
    Int = request.json['Int']
    asck = request.json['asck']
    syl = request.json['syl']
    rtg = request.json['rtg']
    russ_att = request.json['russ_att']
    russ_yards = request.json['russ_yards']
    yards_p_russ = request.json['yards_p_russ']
    big = request.json['big']
    rush_tt = request.json['rush_tt']
    rush_yard_pg = request.json['rush_yard_pg']
    fum = request.json['fum']
    lst = request.json['lst']
    long_pass = request.json['long_pass']
    fd = request.json['fd']
    rec = request.json['rec']
    r_tgts = request.json['r_tgts']
    r_yards = request.json['r_yards']
    yards_p_r = request.json['yards_p_r']
    r_td = request.json['r_td']
    lr = request.json['lr']
    r_big = request.json['r_big']
    r_ypg = request.json['r_ypg']
    r_fl = request.json['r_fl']
    r_yac = request.json['r_yac']
    r_fd = request.json['r_fd']
    pts = request.json['pts']

    stats_offensive_player_ncaa_football.name = name
    stats_offensive_player_ncaa_football.height = height
    stats_offensive_player_ncaa_football.weight = weight
    stats_offensive_player_ncaa_football.birth = birth
    stats_offensive_player_ncaa_football.position = position
    stats_offensive_player_ncaa_football.headshot = headshot
    stats_offensive_player_ncaa_football.dorsal = dorsal
    stats_offensive_player_ncaa_football.season = season
    stats_offensive_player_ncaa_football.team = team
    stats_offensive_player_ncaa_football.games = games
    stats_offensive_player_ncaa_football.Cmp = Cmp
    stats_offensive_player_ncaa_football.pass_att = pass_att
    stats_offensive_player_ncaa_football.cmp_AVG = cmp_AVG
    stats_offensive_player_ncaa_football.yards = yards
    stats_offensive_player_ncaa_football.yards_AVG = yards_AVG
    stats_offensive_player_ncaa_football.yards_pg = yards_pg
    stats_offensive_player_ncaa_football.pass_td = pass_td
    stats_offensive_player_ncaa_football.Int = Int
    stats_offensive_player_ncaa_football.asck = asck
    stats_offensive_player_ncaa_football.syl = syl
    stats_offensive_player_ncaa_football.rtg = rtg
    stats_offensive_player_ncaa_football.russ_att = russ_att
    stats_offensive_player_ncaa_football.russ_yards = russ_yards
    stats_offensive_player_ncaa_football.yards_p_russ = yards_p_russ
    stats_offensive_player_ncaa_football.big = big
    stats_offensive_player_ncaa_football.rush_tt = rush_tt
    stats_offensive_player_ncaa_football.rush_yard_pg = rush_yard_pg
    stats_offensive_player_ncaa_football.fum = fum
    stats_offensive_player_ncaa_football.lst = lst 
    stats_offensive_player_ncaa_football.long_pass = long_pass 
    stats_offensive_player_ncaa_football.fd = fd
    stats_offensive_player_ncaa_football.rec = rec
    stats_offensive_player_ncaa_football.r_tgts = r_tgts
    stats_offensive_player_ncaa_football.r_yards = r_yards
    stats_offensive_player_ncaa_football.yards_p_r = yards_p_r
    stats_offensive_player_ncaa_football.r_td = r_td
    stats_offensive_player_ncaa_football.lr = lr
    stats_offensive_player_ncaa_football.r_big = r_big
    stats_offensive_player_ncaa_football.r_ypg = r_ypg
    stats_offensive_player_ncaa_football.r_fl = r_fl
    stats_offensive_player_ncaa_football.r_yac = r_yac
    stats_offensive_player_ncaa_football.r_fd = r_fd
    stats_offensive_player_ncaa_football.pts = pts
    db.session.commit()
    return jsonify({"msg": "stats_offensive_player_ncaa_football edith successfully"}), 200

@app.route('/stats_defensive_player_ncca_football/<id>', methods=['PUT'])
def stats_defensive_player_ncca_footballEdit(id):
    stats_defensive_player_ncca_football = Stats_defensive_player_ncca_football.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    tack_solo = request.json['tack_solo']
    tack_ast = request.json['tack_ast']
    tack_total = request.json['tack_total']
    sacks = request.json['sacks']
    sacks_yards = request.json['sacks_yards']
    tfl = request.json['tfl']
    pd = request.json['pd']
    Int = request.json['Int']
    yds = request.json['yds']
    ing = request.json['ing']
    td = request.json['td']
    ff = request.json['ff']
    fr = request.json['fr']
    ftd = request.json['ftd']
    kb = request.json['kb']

    stats_defensive_player_ncca_football.name = name
    stats_defensive_player_ncca_football.height = height
    stats_defensive_player_ncca_football.weight = weight
    stats_defensive_player_ncca_football.birth = birth
    stats_defensive_player_ncca_football.position = position
    stats_offensive_player_ncaa_football.headshot = headshot
    stats_defensive_player_ncca_football.dorsal = dorsal
    stats_defensive_player_ncca_football.season = season
    stats_defensive_player_ncca_football.team = team
    stats_defensive_player_ncca_football.games = games
    stats_defensive_player_ncca_football.tack_solo = tack_solo
    stats_defensive_player_ncca_football.tack_ast = tack_ast
    stats_defensive_player_ncca_football.tack_total = tack_total
    stats_defensive_player_ncca_football.sacks = sacks
    stats_defensive_player_ncca_football.sacks_yards = sacks_yards
    stats_defensive_player_ncca_football.tfl = tfl
    stats_defensive_player_ncca_football.pd = pd
    stats_defensive_player_ncca_football.Int = Int
    stats_defensive_player_ncca_football.yds = yds
    stats_defensive_player_ncca_football.ing = ing
    stats_defensive_player_ncca_football.td = td
    stats_defensive_player_ncca_football.ff = ff
    stats_defensive_player_ncca_football.fr = fr
    stats_defensive_player_ncca_football.ftd = ftd
    stats_defensive_player_ncca_football.kb = kb
    db.session.commit()
    return jsonify({"msg": "stats_defensive_player_ncca_football edith successfully"}), 200

@app.route('/stats_returning_player_ncaa_football/<id>', methods=['PUT'])
def stats_returning_player_ncaa_footballEdit(id):
    stats_returning_player_ncaa_football = Stats_returning_player_ncaa_football.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    kick_returns = request.json['kick_returns']
    kick_returns_yards = request.json['kick_returns_yards']
    yards_p_k_p = request.json['yards_p_k_p']
    l_k_r = request.json['l_k_r']
    k_r_td = request.json['k_r_td']
    punt_r = request.json['punt_r']
    punt_r_y = request.json['punt_r_y']
    y_ppr = request.json['y_ppr']
    lpr = request.json['lpr']
    pr_td = request.json['pr_td']
    punt_r_fair_carches = request.json['punt_r_fair_carches']

    stats_returning_player_ncaa_football.name = name
    stats_returning_player_ncaa_football.height = height
    stats_returning_player_ncaa_football.weight = weight
    stats_returning_player_ncaa_football.birth = birth
    stats_returning_player_ncaa_football.position = position
    stats_offensive_player_ncaa_football.headshot = headshot
    stats_returning_player_ncaa_football.dorsal = dorsal
    stats_returning_player_ncaa_football.season = season
    stats_returning_player_ncaa_football.team = team
    stats_returning_player_ncaa_football.games = games
    stats_returning_player_ncaa_football.kick_returns = kick_returns
    stats_returning_player_ncaa_football.kick_returns_yards = kick_returns_yards
    stats_returning_player_ncaa_football.yards_p_k_p = yards_p_k_p
    stats_returning_player_ncaa_football.l_k_r = l_k_r
    stats_returning_player_ncaa_football.k_r_td = k_r_td
    stats_returning_player_ncaa_football.punt_r = punt_r
    stats_returning_player_ncaa_football.punt_r_y = punt_r_y
    stats_returning_player_ncaa_football.y_ppr = y_ppr
    stats_returning_player_ncaa_football.lpr = lpr
    stats_returning_player_ncaa_football.pr_td = pr_td
    stats_returning_player_ncaa_football.punt_r_fair_carches = punt_r_fair_carches
    db.session.commit()
    return jsonify({"msg": "stats_returning_player_ncaa_football edith successfully"}), 200

@app.route('/stats_kiking_player_ncaa_football/<id>', methods=['PUT'])
def stats_kiking_player_ncaa_footballEdit(id):
    stats_kiking_player_ncaa_football = Stats_kiking_player_ncaa_football.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    fgm = request.json['fgm']
    fga = request.json['fga']
    fg_AVG = request.json['fg_AVG']
    lng = request.json['lng']
    yars_f_goals_1_19 = request.json['yars_f_goals_1_19']
    yars_f_goals_20_29 = request.json['yars_f_goals_20_29']
    yars_f_goals_30_49 = request.json['yars_f_goals_30_49']
    yars_f_goals_40_49 = request.json['yars_f_goals_40_49']
    more_50 = request.json['more_50']
    xpm = request.json['xpm']
    xpa = request.json['xpa']
    xp_AVG = request.json['xp_AVG']

    stats_kiking_player_ncaa_football.name = name
    stats_kiking_player_ncaa_football.height = height
    stats_kiking_player_ncaa_football.weight = weight
    stats_kiking_player_ncaa_football.birth = birth
    stats_kiking_player_ncaa_football.position = position
    stats_kiking_player_ncaa_football.headshot = headshot
    stats_kiking_player_ncaa_football.dorsal = dorsal
    stats_kiking_player_ncaa_football.season = season
    stats_kiking_player_ncaa_football.team = team
    stats_kiking_player_ncaa_football.games = games
    stats_kiking_player_ncaa_football.fgm = fgm
    stats_kiking_player_ncaa_football.fga = fga
    stats_kiking_player_ncaa_football.fg_AVG = fg_AVG
    stats_kiking_player_ncaa_football.lng = lng
    stats_kiking_player_ncaa_football.yars_f_goals_1_19 = yars_f_goals_1_19
    stats_kiking_player_ncaa_football.yars_f_goals_20_29 = yars_f_goals_20_29
    stats_kiking_player_ncaa_football.yars_f_goals_30_49 = yars_f_goals_30_49
    stats_kiking_player_ncaa_football.yars_f_goals_40_49 = yars_f_goals_40_49
    stats_kiking_player_ncaa_football.more_50 = more_50
    stats_kiking_player_ncaa_football.xpm = xpm
    stats_kiking_player_ncaa_football.xpa = xpa
    stats_kiking_player_ncaa_football.xp_AVG = xp_AVG
    db.session.commit()
    return jsonify({"msg": "stats_kiking_player_ncaa_football edith successfully"}), 200

@app.route('/stats_punting_player_ncaa_football/<id>', methods=['PUT'])
def stats_punting_player_ncaa_footballEdit(id):
    stats_punting_player_ncaa_football = Stats_punting_player_ncaa_football.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    punts = request.json['punts']
    yards = request.json['yards']
    lng = request.json['lng']
    lng = request.json['lng']
    AVG = request.json['AVG']
    net = request.json['net']
    p_blk = request.json['p_blk']
    IN_20 = request.json['IN_20']
    tb = request.json['tb']
    fc = request.json['fc']
    att = request.json['att']
    punt_return_yds = request.json['punt_return_yds']
    AVG_punt_retun_yards = request.json['AVG_punt_retun_yards']

    stats_punting_player_ncaa_football.name = name
    stats_punting_player_ncaa_football.height = height
    stats_punting_player_ncaa_football.weight = weight
    stats_punting_player_ncaa_football.birth = birth
    stats_punting_player_ncaa_football.position = position
    stats_punting_player_ncaa_football.headshot = headshot
    stats_punting_player_ncaa_football.dorsal = dorsal
    stats_punting_player_ncaa_football.season = season
    stats_punting_player_ncaa_football.team = team
    stats_punting_player_ncaa_football.games = games
    stats_punting_player_ncaa_football.punts = punts
    stats_punting_player_ncaa_football.yards = yards
    stats_punting_player_ncaa_football.lng = lng
    stats_punting_player_ncaa_football.lng = lng
    stats_punting_player_ncaa_football.AVG = AVG
    stats_punting_player_ncaa_football.net = net
    stats_punting_player_ncaa_football.p_blk = p_blk
    stats_punting_player_ncaa_football.IN_20 = IN_20
    stats_punting_player_ncaa_football.tb = tb
    stats_punting_player_ncaa_football.fc = fc
    stats_punting_player_ncaa_football.att = att
    stats_punting_player_ncaa_football.punt_return_yds = punt_return_yds
    stats_punting_player_ncaa_football.AVG_punt_retun_yards = AVG_punt_retun_yards
    db.session.commit()
    return jsonify({"msg": "stats_punting_player_ncaa_football edith successfully"}), 200


@app.route('/nba/<id>', methods=['PUT'])
def nbaEdit(id):
    nba = Nba.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    # --
    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_total = request.json['first_half_total']
    fh_juice_total_over = request.json['fh_juice_total_over']
    fh_juice_total_under = request.json['fh_juice_total_under']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    # --
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_total = request.json['second_half_total']
    sh_juice_total_over = request.json['sh_juice_total_over']
    sh_juice_total_under = request.json['sh_juice_total_under']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    # --
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_under_away = request.json['q1_half_juice_under_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_juice_under_home = request.json['q1_half_juice_under_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']
    # --
    q2_half_spread_away = request.json['q2_half_spread_away']
    q2_half_spread_home = request.json['q2_half_spread_home']
    q2_half_juice_spread_away = request.json['q2_half_juice_spread_away']
    q2_half_juice_spread_home = request.json['q2_half_juice_spread_home']
    q2_half_moneyLineAway = request.json['q2_half_moneyLineAway']
    q2_half_moneyLineHome = request.json['q2_half_moneyLineHome']
    q2_half_total = request.json['q2_half_total']
    q2_juice_over = request.json['q2_juice_over']
    q2_juice_under = request.json['q2_juice_under']
    q2_half_tt_away = request.json['q2_half_tt_away']
    q2_half_juice_over_away = request.json['q2_half_juice_over_away']
    q2_half_juice_under_away = request.json['q2_half_juice_under_away']
    q2_half_tt_home = request.json['q2_half_tt_home']
    q2_half_juice_over_home = request.json['q2_half_juice_over_home']
    q2_half_juice_under_home = request.json['q2_half_juice_under_home']
    q2_half_final_score_away = request.json['q2_half_final_score_away']
    q2_half_final_score_home = request.json['q2_half_final_score_home']
    # --
    q3_half_spread_away = request.json['q3_half_spread_away']
    q3_half_spread_home = request.json['q3_half_spread_home']
    q3_half_juice_spread_away = request.json['q3_half_juice_spread_away']
    q3_half_juice_spread_home = request.json['q3_half_juice_spread_home']
    q3_half_moneyLineAway = request.json['q3_half_moneyLineAway']
    q3_half_moneyLineHome = request.json['q3_half_moneyLineHome']
    q3_half_total = request.json['q3_half_total']
    q3_juice_over = request.json['q3_juice_over']
    q3_juice_under = request.json['q3_juice_under']
    q3_half_tt_away = request.json['q3_half_tt_away']
    q3_half_juice_over_away = request.json['q3_half_juice_over_away']
    q3_half_juice_under_away = request.json['q3_half_juice_under_away']
    q3_half_tt_home = request.json['q3_half_tt_home']
    q3_half_juice_over_home = request.json['q3_half_juice_over_home']
    q3_half_juice_under_home = request.json['q3_half_juice_under_home']
    q3_half_final_score_away = request.json['q3_half_final_score_away']
    q3_half_final_score_home = request.json['q3_half_final_score_home']
    # --
    q4_half_spread_away = request.json['q4_half_spread_away']
    q4_half_spread_home = request.json['q4_half_spread_home']
    q4_half_juice_spread_away = request.json['q4_half_juice_spread_away']
    q4_half_juice_spread_home = request.json['q4_half_juice_spread_home']
    q4_half_moneyLineAway = request.json['q4_half_moneyLineAway']
    q4_half_moneyLineHome = request.json['q4_half_moneyLineHome']
    q4_half_total = request.json['q4_half_total']
    q4_juice_over = request.json['q4_juice_over']
    q4_juice_under = request.json['q4_juice_under']
    q4_half_tt_away = request.json['q4_half_tt_away']
    q4_half_juice_over_away = request.json['q4_half_juice_over_away']
    q4_half_juice_under_away = request.json['q4_half_juice_under_away']
    q4_half_tt_home = request.json['q4_half_tt_home']
    q4_half_juice_over_home = request.json['q4_half_juice_over_home']
    q4_half_juice_under_home = request.json['q4_half_juice_under_home']
    q4_half_final_score_away = request.json['q4_half_final_score_away']
    q4_half_final_score_home = request.json['q4_half_final_score_home']

    nba.date = date
    nba.hour = hour
    nba.week = week
    nba.status = status
    nba.casino = casino
    nba.rotation_away = rotation_away
    nba.rotation_home = rotation_home
    nba.away = away
    nba.home = home
    nba.spread_away = spread_away
    nba.spread_home = spread_home
    nba.juice_spread_away = juice_spread_away
    nba.juice_spread_home = juice_spread_home
    nba.moneyLineAway = moneyLineAway
    nba.moneyLineHome = moneyLineHome
    nba.total = total
    nba.juice_total_over = juice_total_over
    nba.juice_total_under = juice_total_under
    nba.tt_away = tt_away
    nba.juice_over_away = juice_over_away
    nba.juice_under_away = juice_under_away
    nba.tt_home = tt_home
    nba.juice_over_home = juice_over_home
    nba.juice_under_home = juice_under_home
    nba.final_score_away = final_score_away
    nba.final_score_home = final_score_home

    nba.first_half_spread_away = first_half_spread_away
    nba.first_half_spread_home = first_half_spread_home
    nba.first_half_juice_spread_away = first_half_juice_spread_away
    nba.first_half_juice_spread_home = first_half_juice_spread_home
    nba.first_half_moneyLineAway = first_half_moneyLineAway
    nba.first_half_moneyLineHome = first_half_moneyLineHome
    nba.first_half_total = first_half_total
    nba.fh_juice_total_over = fh_juice_total_over
    nba.fh_juice_total_under = fh_juice_total_under
    nba.first_half_tt_away = first_half_tt_away
    nba.first_half_juice_over_away = first_half_juice_over_away
    nba.first_half_juice_under_away = first_half_juice_under_away
    nba.first_half_tt_home = first_half_tt_home
    nba.first_half_juice_over_home = first_half_juice_over_home
    nba.first_half_juice_under_home = first_half_juice_under_home
    nba.first_half_final_score_away = first_half_final_score_away
    nba.first_half_final_score_home = first_half_final_score_home
    # --
    nba.second_half_spread_away = second_half_spread_away
    nba.second_half_spread_home = second_half_spread_home
    nba.second_half_juice_spread_away = second_half_juice_spread_away
    nba.second_half_juice_spread_home = second_half_juice_spread_home
    nba.second_half_moneyLineAway = second_half_moneyLineAway
    nba.second_half_moneyLineHome = second_half_moneyLineHome
    nba.second_half_total = second_half_total
    nba.sh_juice_total_over = sh_juice_total_over
    nba.sh_juice_total_under = sh_juice_total_under
    nba.second_half_tt_away = second_half_tt_away
    nba.second_half_juice_over_away = second_half_juice_over_away
    nba.second_half_juice_under_away = second_half_juice_under_away
    nba.second_half_tt_home = second_half_tt_home
    nba.second_half_juice_over_home = second_half_juice_over_home
    nba.second_half_juice_under_home = second_half_juice_under_home
    nba.second_half_final_score_away = second_half_final_score_away
    nba.second_half_final_score_home = second_half_final_score_home
    # --
    nba.q1_half_spread_away = q1_half_spread_away
    nba.q1_half_spread_home = q1_half_spread_home
    nba.q1_half_juice_spread_away = q1_half_juice_spread_away
    nba.q1_half_juice_spread_home = q1_half_juice_spread_home
    nba.q1_half_moneyLineAway = q1_half_moneyLineAway
    nba.q1_half_moneyLineHome = q1_half_moneyLineHome
    nba.q1_half_total = q1_half_total
    nba.q1_juice_over = q1_juice_over
    nba.q1_juice_under = q1_juice_under
    nba.q1_half_tt_away = q1_half_tt_away
    nba.q1_half_juice_over_away = q1_half_juice_over_away
    nba.q1_half_juice_under_away = q1_half_juice_under_away
    nba.q1_half_tt_home = q1_half_tt_home
    nba.q1_half_juice_over_home = q1_half_juice_over_home
    nba.q1_half_juice_under_home = q1_half_juice_under_home
    nba.q1_half_final_score_away = q1_half_final_score_away
    nba.q1_half_final_score_home = q1_half_final_score_home
    # --
    nba.q2_half_spread_away = q2_half_spread_away
    nba.q2_half_spread_home = q2_half_spread_home
    nba.q2_half_juice_spread_away = q2_half_juice_spread_away
    nba.q2_half_juice_spread_home = q2_half_juice_spread_home
    nba.q2_half_moneyLineAway = q2_half_moneyLineAway
    nba.q2_half_moneyLineHome = q2_half_moneyLineHome
    nba.q2_half_total = q2_half_total
    nba.q2_juice_over = q2_juice_over
    nba.q2_juice_under = q2_juice_under
    nba.q2_half_tt_away = q2_half_tt_away
    nba.q2_half_juice_over_away = q2_half_juice_over_away
    nba.q2_half_juice_under_away = q2_half_juice_under_away
    nba.q2_half_tt_home = q2_half_tt_home
    nba.q2_half_juice_over_home = q2_half_juice_over_home
    nba.q2_half_juice_under_home = q2_half_juice_under_home
    nba.q2_half_final_score_away = q2_half_final_score_away
    nba.q2_half_final_score_home = q2_half_final_score_home
    # --
    nba.q3_half_spread_away = q3_half_spread_away
    nba.q3_half_spread_home = q3_half_spread_home
    nba.q3_half_juice_spread_away = q3_half_juice_spread_away
    nba.q3_half_juice_spread_home = q3_half_juice_spread_home
    nba.q3_half_moneyLineAway = q3_half_moneyLineAway
    nba.q3_half_moneyLineHome = q3_half_moneyLineHome
    nba.q3_half_total = q3_half_total
    nba.q3_juice_over = q3_juice_over
    nba.q3_juice_under = q3_juice_under
    nba.q3_half_tt_away = q3_half_tt_away
    nba.q3_half_juice_over_away = q3_half_juice_over_away
    nba.q3_half_juice_under_away = q3_half_juice_under_away
    nba.q3_half_tt_home = q3_half_tt_home
    nba.q3_half_juice_over_home = q3_half_juice_over_home
    nba.q3_half_juice_under_home = q3_half_juice_under_home
    nba.q3_half_final_score_away = q3_half_final_score_away
    nba.q3_half_final_score_home = q3_half_final_score_home
    # --
    nba.q4_half_spread_away = q4_half_spread_away
    nba.q4_half_spread_home = q4_half_spread_home
    nba.q4_half_juice_spread_away = q4_half_juice_spread_away
    nba.q4_half_juice_spread_home = q4_half_juice_spread_home
    nba.q4_half_moneyLineAway = q4_half_moneyLineAway
    nba.q4_half_moneyLineHome = q4_half_moneyLineHome
    nba.q4_half_total = q4_half_total
    nba.q4_juice_over = q4_juice_over
    nba.q4_juice_under = q4_juice_under
    nba.q4_half_tt_away = q4_half_tt_away
    nba.q4_half_juice_over_away = q4_half_juice_over_away
    nba.q4_half_juice_under_away = q4_half_juice_under_away
    nba.q4_half_tt_home = q4_half_tt_home
    nba.q4_half_juice_over_home = q4_half_juice_over_home
    nba.q4_half_juice_under_home = q4_half_juice_under_home
    nba.q4_half_final_score_away = q4_half_final_score_away
    nba.q4_half_final_score_home = q4_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "nba edith successfully"}), 200


@app.route('/ncaa_basketball/<id>', methods=['PUT'])
def ncaa_basketballEdit(id):
    ncaa_basketball = Ncaa_Basketball.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    away = request.json['away']
    home = request.json['home']
    spread_away = request.json['spread_away']
    spread_home = request.json['spread_home']
    juice_spread_away = request.json['juice_spread_away']
    juice_spread_home = request.json['juice_spread_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    # --
    first_half_spread_away = request.json['first_half_spread_away']
    first_half_spread_home = request.json['first_half_spread_home']
    first_half_juice_spread_away = request.json['first_half_juice_spread_away']
    first_half_juice_spread_home = request.json['first_half_juice_spread_home']
    first_half_moneyLineAway = request.json['first_half_moneyLineAway']
    first_half_moneyLineHome = request.json['first_half_moneyLineHome']
    first_half_total = request.json['first_half_total']
    fh_juice_total_over = request.json['fh_juice_total_over']
    fh_juice_total_under = request.json['fh_juice_total_under']
    first_half_tt_away = request.json['first_half_tt_away']
    first_half_juice_over_away = request.json['first_half_juice_over_away']
    first_half_juice_under_away = request.json['first_half_juice_under_away']
    first_half_tt_home = request.json['first_half_tt_home']
    first_half_juice_over_home = request.json['first_half_juice_over_home']
    first_half_juice_under_home = request.json['first_half_juice_under_home']
    first_half_final_score_away = request.json['first_half_final_score_away']
    first_half_final_score_home = request.json['first_half_final_score_home']
    # --
    second_half_spread_away = request.json['second_half_spread_away']
    second_half_spread_home = request.json['second_half_spread_home']
    second_half_juice_spread_away = request.json['second_half_juice_spread_away']
    second_half_juice_spread_home = request.json['second_half_juice_spread_home']
    second_half_moneyLineAway = request.json['second_half_moneyLineAway']
    second_half_moneyLineHome = request.json['second_half_moneyLineHome']
    second_half_total = request.json['second_half_total']
    sh_juice_total_over = request.json['sh_juice_total_over']
    sh_juice_total_under = request.json['sh_juice_total_under']
    second_half_tt_away = request.json['second_half_tt_away']
    second_half_juice_over_away = request.json['second_half_juice_over_away']
    second_half_juice_under_away = request.json['second_half_juice_under_away']
    second_half_tt_home = request.json['second_half_tt_home']
    second_half_juice_over_home = request.json['second_half_juice_over_home']
    second_half_juice_under_home = request.json['second_half_juice_under_home']
    second_half_final_score_away = request.json['second_half_final_score_away']
    second_half_final_score_home = request.json['second_half_final_score_home']
    # --
    q1_half_spread_away = request.json['q1_half_spread_away']
    q1_half_spread_home = request.json['q1_half_spread_home']
    q1_half_juice_spread_away = request.json['q1_half_juice_spread_away']
    q1_half_juice_spread_home = request.json['q1_half_juice_spread_home']
    q1_half_moneyLineAway = request.json['q1_half_moneyLineAway']
    q1_half_moneyLineHome = request.json['q1_half_moneyLineHome']
    q1_half_total = request.json['q1_half_total']
    q1_juice_over = request.json['q1_juice_over']
    q1_juice_under = request.json['q1_juice_under']
    q1_half_tt_away = request.json['q1_half_tt_away']
    q1_half_juice_over_away = request.json['q1_half_juice_over_away']
    q1_half_juice_under_away = request.json['q1_half_juice_under_away']
    q1_half_tt_home = request.json['q1_half_tt_home']
    q1_half_juice_over_home = request.json['q1_half_juice_over_home']
    q1_half_juice_under_home = request.json['q1_half_juice_under_home']
    q1_half_final_score_away = request.json['q1_half_final_score_away']
    q1_half_final_score_home = request.json['q1_half_final_score_home']
    # --
    q2_half_spread_away = request.json['q2_half_spread_away']
    q2_half_spread_home = request.json['q2_half_spread_home']
    q2_half_juice_spread_away = request.json['q2_half_juice_spread_away']
    q2_half_juice_spread_home = request.json['q2_half_juice_spread_home']
    q2_half_moneyLineAway = request.json['q2_half_moneyLineAway']
    q2_half_moneyLineHome = request.json['q2_half_moneyLineHome']
    q2_half_total = request.json['q2_half_total']
    q2_juice_over = request.json['q2_juice_over']
    q2_juice_under = request.json['q2_juice_under']
    q2_half_tt_away = request.json['q2_half_tt_away']
    q2_half_juice_over_away = request.json['q2_half_juice_over_away']
    q2_half_juice_under_away = request.json['q2_half_juice_under_away']
    q2_half_tt_home = request.json['q2_half_tt_home']
    q2_half_juice_over_home = request.json['q2_half_juice_over_home']
    q2_half_juice_under_home = request.json['q2_half_juice_under_home']
    q2_half_final_score_away = request.json['q2_half_final_score_away']
    q2_half_final_score_home = request.json['q2_half_final_score_home']
    # --
    q3_half_spread_away = request.json['q3_half_spread_away']
    q3_half_spread_home = request.json['q3_half_spread_home']
    q3_half_juice_spread_away = request.json['q3_half_juice_spread_away']
    q3_half_juice_spread_home = request.json['q3_half_juice_spread_home']
    q3_half_moneyLineAway = request.json['q3_half_moneyLineAway']
    q3_half_moneyLineHome = request.json['q3_half_moneyLineHome']
    q3_half_total = request.json['q3_half_total']
    q3_juice_over = request.json['q3_juice_over']
    q3_juice_under = request.json['q3_juice_under']
    q3_half_tt_away = request.json['q3_half_tt_away']
    q3_half_juice_over_away = request.json['q3_half_juice_over_away']
    q3_half_juice_under_away = request.json['q3_half_juice_under_away']
    q3_half_tt_home = request.json['q3_half_tt_home']
    q3_half_juice_over_home = request.json['q3_half_juice_over_home']
    q3_half_juice_under_home = request.json['q3_half_juice_under_home']
    q3_half_final_score_away = request.json['q3_half_final_score_away']
    q3_half_final_score_home = request.json['q3_half_final_score_home']
    # --
    q4_half_spread_away = request.json['q4_half_spread_away']
    q4_half_spread_home = request.json['q4_half_spread_home']
    q4_half_juice_spread_away = request.json['q4_half_juice_spread_away']
    q4_half_juice_spread_home = request.json['q4_half_juice_spread_home']
    q4_half_moneyLineAway = request.json['q4_half_moneyLineAway']
    q4_half_moneyLineHome = request.json['q4_half_moneyLineHome']
    q4_half_total = request.json['q4_half_total']
    q4_juice_over = request.json['q4_juice_over']
    q4_juice_under = request.json['q4_juice_under']
    q4_half_tt_away = request.json['q4_half_tt_away']
    q4_half_juice_over_away = request.json['q4_half_juice_over_away']
    q4_half_juice_under_away = request.json['q4_half_juice_under_away']
    q4_half_tt_home = request.json['q4_half_tt_home']
    q4_half_juice_over_home = request.json['q4_half_juice_over_home']
    q4_half_juice_under_home = request.json['q4_half_juice_under_home']
    q4_half_final_score_away = request.json['q4_half_final_score_away']
    q4_half_final_score_home = request.json['q4_half_final_score_home']

    ncaa_basketball.date = date
    ncaa_basketball.hour = hour
    ncaa_basketball.week = week
    ncaa_basketball.status = status
    ncaa_basketball.casino = casino
    ncaa_basketball.rotation_away = rotation_away
    ncaa_basketball.rotation_home = rotation_home
    ncaa_basketball.away = away
    ncaa_basketball.home = home
    ncaa_basketball.spread_away = spread_away
    ncaa_basketball.spread_home = spread_home
    ncaa_basketball.juice_spread_away = juice_spread_away
    ncaa_basketball.juice_spread_home = juice_spread_home
    ncaa_basketball.moneyLineAway = moneyLineAway
    ncaa_basketball.moneyLineHome = moneyLineHome
    ncaa_basketball.total = total
    ncaa_basketball.juice_total_over = juice_total_over
    ncaa_basketball.juice_total_under = juice_total_under
    ncaa_basketball.tt_away = tt_away
    ncaa_basketball.juice_over_away = juice_over_away
    ncaa_basketball.juice_under_away = juice_under_away
    ncaa_basketball.tt_home = tt_home
    ncaa_basketball.juice_over_home = juice_over_home
    ncaa_basketball.juice_under_home = juice_under_home
    ncaa_basketball.final_score_away = final_score_away
    ncaa_basketball.final_score_home = final_score_home

    ncaa_basketball.first_half_spread_away = first_half_spread_away
    ncaa_basketball.first_half_spread_home = first_half_spread_home
    ncaa_basketball.first_half_juice_spread_away = first_half_juice_spread_away
    ncaa_basketball.first_half_juice_spread_home = first_half_juice_spread_home
    ncaa_basketball.first_half_moneyLineAway = first_half_moneyLineAway
    ncaa_basketball.first_half_moneyLineHome = first_half_moneyLineHome
    ncaa_basketball.first_half_total = first_half_total
    ncaa_basketball.fh_juice_total_over = fh_juice_total_over
    ncaa_basketball.fh_juice_total_under = fh_juice_total_under
    ncaa_basketball.first_half_tt_away = first_half_tt_away
    ncaa_basketball.first_half_juice_over_away = first_half_juice_over_away
    ncaa_basketball.first_half_juice_under_away = first_half_juice_under_away
    ncaa_basketball.first_half_tt_home = first_half_tt_home
    ncaa_basketball.first_half_juice_over_home = first_half_juice_over_home
    ncaa_basketball.first_half_juice_under_home = first_half_juice_under_home
    ncaa_basketball.first_half_final_score_away = first_half_final_score_away
    ncaa_basketball.first_half_final_score_home = first_half_final_score_home
    # --
    ncaa_basketball.second_half_spread_away = second_half_spread_away
    ncaa_basketball.second_half_spread_home = second_half_spread_home
    ncaa_basketball.second_half_juice_spread_away = second_half_juice_spread_away
    ncaa_basketball.second_half_juice_spread_home = second_half_juice_spread_home
    ncaa_basketball.second_half_moneyLineAway = second_half_moneyLineAway
    ncaa_basketball.second_half_moneyLineHome = second_half_moneyLineHome
    ncaa_basketball.second_half_total = second_half_total
    ncaa_basketball.sh_juice_total_over = sh_juice_total_over
    ncaa_basketball.sh_juice_total_under = sh_juice_total_under
    ncaa_basketball.second_half_tt_away = second_half_tt_away
    ncaa_basketball.second_half_juice_over_away = second_half_juice_over_away
    ncaa_basketball.second_half_juice_under_away = second_half_juice_under_away
    ncaa_basketball.second_half_tt_home = second_half_tt_home
    ncaa_basketball.second_half_juice_over_home = second_half_juice_over_home
    ncaa_basketball.second_half_juice_under_home = second_half_juice_under_home
    ncaa_basketball.second_half_final_score_away = second_half_final_score_away
    ncaa_basketball.second_half_final_score_home = second_half_final_score_home
    # --
    ncaa_basketball.q1_half_spread_away = q1_half_spread_away
    ncaa_basketball.q1_half_spread_home = q1_half_spread_home
    ncaa_basketball.q1_half_juice_spread_away = q1_half_juice_spread_away
    ncaa_basketball.q1_half_juice_spread_home = q1_half_juice_spread_home
    ncaa_basketball.q1_half_moneyLineAway = q1_half_moneyLineAway
    ncaa_basketball.q1_half_moneyLineHome = q1_half_moneyLineHome
    ncaa_basketball.q1_half_total = q1_half_total
    ncaa_basketball.q1_juice_over = q1_juice_over
    ncaa_basketball.q1_juice_under = q1_juice_under
    ncaa_basketball.q1_half_tt_away = q1_half_tt_away
    ncaa_basketball.q1_half_juice_over_away = q1_half_juice_over_away
    ncaa_basketball.q1_half_juice_under_away = q1_half_juice_under_away
    ncaa_basketball.q1_half_tt_home = q1_half_tt_home
    ncaa_basketball.q1_half_juice_over_home = q1_half_juice_over_home
    ncaa_basketball.q1_half_juice_under_home = q1_half_juice_under_home
    ncaa_basketball.q1_half_final_score_away = q1_half_final_score_away
    ncaa_basketball.q1_half_final_score_home = q1_half_final_score_home
    # --
    ncaa_basketball.q2_half_spread_away = q2_half_spread_away
    ncaa_basketball.q2_half_spread_home = q2_half_spread_home
    ncaa_basketball.q2_half_juice_spread_away = q2_half_juice_spread_away
    ncaa_basketball.q2_half_juice_spread_home = q2_half_juice_spread_home
    ncaa_basketball.q2_half_moneyLineAway = q2_half_moneyLineAway
    ncaa_basketball.q2_half_moneyLineHome = q2_half_moneyLineHome
    ncaa_basketball.q2_half_total = q2_half_total
    ncaa_basketball.q2_juice_over = q2_juice_over
    ncaa_basketball.q2_juice_under = q2_juice_under
    ncaa_basketball.q2_half_tt_away = q2_half_tt_away
    ncaa_basketball.q2_half_juice_over_away = q2_half_juice_over_away
    ncaa_basketball.q2_half_juice_under_away = q2_half_juice_under_away
    ncaa_basketball.q2_half_tt_home = q2_half_tt_home
    ncaa_basketball.q2_half_juice_over_home = q2_half_juice_over_home
    ncaa_basketball.q2_half_juice_under_home = q2_half_juice_under_home
    ncaa_basketball.q2_half_final_score_away = q2_half_final_score_away
    ncaa_basketball.q2_half_final_score_home = q2_half_final_score_home
    # --
    ncaa_basketball.q3_half_spread_away = q3_half_spread_away
    ncaa_basketball.q3_half_spread_home = q3_half_spread_home
    ncaa_basketball.q3_half_juice_spread_away = q3_half_juice_spread_away
    ncaa_basketball.q3_half_juice_spread_home = q3_half_juice_spread_home
    ncaa_basketball.q3_half_moneyLineAway = q3_half_moneyLineAway
    ncaa_basketball.q3_half_moneyLineHome = q3_half_moneyLineHome
    ncaa_basketball.q3_half_total = q3_half_total
    ncaa_basketball.q3_juice_over = q3_juice_over
    ncaa_basketball.q3_juice_under = q3_juice_under
    ncaa_basketball.q3_half_tt_away = q3_half_tt_away
    ncaa_basketball.q3_half_juice_over_away = q3_half_juice_over_away
    ncaa_basketball.q3_half_juice_under_away = q3_half_juice_under_away
    ncaa_basketball.q3_half_tt_home = q3_half_tt_home
    ncaa_basketball.q3_half_juice_over_home = q3_half_juice_over_home
    ncaa_basketball.q3_half_juice_under_home = q3_half_juice_under_home
    ncaa_basketball.q3_half_final_score_away = q3_half_final_score_away
    ncaa_basketball.q3_half_final_score_home = q3_half_final_score_home
    # --
    ncaa_basketball.q4_half_spread_away = q4_half_spread_away
    ncaa_basketball.q4_half_spread_home = q4_half_spread_home
    ncaa_basketball.q4_half_juice_spread_away = q4_half_juice_spread_away
    ncaa_basketball.q4_half_juice_spread_home = q4_half_juice_spread_home
    ncaa_basketball.q4_half_moneyLineAway = q4_half_moneyLineAway
    ncaa_basketball.q4_half_moneyLineHome = q4_half_moneyLineHome
    ncaa_basketball.q4_half_total = q4_half_total
    ncaa_basketball.q4_juice_over = q4_juice_over
    ncaa_basketball.q4_juice_under = q4_juice_under
    ncaa_basketball.q4_half_tt_away = q4_half_tt_away
    ncaa_basketball.q4_half_juice_over_away = q4_half_juice_over_away
    ncaa_basketball.q4_half_juice_under_away = q4_half_juice_under_away
    ncaa_basketball.q4_half_tt_home = q4_half_tt_home
    ncaa_basketball.q4_half_juice_over_home = q4_half_juice_over_home
    ncaa_basketball.q4_half_juice_under_home = q4_half_juice_under_home
    ncaa_basketball.q4_half_final_score_away = q4_half_final_score_away
    ncaa_basketball.q4_half_final_score_home = q4_half_final_score_home
    db.session.commit()
    return jsonify({"msg": "ncaa_basketball edith successfully"}), 200

@app.route('/stats_ncaa_basket_player/<id>', methods=['PUT'])
def stats_ncaa_basket_playerEdit(id):
    stats_ncaa_basket_player = Stats_ncaa_basket_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    college = request.json['college']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    minutes = request.json['minutes']
    position = request.json['position']
    headshot = request.json['headshot']
    gp = request.json['gp']
    gs = request.json['gs']
    fg = request.json['fg']
    fg_AVG = request.json['fg_AVG']
    three_pt = request.json['three_pt']
    three_pt_AVG = request.json['three_pt_AVG']
    ft = request.json['ft']
    ft_AVG = request.json['ft_AVG']
    Or = request.json['Or']
    dr = request.json['dr']
    reb = request.json['reb']
    ast = request.json['ast']
    stl = request.json['stl']
    blk = request.json['blk']
    to = request.json['to']
    pf = request.json['pf']
    pts = request.json['pts']

    stats_ncaa_basket_player.name = name
    stats_ncaa_basket_player.height = height
    stats_ncaa_basket_player.weight = weight
    stats_ncaa_basket_player.birth = birth
    stats_ncaa_basket_player.college = college
    stats_ncaa_basket_player.season = season
    stats_ncaa_basket_player.team = team
    stats_ncaa_basket_player.dorsal = dorsal
    stats_ncaa_basket_player.minutes = minutes
    stats_ncaa_basket_player.position = position
    stats_ncaa_basket_player.headshot = headshot
    stats_ncaa_basket_player.gp = gp
    stats_ncaa_basket_player.gs = gs
    stats_ncaa_basket_player.fg = fg
    stats_ncaa_basket_player.fg_AVG = fg_AVG
    stats_ncaa_basket_player.three_pt = three_pt
    stats_ncaa_basket_player.three_pt_AVG = three_pt_AVG
    stats_ncaa_basket_player.ft = ft
    stats_ncaa_basket_player.ft_AVG = ft_AVG
    stats_ncaa_basket_player.Or = Or
    stats_ncaa_basket_player.dr = dr
    stats_ncaa_basket_player.reb = reb
    stats_ncaa_basket_player.ast = ast
    stats_ncaa_basket_player.stl = stl
    stats_ncaa_basket_player.blk = blk
    stats_ncaa_basket_player.to = to
    stats_ncaa_basket_player.pf = pf
    stats_ncaa_basket_player.pts = pts

    db.session.commit()
    return jsonify({"msg": "stats_ncaa_basket_player edith successfully"}), 200

@app.route('/stats_ncaa_basket_team/<id>', methods=['PUT'])
def stats_ncaa_basket_teamEdit(id):
    stats_ncaa_basket_team = Stats_ncaa_basket_team.query.get(id)
    season = request.json['season']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']

    w = request.json['w']
    L = request.json['L']
    ptc = request.json['ptc']
    gb = request.json['gb']
    home = request.json['home']
    away = request.json['away']
    div = request.json['div']
    conf = request.json['conf']
    ppg = request.json['ppg']
    opp_ppg = request.json['opp_ppg']
    diff = request.json['diff']
    strk = request.json['strk']
    l10 = request.json['l10']

    stats_ncaa_basket_team.season = season
    stats_ncaa_basket_team.team = team
    stats_ncaa_basket_team.conference = conference
    stats_ncaa_basket_team.division = division
    stats_ncaa_basket_team.w = w
    stats_ncaa_basket_team.L = L
    stats_ncaa_basket_team.ptc = ptc
    stats_ncaa_basket_team.home = home
    stats_ncaa_basket_team.away = away
    stats_ncaa_basket_team.div = div
    stats_ncaa_basket_team.conf = conf
    stats_ncaa_basket_team.ppg = ppg
    stats_ncaa_basket_team.opp_ppg = opp_ppg
    stats_ncaa_basket_team.diff = diff
    stats_ncaa_basket_team.strk = strk
    stats_ncaa_basket_team.l10 = l10

    db.session.commit()
    return jsonify({"msg": "stats_ncaa_basket_team edith successfully"}), 200

@app.route('/nhl/<id>', methods=['PUT'])
def nhlEdit(id):
    nhl = Nhl.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    casino = request.json['casino']
    away = request.json['away']
    home = request.json['home']
    puck_line_away = request.json['puck_line_away']
    puck_line_home = request.json['puck_line_home']
    juice_puck_away = request.json['juice_puck_away']
    juice_puck_home = request.json['juice_puck_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']

    puck_away_1Q = request.json['puck_away_1Q']
    puck_home_1Q = request.json['puck_home_1Q']
    juice_puck_away_1Q = request.json['juice_puck_away_1Q']
    juice_puck_home_1Q = request.json['juice_puck_home_1Q']
    moneyLineAway_1Q = request.json['moneyLineAway_1Q']
    moneyLineHome_1Q = request.json['moneyLineHome_1Q']
    total_1Q = request.json['total_1Q']
    Q1_juice_over = request.json['Q1_juice_over']
    Q1_juice_under = request.json['Q1_juice_under']
    tt_away_1Q = request.json['tt_away_1Q']
    juice_over_away_1Q = request.json['juice_over_away_1Q']
    juice_under_away_1Q = request.json['juice_under_away_1Q']
    tt_home_1Q = request.json['tt_home_1Q']
    juice_over_home_1Q = request.json['juice_over_home_1Q']
    juice_under_home_1Q = request.json['juice_under_home_1Q']
    sa_1Q = request.json['sa_1Q']
    sh_1Q = request.json['sh_1Q']
    sa_2Q = request.json['sa_2Q']
    sh_2Q = request.json['sh_2Q']
    sa_3Q = request.json['sa_3Q']
    sh_3Q = request.json['sh_3Q']

    nhl.date = date
    nhl.hour = hour
    nhl.status = status
    nhl.rotation_away = rotation_away
    nhl.rotation_home = rotation_home
    nhl.casino = casino
    nhl.away = away
    nhl.home = home

    nhl.puck_line_away = puck_line_away
    nhl.puck_line_home = puck_line_home
    nhl.juice_puck_away = juice_puck_away
    nhl.juice_puck_home = juice_puck_home
    nhl.moneyLineAway = moneyLineAway
    nhl.moneyLineHome = moneyLineHome
    nhl.total = total
    nhl.juice_total_over = juice_total_over
    nhl.juice_total_under = juice_total_under
    nhl.tt_away = tt_away
    nhl.juice_over_away = juice_over_away
    nhl.juice_under_away = juice_under_away
    nhl.tt_home = tt_home
    nhl.juice_over_home = juice_over_home
    nhl.juice_under_home = juice_under_home
    nhl.final_score_away = final_score_away
    nhl.final_score_home = final_score_home
    nhl.final_score_home = final_score_home
    nhl.puck_away_1Q = puck_away_1Q
    nhl.puck_home_1Q = puck_home_1Q
    nhl.moneyLineAway_1Q = moneyLineAway_1Q
    nhl.moneyLineHome_1Q = moneyLineHome_1Q
    nhl.total_1Q = total_1Q
    nhl.Q1_juice_over = Q1_juice_over
    nhl.Q1_juice_under = Q1_juice_under
    nhl.tt_away_1Q = tt_away_1Q
    nhl.juice_over_away_1Q = juice_over_away_1Q
    nhl.juice_under_away_1Q = juice_under_away_1Q
    nhl.tt_home_1Q = tt_home_1Q
    nhl.juice_over_home_1Q = juice_over_home_1Q
    nhl.juice_under_home_1Q = juice_under_home_1Q
    nhl.sa_1Q = sa_1Q
    nhl.sh_1Q = sh_1Q
    nhl.sa_2Q = sa_2Q
    nhl.sh_2Q = sh_2Q
    nhl.sa_3Q = sa_3Q
    nhl.sh_3Q = sh_3Q
    db.session.commit()
    return jsonify({"msg": "nhl edith successfully"}), 200


@app.route('/boxeo/<id>', methods=['PUT'])
def boxeoEdit(id):
    boxeo = Boxeo.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_number = request.json['rotation_number']
    event = request.json['event']
    rounds = request.json['rounds']
    location_Fight = request.json['location_Fight']
    fighter_One = request.json['fighter_One']
    money_Line_One = request.json['money_Line_One']
    fighter_Two = request.json['fighter_Two']
    money_Line_Two = request.json['money_Line_Two']
    winner = request.json['winner']
    finish_by = request.json['finish_by']
    r1_result = request.json['r1_result']
    r2_result = request.json['r2_result']
    r3_result = request.json['r3_result']
    r4_result = request.json['r4_result']
    r5_result = request.json['r5_result']
    r6_result = request.json['r6_result']
    r7_result = request.json['r7_result']
    r8_result = request.json['r8_result']
    r9_result = request.json['r9_result']
    r10_result = request.json['r10_result']
    r11_result = request.json['r11_result']
    r12_result = request.json['r12_result']
    r13_result = request.json['r13_result']
    r14_result = request.json['r14_result']
    r15_result = request.json['r15_result']

    boxeo.date = date
    boxeo.hour = hour
    boxeo.week = week
    boxeo.status = status
    boxeo.casino = casino 
    boxeo.rotation_number = rotation_number 
    boxeo.event = event
    boxeo.rounds = rounds
    boxeo.location_Fight = location_Fight
    boxeo.fighter_One = fighter_One
    boxeo.money_Line_One = money_Line_One
    boxeo.fighter_Two = fighter_Two
    boxeo.money_Line_Two = money_Line_Two
    boxeo.winner = winner
    boxeo.finish_by = finish_by
    boxeo.r1_result = r1_result
    boxeo.r2_result = r2_result
    boxeo.r3_result = r3_result
    boxeo.r4_result = r4_result
    boxeo.r5_result = r5_result
    boxeo.r6_result = r6_result
    boxeo.r7_result = r7_result
    boxeo.r8_result = r8_result
    boxeo.r9_result = r9_result
    boxeo.r10_result = r10_result
    boxeo.r11_result = r11_result
    boxeo.r12_result = r12_result
    boxeo.r13_result = r13_result
    boxeo.r14_result = r14_result
    boxeo.r15_result = r15_result

    db.session.commit()
    return jsonify({"msg": "boxeo edith successfully"}), 200


@app.route('/mma/<id>', methods=['PUT'])
def mmaEdit(id):
    mma = Mma.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_number = request.json['rotation_number']
    event = request.json['event']
    rounds = request.json['rounds']
    location_Fight = request.json['location_Fight']
    fighter_One = request.json['fighter_One']
    money_Line_One = request.json['money_Line_One']
    fighter_Two = request.json['fighter_Two']
    money_Line_Two = request.json['money_Line_Two']
    winner = request.json['winner']
    finish_by = request.json['finish_by']
    r1_result = request.json['r1_result']
    r2_result = request.json['r2_result']
    r3_result = request.json['r3_result']
    r4_result = request.json['r4_result']
    r5_result = request.json['r5_result']
    r6_result = request.json['r6_result']
    r7_result = request.json['r7_result']
    r8_result = request.json['r8_result']
    r9_result = request.json['r9_result']
    r10_result = request.json['r10_result']
    r11_result = request.json['r11_result']
    r12_result = request.json['r12_result']
    r13_result = request.json['r13_result']
    r14_result = request.json['r14_result']
    r15_result = request.json['r15_result']

    mma.date = date
    mma.hour = hour
    mma.week = week
    mma.status = status
    mma.casino = casino 
    mma.rotation_number = rotation_number
    mma.event = event
    mma.rounds = rounds
    mma.location_Fight = location_Fight
    mma.fighter_One = fighter_One
    mma.money_Line_One = money_Line_One
    mma.fighter_Two = fighter_Two
    mma.money_Line_Two = money_Line_Two
    mma.winner = winner
    mma.finish_by = finish_by
    mma.r1_result = r1_result
    mma.r2_result = r2_result
    mma.r3_result = r3_result
    mma.r4_result = r4_result
    mma.r5_result = r5_result
    mma.r6_result = r6_result
    mma.r7_result = r7_result
    mma.r8_result = r8_result
    mma.r9_result = r9_result
    mma.r10_result = r10_result
    mma.r11_result = r11_result
    mma.r12_result = r12_result
    mma.r13_result = r13_result
    mma.r14_result = r14_result
    mma.r15_result = r15_result

    db.session.commit()
    return jsonify({"msg": "mma edith successfully"}), 200


@app.route('/nascar/<id>', methods=['PUT'])
def nascarEdit(id):
    nascar = Nascar.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_number = request.json['rotation_number']
    race = request.json['race']
    event = request.json['event']
    track = request.json['track']
    location = request.json['location']
    place1 = request.json['place1']
    place2 = request.json['place2']
    place3 = request.json['place3']

    nascar.date = date
    nascar.hour = hour
    nascar.week = week
    nascar.status = status
    nascar.casino = casino 
    nascar.rotation_number = rotation_number
    nascar.race = race
    nascar.event = event
    nascar.track = track
    nascar.location = location
    nascar.place1 = place1
    nascar.place2 = place2
    nascar.place3 = place3

    db.session.commit()
    return jsonify({"msg": "nascar edith successfully"}), 200

@app.route('/nascar_drivers/<id>', methods=['PUT'])
def nascar_driversEdit(id):
    nascar_drivers = Nascar_drivers.query.get(id)
    name = request.json['name']
    country = request.json['country']
    birth = request.json['birth']
    headshot = request.json['headshot']
    sponsor = request.json['sponsor']
    engine = request.json['engine']
    number_car = request.json['number_car']
    rank = request.json['rank']
    starts = request.json['starts']
    poles = request.json['poles']
    top5 = request.json['top5']
    top10 = request.json['top10']
    laps_lead = request.json['laps_lead']
    pts = request.json['pts']
    AVG_laps = request.json['AVG_laps']
    AVG_finish = request.json['AVG_finish']

    nascar_drivers.name = name
    nascar_drivers.country = country
    nascar_drivers.birth = birth
    nascar_drivers.headshot = headshot
    nascar_drivers.sponsor = sponsor
    nascar_drivers.engine = engine
    nascar_drivers.number_car = number_car
    nascar_drivers.rank = rank
    nascar_drivers.starts = starts
    nascar_drivers.poles = poles
    nascar_drivers.top5 = top5
    nascar_drivers.top10 = top10
    nascar_drivers.laps_lead = laps_lead
    nascar_drivers.pts = pts
    nascar_drivers.AVG_laps = AVG_laps
    nascar_drivers.AVG_finish = AVG_finish

    db.session.commit()
    return jsonify({"msg": "nascar_drivers edith successfully"}), 200

@app.route('/moto_gp_drivers/<id>', methods=['PUT'])
def moto_gp_driversEdit(id):
    moto_gp_drivers = Moto_gp_drivers.query.get(id)
    name = request.json['name']
    country = request.json['country']
    birth = request.json['birth']
    headshot = request.json['headshot']
    sponsor = request.json['sponsor']
    engine = request.json['engine']
    number_car = request.json['number_car']
    rank = request.json['rank']
    starts = request.json['starts']
    poles = request.json['poles']
    top5 = request.json['top5']
    top10 = request.json['top10']
    laps_lead = request.json['laps_lead']
    pts = request.json['pts']
    AVG_laps = request.json['AVG_laps']
    AVG_finish = request.json['AVG_finish']

    moto_gp_drivers.name = name
    moto_gp_drivers.country = country
    moto_gp_drivers.birth = birth
    moto_gp_drivers.headshot = headshot
    moto_gp_drivers.sponsor = sponsor
    moto_gp_drivers.engine = engine
    moto_gp_drivers.number_car = number_car
    moto_gp_drivers.rank = rank
    moto_gp_drivers.starts = starts
    moto_gp_drivers.poles = poles
    moto_gp_drivers.top5 = top5
    moto_gp_drivers.top10 = top10
    moto_gp_drivers.laps_lead = laps_lead
    moto_gp_drivers.pts = pts
    moto_gp_drivers.AVG_laps = AVG_laps
    moto_gp_drivers.AVG_finish = AVG_finish

    db.session.commit()
    return jsonify({"msg": "moto_gp_drivers edith successfully"}), 200

@app.route('/moto_gp/<id>', methods=['PUT'])
def moto_gpEdit(id):
    moto_gp = Moto_GP.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_number = request.json['rotation_number']
    race = request.json['race']
    track = request.json['track']
    location = request.json['location']
    place1 = request.json['place1']
    place2 = request.json['place2']
    place3 = request.json['place3']

    moto_gp.date = date
    moto_gp.hour = hour
    moto_gp.week = week
    moto_gp.status = status
    moto_gp.casino = casino 
    moto_gp.rotation_number = rotation_number 
    moto_gp.race = race
    moto_gp.track = track
    moto_gp.location = location
    moto_gp.place1 = place1
    moto_gp.place2 = place2
    moto_gp.place3 = place3

    db.session.commit()
    return jsonify({"msg": "moto_gp edith successfully"}), 200


@app.route('/match_ups_nascar/<id>', methods=['PUT'])
def match_ups_nascarEdit(id):
    match_ups_nascar = Match_Ups_Nacar.query.get(id)
    name1 = request.json['name1']
    mu1 = request.json['mu1']
    name2 = request.json['name2']
    mu2 = request.json['mu2']
    match_ups_nascar.name1 = name1
    match_ups_nascar.mu1 = mu1
    match_ups_nascar.name2 = name2
    match_ups_nascar.mu2 = mu2

    db.session.commit()
    return jsonify({"msg": "match_ups_nascar edith successfully"}), 200


@app.route('/golf/<id>', methods=['PUT'])
def golfEdit(id):
    golf = Golf.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    week = request.json['week']
    status = request.json['status']
    casino = request.json['casino']
    rotation_number = request.json['rotation_number']
    event = request.json['event']
    location = request.json['location']
    place1 = request.json['place1']
    place2 = request.json['place2']
    place3 = request.json['place3']

    golf.date = date
    golf.hour = hour
    golf.week = week
    golf.status = status
    golf.casino = casino 
    golf.rotation_number = rotation_number 
    golf.event = event
    golf.location = location
    golf.place1 = place1
    golf.place2 = place2
    golf.place3 = place3

    db.session.commit()
    return jsonify({"msg": "golf edith successfully"}), 200


@app.route('/golfer/<id>', methods=['PUT'])
def golferEdit(id):
    golfer = Golfer.query.get(id)
    country = request.json['country']
    season = request.json['season']
    swing = request.json['swing']
    birth = request.json['birth']
    cuts = request.json['cuts']
    top10 = request.json['top10']
    w = request.json['w']
    rnds = request.json['rnds']
    holes = request.json['holes']
    avg = request.json['avg']

    golfer.country = country
    golfer.season = season
    golfer.swing = swing
    golfer.birth = birth
    golfer.cuts = cuts
    golfer.top10 = top10
    golfer.w = w
    golfer.rnds = rnds
    golfer.holes = holes
    golfer.avg = avg

    db.session.commit()
    return jsonify({"msg": "golfer edith successfully"}), 200


@app.route('/soccer/<id>', methods=['PUT'])
def soccerEdit(id):
    soccer = Soccer.query.get(id)
    date = request.json['date']
    hour = request.json['hour']
    status = request.json['status']
    casino = request.json['casino']
    country = request.json['country']
    tournament = request.json['tournament']
    away = request.json['away']
    home = request.json['home']
    rotation_away = request.json['rotation_away']
    rotation_home = request.json['rotation_home']
    goal_line_away = request.json['goal_line_away']
    goal_line_home = request.json['goal_line_home']
    juice_goal_away = request.json['juice_goal_away']
    juice_goal_home = request.json['juice_goal_home']
    moneyLineAway = request.json['moneyLineAway']
    moneyLineHome = request.json['moneyLineHome']
    total = request.json['total']
    juice_total_over = request.json['juice_total_over']
    juice_total_under = request.json['juice_total_under']
    tt_away = request.json['tt_away']
    juice_over_away = request.json['juice_over_away']
    juice_under_away = request.json['juice_under_away']
    tt_home = request.json['tt_home']
    juice_over_home = request.json['juice_over_home']
    juice_under_home = request.json['juice_under_home']
    final_score_away = request.json['final_score_away']
    final_score_home = request.json['final_score_home']
    goal_away_1H = request.json['goal_away_1H']
    goal_home_1H = request.json['goal_home_1H']
    juice_goal_away_1H = request.json['juice_goal_away_1H']
    juice_goal_home_1H = request.json['juice_goal_home_1H']
    moneyLineAway_1H = request.json['moneyLineAway_1H']
    moneyLineHome_1H = request.json['moneyLineHome_1H']
    total_1H = request.json['total_1H']
    H1_juice_over = request.json['H1_juice_over']
    H1_juice_under = request.json['H1_juice_under']
    tt_away_1H = request.json['tt_away_1H']
    juice_over_away_1H = request.json['juice_over_away_1H']
    juice_under_away_1H = request.json['juice_under_away_1H']
    tt_home_1H = request.json['tt_home_1H']
    juice_over_home_1H = request.json['juice_over_home_1H']
    juice_under_home_1H = request.json['juice_under_home_1H']

    soccer.date = date
    soccer.hour = hour
    soccer.status = status
    soccer.casino = casino
    soccer.country = country
    soccer.tournament = tournament
    soccer.away = away
    soccer.home = home
    soccer.rotation_away = rotation_away
    soccer.rotation_home = rotation_home
    soccer.goal_line_away = goal_line_away
    soccer.goal_line_home = goal_line_home
    soccer.juice_goal_away = juice_goal_away
    soccer.juice_goal_home = juice_goal_home
    soccer.moneyLineAway = moneyLineAway
    soccer.moneyLineHome = moneyLineHome
    soccer.total = total
    soccer.juice_total_over = juice_total_over
    soccer.juice_total_under = juice_total_under
    soccer.tt_away = tt_away
    soccer.juice_over_away = juice_over_away
    soccer.juice_under_away = juice_under_away
    soccer.tt_home = tt_home
    soccer.juice_over_home = juice_over_home
    soccer.juice_under_home = juice_under_home
    soccer.final_score_away = final_score_away
    soccer.final_score_home = final_score_home
    soccer.final_score_home = final_score_home
    soccer.goal_away_1H = goal_away_1H
    soccer.goal_home_1H = goal_home_1H
    soccer.juice_goal_away_1H = juice_goal_away_1H
    soccer.juice_goal_home_1H = juice_goal_home_1H
    soccer.moneyLineAway_1H = moneyLineAway_1H
    soccer.moneyLineHome_1H = moneyLineHome_1H
    soccer.total_1H = total_1H
    soccer.H1_juice_over = H1_juice_over
    soccer.H1_juice_under = H1_juice_under
    soccer.tt_away_1H = tt_away_1H
    soccer.juice_over_away_1H = juice_over_away_1H
    soccer.juice_under_away_1H = juice_under_away_1H
    soccer.tt_home_1H = tt_home_1H
    soccer.juice_over_home_1H = juice_over_home_1H
    soccer.juice_under_home_1H = juice_under_home_1H

    db.session.commit()
    return jsonify({"msg": "soccer edith successfully"}), 200

@app.route('/stats_soccer_team/<id>', methods=['PUT'])
def stats_soccer_teamEdit(id):
    stats_soccer_team = Stats_Soccer_Team.query.get(id)
    season = request.json['season']
    name = request.json['name']
    league = request.json['league']
    position = request.json['position']
    matches = request.json['matches']
    win = request.json['win']
    loss = request.json['loss']
    pts = request.json['pts']
    goals_for = request.json['goals_for']
    goals_against = request.json['goals_against']
    more_2_5_goals = request.json['more_2_5_goals']
    less_2_5_goals = request.json['less_2_5_goals']
    zero_goal_against = request.json['zero_goal_against']
    zero_goals_for = request.json['zero_goals_for']
    ties = request.json['ties']

    stats_soccer_team.season = season
    stats_soccer_team.name = name
    stats_soccer_team.league = league
    stats_soccer_team.position = position
    stats_soccer_team.matches = matches
    stats_soccer_team.win = win
    stats_soccer_team.loss = loss
    stats_soccer_team.pts = pts
    stats_soccer_team.goals_for = goals_for
    stats_soccer_team.goals_against = goals_against
    stats_soccer_team.more_2_5_goals = more_2_5_goals
    stats_soccer_team.less_2_5_goals = less_2_5_goals
    stats_soccer_team.zero_goal_against = zero_goal_against
    stats_soccer_team.zero_goals_for = zero_goals_for
    stats_soccer_team.ties = ties
    db.session.commit()
    return jsonify({"msg": "stats_soccer_team edith successfully"}), 200

@app.route('/stats_soccer_player/<id>', methods=['PUT'])
def stats_soccer_playerEdit(id):
    stats_soccer_player = Stats_Soccer_Player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    season = request.json['season']
    dorsal = request.json['dorsal']
    team = request.json['team']

    games = request.json['games']
    strt = request.json['strt']
    fc = request.json['fc']
    fa = request.json['fa']
    yc = request.json['yc']
    rc = request.json['rc']
    goals = request.json['goals']
    ast = request.json['ast']
    sh = request.json['sh']
    st = request.json['st']
    off = request.json['off']

    stats_soccer_player.name = name
    stats_soccer_player.height = height
    stats_soccer_player.weight = weight
    stats_soccer_player.birth = birth
    stats_soccer_player.position = position
    stats_soccer_player.headshot = headshot
    stats_soccer_player.season = season
    stats_soccer_player.dorsal = dorsal
    stats_soccer_player.team = team
    stats_soccer_player.games = games
    stats_soccer_player.strt = strt
    stats_soccer_player.fc = fc
    stats_soccer_player.fa = fa
    stats_soccer_player.yc = yc
    stats_soccer_player.rc = rc
    stats_soccer_player.goals = goals
    stats_soccer_player.ast = ast
    stats_soccer_player.sh = sh
    stats_soccer_player.st = st
    stats_soccer_player.off = off

    db.session.commit()
    return jsonify({"msg": "Stats_Soccer_Player edith successfully"}), 200

@app.route('/stats_nba_team/<id>', methods=['PUT'])
def stats_nba_teamEdit(id):
    stats_nba_team = Stats_nba_team.query.get(id)
    season = request.json['season']
    season_type = request.json['season_type']
    group_type_comparation = request.json['group_type_comparation']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']

    w = request.json['w']
    L = request.json['L']
    ptc = request.json['ptc']
    gb = request.json['gb']
    home = request.json['home']
    away = request.json['away']
    div = request.json['div']
    conf = request.json['conf']
    ppg = request.json['ppg']
    opp_ppg = request.json['opp_ppg']
    diff = request.json['diff']
    strk = request.json['strk']
    l10 = request.json['l10']

    stats_nba_team.season = season
    stats_nba_team.season_type = season_type
    stats_nba_team.group_type_comparation = group_type_comparation
    stats_nba_team.team = team
    stats_nba_team.conference = conference
    stats_nba_team.division = division
    stats_nba_team.w = w
    stats_nba_team.L = L
    stats_nba_team.ptc = ptc
    stats_nba_team.gb = gb
    stats_nba_team.home = home
    stats_nba_team.away = away
    stats_nba_team.div = div
    stats_nba_team.conf = conf
    stats_nba_team.ppg = ppg
    stats_nba_team.opp_ppg = opp_ppg
    stats_nba_team.diff = diff
    stats_nba_team.strk = strk
    stats_nba_team.l10 = l10

    db.session.commit()
    return jsonify({"msg": "stats_nba_team edith successfully"}), 200


@app.route('/stats_nba_player/<id>', methods=['PUT'])
def stats_nba_playerEdit(id):
    stats_nba_player = Stats_nba_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    college = request.json['college']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    minutes = request.json['minutes']
    position = request.json['position']
    headshot = request.json['headshot']
    gp = request.json['gp']
    gs = request.json['gs']
    fg = request.json['fg']
    fg_AVG = request.json['fg_AVG']
    three_pt = request.json['three_pt']
    three_pt_AVG = request.json['three_pt_AVG']
    ft = request.json['ft']
    ft_AVG = request.json['ft_AVG']
    Or = request.json['Or']
    dr = request.json['dr']
    reb = request.json['reb']
    ast = request.json['ast']
    stl = request.json['stl']
    blk = request.json['blk']
    to = request.json['to']
    pf = request.json['pf']
    pts = request.json['pts']

    stats_nba_player.name = name
    stats_nba_player.height = height
    stats_nba_player.weight = weight
    stats_nba_player.birth = birth
    stats_nba_player.college = college
    stats_nba_player.season = season
    stats_nba_player.team = team
    stats_nba_player.dorsal = dorsal
    stats_nba_player.minutes = minutes
    stats_nba_player.position = position
    stats_nba_player.headshot = headshot
    stats_nba_player.gp = gp
    stats_nba_player.gs = gs
    stats_nba_player.fg = fg
    stats_nba_player.fg_AVG = fg_AVG
    stats_nba_player.three_pt = three_pt
    stats_nba_player.three_pt_AVG = three_pt_AVG
    stats_nba_player.ft = ft
    stats_nba_player.ft_AVG = ft_AVG
    stats_nba_player.Or = Or
    stats_nba_player.dr = dr
    stats_nba_player.reb = reb
    stats_nba_player.ast = ast
    stats_nba_player.stl = stl
    stats_nba_player.blk = blk
    stats_nba_player.to = to
    stats_nba_player.pf = pf
    stats_nba_player.pts = pts

    db.session.commit()
    return jsonify({"msg": "stats_nba_player edith successfully"}), 200


@app.route('/stats_mlb_team/<id>', methods=['PUT'])
def stats_mlb_teamEdit(id):
    stats_mlb_team = Stats_mlb_team.query.get(id)
    season = request.json['season']
    season_type = request.json['season_type']
    group_type_comparation = request.json['group_type_comparation']
    team = request.json['team']
    league = request.json['league']
    division = request.json['division']
    w = request.json['w']
    L = request.json['L']
    pct = request.json['pct']
    gb = request.json['gb']
    home = request.json['home']
    away = request.json['away']
    rs = request.json['rs']
    ra = request.json['ra']
    diff = request.json['diff']
    strk = request.json['strk']
    L10 = request.json['L10']

    stats_mlb_team.season = season
    stats_mlb_team.season_type = season_type
    stats_mlb_team.group_type_comparation = group_type_comparation
    stats_mlb_team.team = team
    stats_mlb_team.league = league
    stats_mlb_team.division = division
    stats_mlb_team.w = w
    stats_mlb_team.L = L
    stats_mlb_team.pct = pct
    stats_mlb_team.gb = gb
    stats_mlb_team.home = home
    stats_mlb_team.away = away
    stats_mlb_team.rs = rs
    stats_mlb_team.ra = ra
    stats_mlb_team.diff = diff
    stats_mlb_team.strk = strk
    stats_mlb_team.L10 = L10

    db.session.commit()
    return jsonify({"msg": "stats_mlb_team edith successfully"}), 200


@app.route('/stats_mlb_player/<id>', methods=['PUT'])
def stats_mlb_playerEdit(id):
    stats_mlb_player = Stats_mlb_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    position = request.json['position']
    headshot = request.json['headshot']
    gp = request.json['gp']
    ab = request.json['ab']
    r = request.json['r']
    h = request.json['h']
    two_b = request.json['two_b']
    three_b = request.json['three_b']
    hb = request.json['hb']
    rbi = request.json['rbi']
    tb = request.json['tb']
    bb = request.json['bb']
    so = request.json['so']
    sb = request.json['sb']
    avg = request.json['avg']
    obp = request.json['obp']
    slg = request.json['slg']
    ops = request.json['ops']
    war = request.json['war']

    stats_mlb_player.name = name
    stats_mlb_player.height = height
    stats_mlb_player.weight = weight
    stats_mlb_player.birth = birth
    stats_mlb_player.season = season
    stats_mlb_player.team = team
    stats_mlb_player.dorsal = dorsal
    stats_mlb_player.position = position
    stats_mlb_player.headshot = headshot
    stats_mlb_player.gp = gp
    stats_mlb_player.ab = ab
    stats_mlb_player.r = r
    stats_mlb_player.h = h
    stats_mlb_player.two_b = two_b
    stats_mlb_player.three_b = three_b
    stats_mlb_player.hb = hb
    stats_mlb_player.rbi = rbi
    stats_mlb_player.tb = tb
    stats_mlb_player.bb = bb
    stats_mlb_player.so = so
    stats_mlb_player.sb = sb
    stats_mlb_player.avg = avg
    stats_mlb_player.obp = obp
    stats_mlb_player.slg = slg
    stats_mlb_player.ops = ops
    stats_mlb_player.war = war

    db.session.commit()
    return jsonify({"msg": "stats_mlb_player edith successfully"}), 200


@app.route('/stats_nhl_team/<id>', methods=['PUT'])
def stats_nhl_teamEdit(id):
    stats_nhl_team = Stats_nhl_team.query.get(id)
    season = request.json['season']
    season_type = request.json['season_type']
    group_type_comparation = request.json['group_type_comparation']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']
    gp = request.json['gp']
    w = request.json['w']
    L = request.json['L']

    otl = request.json['otl']
    pts = request.json['pts']
    rw = request.json['rw']
    row = request.json['row']
    sow = request.json['sow']
    sol = request.json['sol']
    home = request.json['home']
    away = request.json['away']
    gf = request.json['gf']
    ga = request.json['ga']
    diff = request.json['diff']
    l10 = request.json['l10']
    strk = request.json['strk']

    stats_nhl_team.season = season
    stats_nhl_team.season_type = season_type
    stats_nhl_team.group_type_comparation = group_type_comparation
    stats_nhl_team.team = team
    stats_nhl_team.conference = conference
    stats_nhl_team.division = division
    stats_nhl_team.gp = gp
    stats_nhl_team.w = w
    stats_nhl_team.L = L

    stats_nhl_team.otl = otl
    stats_nhl_team.pts = pts
    stats_nhl_team.rw = rw
    stats_nhl_team.row = row
    stats_nhl_team.sow = sow
    stats_nhl_team.sol = sol
    stats_nhl_team.home = home
    stats_nhl_team.away = away
    stats_nhl_team.gf = gf
    stats_nhl_team.ga = ga
    stats_nhl_team.diff = diff
    stats_nhl_team.l10 = l10
    stats_nhl_team.strk = strk

    db.session.commit()
    return jsonify({"msg": "stats_nhl_team edith successfully"}), 200


@app.route('/stats_nhl_player/<id>', methods=['PUT'])
def stats_nhl_playerEdit(id):
    stats_nhl_player = Stats_nhl_player.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    season = request.json['season']
    team = request.json['team']
    dorsal = request.json['dorsal']
    position = request.json['position']
    headshot = request.json['headshot']
    gp = request.json['gp']

    g = request.json['g']
    a = request.json['a']
    pts = request.json['pts']
    p_m_rating = request.json['p_m_rating']
    pim = request.json['pim']
    sog = request.json['sog']
    spct = request.json['spct']
    ppg = request.json['ppg']
    ppa = request.json['ppa']
    shg = request.json['shg']
    sha = request.json['sha']
    gwg = request.json['gwg']
    gtg = request.json['gtg']
    toi_g = request.json['toi_g']
    prod = request.json['prod']

    stats_nhl_player.name = name
    stats_nhl_player.height = height
    stats_nhl_player.weight = weight
    stats_nhl_player.birth = birth
    stats_nhl_player.season = season
    stats_nhl_player.team = team
    stats_nhl_player.dorsal = dorsal
    stats_nhl_player.position = position
    stats_nhl_player.headshot = headshot
    stats_nhl_player.gp = gp
    stats_nhl_player.g = g
    stats_nhl_player.a = a
    stats_nhl_player.pts = pts
    stats_nhl_player.p_m_rating = p_m_rating
    stats_nhl_player.pim = pim
    stats_nhl_player.sog = sog
    stats_nhl_player.spct = spct
    stats_nhl_player.ppg = ppg
    stats_nhl_player.ppa = ppa
    stats_nhl_player.shg = shg
    stats_nhl_player.sha = sha
    stats_nhl_player.gwg = gwg
    stats_nhl_player.gtg = gtg
    stats_nhl_player.toi_g = toi_g
    stats_nhl_player.prod = prod
    db.session.commit()
    return jsonify({"msg": "stats_nhl_player edith successfully"}), 200


@app.route('/stats_box_fighter/<id>', methods=['PUT'])
def stats_box_fighterEdit(id):
    stats_box_fighter = Stats_box_fighter.query.get(id)
    name = request.json['name']
    nickname = request.json['nickname']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    country = request.json['country']
    season = request.json['season']
    association = request.json['association']
    category = request.json['category']
    w = request.json['w']
    w_by = request.json['w_by']
    L = request.json['L']
    L_by = request.json['L_by']

    stats_box_fighter.name = name
    stats_box_fighter.nickname = nickname
    stats_box_fighter.height = height
    stats_box_fighter.weight = weight
    stats_box_fighter.birth = birth
    stats_box_fighter.country = country
    stats_box_fighter.season = season
    stats_box_fighter.association = association
    stats_box_fighter.category = category
    stats_box_fighter.w = w
    stats_box_fighter.w_by = w_by
    stats_box_fighter.L = L
    stats_box_fighter.L_by = L_by
    db.session.commit()
    return jsonify({"msg": "stats_box_fighter edith successfully"}), 200


@app.route('/stats_mma_fighter/<id>', methods=['PUT'])
def stats_mma_fighterEdit(id):
    stats_mma_fighter = Stats_mma_fighter.query.get(id)
    name = request.json['name']
    nickname = request.json['nickname']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    country = request.json['country']
    season = request.json['season']
    association = request.json['association']
    category = request.json['category']
    w = request.json['w']
    w_by = request.json['w_by']
    L = request.json['L']
    L_by = request.json['L_by']

    stats_mma_fighter.name = name
    stats_mma_fighter.nickname = nickname
    stats_mma_fighter.height = height
    stats_mma_fighter.weight = weight
    stats_mma_fighter.birth = birth
    stats_mma_fighter.country = country
    stats_mma_fighter.season = season
    stats_mma_fighter.association = association
    stats_mma_fighter.category = category
    stats_mma_fighter.w = w
    stats_mma_fighter.w_by = w_by
    stats_mma_fighter.L = L
    stats_mma_fighter.L_by = L_by
    db.session.commit()
    return jsonify({"msg": "stats_mma_fighter edith successfully"}), 200


@app.route('/stats_nfl_team/<id>', methods=['PUT'])
def stats_nfl_teamEdit(id):
    stats_nfl_team = Stats_nfl_team.query.get(id)
    season = request.json['season']
    season_type = request.json['season_type']
    team = request.json['team']
    conference = request.json['conference']
    division = request.json['division']
    TP = request.json['TP']
    ttpg = request.json['ttpg']
    t_td = request.json['t_td']
    t_1_down = request.json['t_1_down']
    Russ_1_d = request.json['Russ_1_d']
    pass_1_d = request.json['pass_1_d']
    down_1_penal = request.json['down_1_penal']
    down_3_eff = request.json['down_3_eff']
    down_3_AVG = request.json['down_3_AVG']
    down_4_eff = request.json['down_4_eff']
    down_4_AVG = request.json['down_4_AVG']
    comp_att = request.json['comp_att']
    net_pass_y = request.json['net_pass_y']
    y_p_pas_attps = request.json['y_p_pas_attps']
    net_pass_y_pg = request.json['net_pass_y_pg']
    pass_td = request.json['pass_td']
    interceptions = request.json['interceptions']
    sacks_y_lost = request.json['sacks_y_lost']
    russ_attps = request.json['russ_attps']
    russ_y = request.json['russ_y']
    y_p_russ_attp = request.json['y_p_russ_attp']
    russ_y_pg = request.json['russ_y_pg']
    russ_td = request.json['russ_td']
    total_of_plays = request.json['total_of_plays']
    total_y = request.json['total_y']
    y_pg = request.json['y_pg']
    kickoffs_t = request.json['kickoffs_t']
    AVG_kickoff_return_y = request.json['AVG_kickoff_return_y']
    punt_t = request.json['punt_t']
    AVG_punt_ruturn_y = request.json['AVG_punt_ruturn_y']
    int_t = request.json['int_t']
    AVG_intercept_y = request.json['AVG_intercept_y']
    net_AVG_punt_y = request.json['net_AVG_punt_y']
    punt_ty = request.json['punt_ty']
    fg_goog_attps = request.json['fg_goog_attps']
    touchback_percent = request.json['touchback_percent']
    penal_ty = request.json['penal_ty']
    penal_y_AVG_pg = request.json['penal_y_AVG_pg']
    possesion_time = request.json['possesion_time']
    fumbles_lost = request.json['fumbles_lost']
    turnover_ratio = request.json['turnover_ratio']

    stats_nfl_team.season = season
    stats_nfl_team.season_type = season_type
    stats_nfl_team.team = team
    stats_nfl_team.conference = conference
    stats_nfl_team.division = division
    stats_nfl_team.TP = TP
    stats_nfl_team.ttpg = ttpg
    stats_nfl_team.t_td = t_td
    stats_nfl_team.t_1_down = t_1_down
    stats_nfl_team.Russ_1_d = Russ_1_d
    stats_nfl_team.pass_1_d = pass_1_d
    stats_nfl_team.down_1_penal = down_1_penal
    stats_nfl_team.down_3_eff = down_3_eff
    stats_nfl_team.down_3_AVG = down_3_AVG
    stats_nfl_team.down_4_eff = down_4_eff
    stats_nfl_team.down_4_AVG = down_4_AVG
    stats_nfl_team.comp_att = comp_att
    stats_nfl_team.net_pass_y = net_pass_y
    stats_nfl_team.y_p_pas_attps = y_p_pas_attps
    stats_nfl_team.net_pass_y_pg = net_pass_y_pg
    stats_nfl_team.pass_td = pass_td
    stats_nfl_team.interceptions = interceptions
    stats_nfl_team.sacks_y_lost = sacks_y_lost
    stats_nfl_team.russ_attps = russ_attps
    stats_nfl_team.russ_y = russ_y
    stats_nfl_team.y_p_russ_attp = y_p_russ_attp
    stats_nfl_team.russ_y_pg = russ_y_pg
    stats_nfl_team.russ_td = russ_td
    stats_nfl_team.total_of_plays = total_of_plays
    stats_nfl_team.total_y = total_y
    stats_nfl_team.y_pg = y_pg
    stats_nfl_team.kickoffs_t = kickoffs_t
    stats_nfl_team.AVG_kickoff_return_y = AVG_kickoff_return_y
    stats_nfl_team.punt_t = punt_t
    stats_nfl_team.AVG_punt_ruturn_y = AVG_punt_ruturn_y
    stats_nfl_team.int_t = int_t
    stats_nfl_team.AVG_intercept_y = AVG_intercept_y
    stats_nfl_team.net_AVG_punt_y = net_AVG_punt_y
    stats_nfl_team.punt_ty = punt_ty
    stats_nfl_team.fg_goog_attps = fg_goog_attps
    stats_nfl_team.touchback_percent = touchback_percent
    stats_nfl_team.penal_ty = penal_ty
    stats_nfl_team.penal_y_AVG_pg = penal_y_AVG_pg
    stats_nfl_team.possesion_time = possesion_time
    stats_nfl_team.fumbles_lost = fumbles_lost
    stats_nfl_team.turnover_ratio = turnover_ratio

    db.session.commit()
    return jsonify({"msg": "stats_nfl_team edith successfully"}), 200

@app.route('/stats_defensive_player_nfl/<id>', methods=['PUT'])
def stats_defensive_player_nflEdit(id):
    stats_defensive_player_nfl = Stats_defensive_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    tack_solo = request.json['tack_solo']
    tack_ast = request.json['tack_ast']
    tack_total = request.json['tack_total']
    sacks = request.json['sacks']
    sacks_yards = request.json['sacks_yards']
    tfl = request.json['tfl']
    pd = request.json['pd']
    Int = request.json['Int']
    yds = request.json['yds']
    ing = request.json['ing']
    td = request.json['td']
    ff = request.json['ff']
    fr = request.json['fr']
    ftd = request.json['ftd']
    kb = request.json['kb']

    stats_defensive_player_nfl.name = name
    stats_defensive_player_nfl.height = height
    stats_defensive_player_nfl.weight = weight
    stats_defensive_player_nfl.birth = birth
    stats_defensive_player_nfl.position = position
    stats_defensive_player_nfl.headshot = headshot
    stats_defensive_player_nfl.dorsal = dorsal
    stats_defensive_player_nfl.season = season
    stats_defensive_player_nfl.team = team
    stats_defensive_player_nfl.games = games
    stats_defensive_player_nfl.tack_solo = tack_solo
    stats_defensive_player_nfl.tack_ast = tack_ast
    stats_defensive_player_nfl.tack_total = tack_total
    stats_defensive_player_nfl.sacks = sacks
    stats_defensive_player_nfl.sacks_yards = sacks_yards
    stats_defensive_player_nfl.tfl = tfl
    stats_defensive_player_nfl.pd = pd
    stats_defensive_player_nfl.Int = Int
    stats_defensive_player_nfl.yds = yds
    stats_defensive_player_nfl.ing = ing
    stats_defensive_player_nfl.td = td
    stats_defensive_player_nfl.ff = ff
    stats_defensive_player_nfl.fr = fr
    stats_defensive_player_nfl.ftd = ftd
    stats_defensive_player_nfl.kb = kb
    db.session.commit()
    return jsonify({"msg": "stats_defensive_player_nfl edith successfully"}), 200


@app.route('/stats_offensive_player_nfl/<id>', methods=['PUT'])
def stats_offensive_player_nflEdit(id):
    stats_offensive_player_nfl = Stats_offensive_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']

    Cmp = request.json['Cmp']
    pass_att = request.json['pass_att']
    cmp_AVG = request.json['cmp_AVG']
    yards = request.json['yards']
    yards_AVG = request.json['yards_AVG']
    yards_pg = request.json['yards_pg']
    pass_td = request.json['pass_td']
    Int = request.json['Int']
    asck = request.json['asck']
    syl = request.json['syl']
    rtg = request.json['rtg']
    russ_att = request.json['russ_att']
    russ_yards = request.json['russ_yards']
    yards_p_russ = request.json['yards_p_russ']
    big = request.json['big']
    rush_tt = request.json['rush_tt']
    rush_yard_pg = request.json['rush_yard_pg']
    fum = request.json['fum']
    lst = request.json['lst']
    long_pass = request.json['long_pass']
    fd = request.json['fd']
    rec = request.json['rec']
    r_tgts = request.json['r_tgts']
    r_yards = request.json['r_yards']
    yards_p_r = request.json['yards_p_r']
    r_td = request.json['r_td']
    lr = request.json['lr']
    r_big = request.json['r_big']
    r_ypg = request.json['r_ypg']
    r_fl = request.json['r_fl']
    r_yac = request.json['r_yac']
    r_fd = request.json['r_fd']
    pts = request.json['pts']

    stats_offensive_player_nfl.name = name
    stats_offensive_player_nfl.height = height
    stats_offensive_player_nfl.weight = weight
    stats_offensive_player_nfl.birth = birth
    stats_offensive_player_nfl.position = position
    stats_offensive_player_nfl.headshot = headshot
    stats_offensive_player_nfl.dorsal = dorsal
    stats_offensive_player_nfl.season = season
    stats_offensive_player_nfl.team = team
    stats_offensive_player_nfl.games = games
    stats_offensive_player_nfl.Cmp = Cmp
    stats_offensive_player_nfl.pass_att = pass_att
    stats_offensive_player_nfl.cmp_AVG = cmp_AVG
    stats_offensive_player_nfl.yards = yards
    stats_offensive_player_nfl.yards_AVG = yards_AVG
    stats_offensive_player_nfl.yards_pg = yards_pg
    stats_offensive_player_nfl.pass_td = pass_td
    stats_offensive_player_nfl.Int = Int
    stats_offensive_player_nfl.asck = asck
    stats_offensive_player_nfl.syl = syl
    stats_offensive_player_nfl.rtg = rtg
    stats_offensive_player_nfl.russ_att = russ_att
    stats_offensive_player_nfl.russ_yards = russ_yards
    stats_offensive_player_nfl.yards_p_russ = yards_p_russ
    stats_offensive_player_nfl.big = big
    stats_offensive_player_nfl.rush_tt = rush_tt
    stats_offensive_player_nfl.rush_yard_pg = rush_yard_pg
    stats_offensive_player_nfl.fum = fum
    stats_offensive_player_nfl.lst = lst 
    stats_offensive_player_nfl.lst = lst 
    stats_offensive_player_nfl.long_pass = long_pass
    stats_offensive_player_nfl.fd = fd
    stats_offensive_player_nfl.rec = rec
    stats_offensive_player_nfl.r_tgts = r_tgts
    stats_offensive_player_nfl.r_yards = r_yards
    stats_offensive_player_nfl.yards_p_r = yards_p_r
    stats_offensive_player_nfl.r_td = r_td
    stats_offensive_player_nfl.lr = lr
    stats_offensive_player_nfl.r_big = r_big
    stats_offensive_player_nfl.r_ypg = r_ypg
    stats_offensive_player_nfl.r_fl = r_fl
    stats_offensive_player_nfl.r_yac = r_yac
    stats_offensive_player_nfl.r_fd = r_fd
    stats_offensive_player_nfl.pts = pts
    db.session.commit()
    return jsonify({"msg": "stats_offensive_player_nfl edith successfully"}), 200


@app.route('/stats_returning_player_nfl/<id>', methods=['PUT'])
def stats_returning_player_nflEdit(id):
    stats_returning_player_nfl = Stats_returning_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    kick_returns = request.json['kick_returns']
    kick_returns_yards = request.json['kick_returns_yards']
    yards_p_k_p = request.json['yards_p_k_p']
    l_k_r = request.json['l_k_r']
    k_r_td = request.json['k_r_td']
    punt_r = request.json['punt_r']
    punt_r_y = request.json['punt_r_y']
    y_ppr = request.json['y_ppr']
    lpr = request.json['lpr']
    pr_td = request.json['pr_td']
    punt_r_fair_carches = request.json['punt_r_fair_carches']

    stats_returning_player_nfl.name = name
    stats_returning_player_nfl.height = height
    stats_returning_player_nfl.weight = weight
    stats_returning_player_nfl.birth = birth
    stats_returning_player_nfl.position = position
    stats_returning_player_nfl.headshot = headshot
    stats_returning_player_nfl.dorsal = dorsal
    stats_returning_player_nfl.season = season
    stats_returning_player_nfl.team = team
    stats_returning_player_nfl.games = games
    stats_returning_player_nfl.kick_returns = kick_returns
    stats_returning_player_nfl.kick_returns_yards = kick_returns_yards
    stats_returning_player_nfl.yards_p_k_p = yards_p_k_p
    stats_returning_player_nfl.l_k_r = l_k_r
    stats_returning_player_nfl.k_r_td = k_r_td
    stats_returning_player_nfl.punt_r = punt_r
    stats_returning_player_nfl.punt_r_y = punt_r_y
    stats_returning_player_nfl.y_ppr = y_ppr
    stats_returning_player_nfl.lpr = lpr
    stats_returning_player_nfl.pr_td = pr_td
    stats_returning_player_nfl.punt_r_fair_carches = punt_r_fair_carches
    db.session.commit()
    return jsonify({"msg": "stats_returning_player_nfl edith successfully"}), 200


@app.route('/stats_kiking_player_nfl/<id>', methods=['PUT'])
def stats_kiking_player_nflEdit(id):
    stats_kiking_player_nfl = Stats_kiking_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    fgm = request.json['fgm']
    fga = request.json['fga']
    fg_AVG = request.json['fg_AVG']
    lng = request.json['lng']
    yars_f_goals_1_19 = request.json['yars_f_goals_1_19']
    yars_f_goals_20_29 = request.json['yars_f_goals_20_29']
    yars_f_goals_30_49 = request.json['yars_f_goals_30_49']
    yars_f_goals_40_49 = request.json['yars_f_goals_40_49']
    more_50 = request.json['more_50']
    xpm = request.json['xpm']
    xpa = request.json['xpa']
    xp_AVG = request.json['xp_AVG']

    stats_kiking_player_nfl.name = name
    stats_kiking_player_nfl.height = height
    stats_kiking_player_nfl.weight = weight
    stats_kiking_player_nfl.birth = birth
    stats_kiking_player_nfl.position = position
    stats_kiking_player_nfl.headshot = headshot
    stats_kiking_player_nfl.dorsal = dorsal
    stats_kiking_player_nfl.season = season
    stats_kiking_player_nfl.team = team
    stats_kiking_player_nfl.games = games
    stats_kiking_player_nfl.fgm = fgm
    stats_kiking_player_nfl.fga = fga
    stats_kiking_player_nfl.fg_AVG = fg_AVG
    stats_kiking_player_nfl.lng = lng
    stats_kiking_player_nfl.yars_f_goals_1_19 = yars_f_goals_1_19
    stats_kiking_player_nfl.yars_f_goals_20_29 = yars_f_goals_20_29
    stats_kiking_player_nfl.yars_f_goals_30_49 = yars_f_goals_30_49
    stats_kiking_player_nfl.yars_f_goals_40_49 = yars_f_goals_40_49
    stats_kiking_player_nfl.more_50 = more_50
    stats_kiking_player_nfl.xpm = xpm
    stats_kiking_player_nfl.xpa = xpa
    stats_kiking_player_nfl.xp_AVG = xp_AVG
    db.session.commit()
    return jsonify({"msg": "stats_kiking_player_nfl edith successfully"}), 200


@app.route('/stats_punting_player_nfl/<id>', methods=['PUT'])
def stats_punting_player_nflEdit(id):
    stats_punting_player_nfl = Stats_punting_player_nfl.query.get(id)
    name = request.json['name']
    height = request.json['height']
    weight = request.json['weight']
    birth = request.json['birth']
    position = request.json['position']
    headshot = request.json['headshot']
    dorsal = request.json['dorsal']
    season = request.json['season']
    team = request.json['team']
    games = request.json['games']
    punts = request.json['punts']
    yards = request.json['yards']
    lng = request.json['lng']
    lng = request.json['lng']
    AVG = request.json['AVG']
    net = request.json['net']
    p_blk = request.json['p_blk']
    IN_20 = request.json['IN_20']
    tb = request.json['tb']
    fc = request.json['fc']
    att = request.json['att']
    punt_return_yds = request.json['punt_return_yds']
    AVG_punt_retun_yards = request.json['AVG_punt_retun_yards']

    stats_punting_player_nfl.name = name
    stats_punting_player_nfl.height = height
    stats_punting_player_nfl.weight = weight
    stats_punting_player_nfl.birth = birth
    stats_punting_player_nfl.position = position
    stats_punting_player_nfl.headshot = headshot
    stats_punting_player_nfl.dorsal = dorsal
    stats_punting_player_nfl.season = season
    stats_punting_player_nfl.team = team
    stats_punting_player_nfl.games = games
    stats_punting_player_nfl.punts = punts
    stats_punting_player_nfl.yards = yards
    stats_punting_player_nfl.lng = lng
    stats_punting_player_nfl.lng = lng
    stats_punting_player_nfl.AVG = AVG
    stats_punting_player_nfl.net = net
    stats_punting_player_nfl.p_blk = p_blk
    stats_punting_player_nfl.IN_20 = IN_20
    stats_punting_player_nfl.tb = tb
    stats_punting_player_nfl.fc = fc
    stats_punting_player_nfl.att = att
    stats_punting_player_nfl.punt_return_yds = punt_return_yds
    stats_punting_player_nfl.AVG_punt_retun_yards = AVG_punt_retun_yards
    db.session.commit()
    return jsonify({"msg": "stats_punting_player_nfl edith successfully"}), 200

# Endpoint for deleting a record

#-----------------Delete-----------------------------------------------

@app.route("/soccer_tournament/<id>", methods=["DELETE"])
def soccer_tournament_delete(id):
    soccer_tournament = Soccer_Tournament.query.get(id)
    db.session.delete(soccer_tournament)
    db.session.commit()
    return "soccer_tournament was successfully deleted"

@app.route("/futures/<id>", methods=["DELETE"])
def futures_delete(id):
    futures = Futures.query.get(id)
    db.session.delete(futures)
    db.session.commit()
    return "futures was successfully deleted"

@app.route("/injuries/<id>", methods=["DELETE"])
def injuries_delete(id):
    injuries = Injuries.query.get(id)
    db.session.delete(injuries)
    db.session.commit()
    return "injuries was successfully deleted"

@app.route("/props/<id>", methods=["DELETE"])
def props_delete(id):
    props = Props.query.get(id)
    db.session.delete(props)
    db.session.commit()
    return "props was successfully deleted"

@app.route("/odds_to_win/<id>", methods=["DELETE"])
def odds_to_win_delete(id):
    odds_to_win = Odds_to_win.query.get(id)
    db.session.delete(odds_to_win)
    db.session.commit()
    return "odds_to_win was successfully deleted"

@app.route("/logos_nfl/<id>", methods=["DELETE"])
def logos_nfl_delete(id):
    logos_nfl = Logos_NFL.query.get(id)
    db.session.delete(logos_nfl)
    db.session.commit()
    return "logos_nfl was successfully deleted"

@app.route("/logos_nba/<id>", methods=["DELETE"])
def logos_nba_delete(id):
    logos_nba = Logos_NBA.query.get(id)
    db.session.delete(logos_nba)
    db.session.commit()
    return "logos_nba was successfully deleted"

@app.route("/logos_mlb/<id>", methods=["DELETE"])
def logos_mlb_delete(id):
    logos_mlb = Logos_MLB.query.get(id)
    db.session.delete(logos_mlb)
    db.session.commit()
    return "logos_nba was successfully deleted"

@app.route("/logos_nhl/<id>", methods=["DELETE"])
def logos_nhl_delete(id):
    logos_nhl = Logos_NHL.query.get(id)
    db.session.delete(logos_nhl)
    db.session.commit()
    return "logos_nhl was successfully deleted"

@app.route("/logos_soccer/<id>", methods=["DELETE"])
def logos_soccer_delete(id):
    logos_soccer = Logos_SOCCER.query.get(id)
    db.session.delete(logos_soccer)
    db.session.commit()
    return "logos_soccer was successfully deleted"

@app.route("/logos_ncaa_basketball/<id>", methods=["DELETE"])
def logos_ncaa_basketball_delete(id):
    logos_ncaa_basketball = Logos_Ncaa_Basketball.query.get(id)
    db.session.delete(logos_ncaa_basketball)
    db.session.commit()
    return "logos_ncaa_basketball was successfully deleted"

@app.route("/logos_ncaa_football/<id>", methods=["DELETE"])
def logos_ncaa_football_delete(id):
    logos_ncaa_football = Logos_Ncaa_Football.query.get(id)
    db.session.delete(logos_ncaa_football)
    db.session.commit()
    return "logos_ncaa_football was successfully deleted"

@app.route("/logos_ncaa_baseball/<id>", methods=["DELETE"])
def logos_ncaa_baseball_delete(id):
    logos_ncaa_baseball = Logos_Ncaa_Baseball.query.get(id)
    db.session.delete(logos_ncaa_baseball)
    db.session.commit()
    return "logos_ncaa_baseball was successfully deleted"

@app.route("/soccer/<id>", methods=["DELETE"])
def soccer_delete(id):
    soccer = Soccer.query.get(id)
    db.session.delete(soccer)
    db.session.commit()
    return "soccer was successfully deleted"

@app.route("/casinos/<id>", methods=["DELETE"])
def casinos_delete(id):
    casinos = Casinos.query.get(id)
    db.session.delete(casinos)
    db.session.commit()
    return "casinos was successfully deleted"

@app.route("/mlb/<id>", methods=["DELETE"])
def mlb_delete(id):
    mlb = Mlb.query.get(id)
    db.session.delete(mlb)
    db.session.commit()
    return "mlb was successfully deleted"

@app.route("/nfl/<id>", methods=["DELETE"])
def nfl_delete(id):
    nfl = Nfl.query.get(id)
    db.session.delete(nfl)
    db.session.commit()
    return "nfl was successfully deleted"

@app.route("/ncaa_football/<id>", methods=["DELETE"])
def ncaa_football_delete(id):
    ncaa_football = Ncaa_Football.query.get(id)
    db.session.delete(ncaa_football)
    db.session.commit()
    return "ncaa_football was successfully deleted"

@app.route("/stats_ncaa_football_team/<id>", methods=["DELETE"])
def stats_ncaa_football_team_delete(id):
    stats_ncaa_football_team = Stats_ncaa_football_team.query.get(id)
    db.session.delete(stats_ncaa_football_team)
    db.session.commit()
    return "stats_ncaa_football_team was successfully deleted"

@app.route("/stats_offensive_player_ncaa_football/<id>", methods=["DELETE"])
def Stats_offensive_player_ncaa_football_delete(id):
    stats_offensive_player_ncaa_football = Stats_offensive_player_ncaa_football.query.get(id)
    db.session.delete(stats_offensive_player_ncaa_football)
    db.session.commit()
    return "Stats_offensive_player_ncaa_football was successfully deleted"

@app.route("/stats_defensive_player_ncca_football/<id>", methods=["DELETE"])
def stats_defensive_player_ncca_football_delete(id):
    stats_defensive_player_ncca_football = Stats_defensive_player_ncca_football.query.get(id)
    db.session.delete(stats_defensive_player_ncca_football)
    db.session.commit()
    return "stats_defensive_player_ncca_football was successfully deleted"

@app.route("/stats_returning_player_ncaa_football/<id>", methods=["DELETE"])
def stats_returning_player_ncaa_football_delete(id):
    stats_returning_player_ncaa_football = Stats_returning_player_ncaa_football.query.get(id)
    db.session.delete(stats_returning_player_ncaa_football)
    db.session.commit()
    return "stats_returning_player_ncaa_football was successfully deleted"

@app.route("/stats_punting_player_ncaa_football/<id>", methods=["DELETE"])
def stats_punting_player_ncaa_football_delete(id):
    stats_punting_player_ncaa_football = Stats_punting_player_ncaa_football.query.get(id)
    db.session.delete(stats_punting_player_ncaa_football)
    db.session.commit()
    return "stats_punting_player_ncaa_football was successfully deleted"

@app.route("/stats_kiking_player_ncaa_football/<id>", methods=["DELETE"])
def stats_kiking_player_ncaa_football_delete(id):
    stats_kiking_player_ncaa_football = Stats_kiking_player_ncaa_football.query.get(id)
    db.session.delete(stats_kiking_player_ncaa_football)
    db.session.commit()
    return "stats_kiking_player_ncaa_football was successfully deleted"

@app.route("/nba/<id>", methods=["DELETE"])
def nba_delete(id):
    nba = Nba.query.get(id)
    db.session.delete(nba)
    db.session.commit()
    return "nba was successfully deleted"


@app.route("/ncaa_basketball/<id>", methods=["DELETE"])
def ncaa_basketball_delete(id):
    ncaa_basketball = Ncaa_Basketball.query.get(id)
    db.session.delete(ncaa_basketball)
    db.session.commit()
    return "ncaa_basketball was successfully deleted"


@app.route("/nhl/<id>", methods=["DELETE"])
def nhl_delete(id):
    nhl = Nhl.query.get(id)
    db.session.delete(nhl)
    db.session.commit()
    return "nhl was successfully deleted"


@app.route("/boxeo/<id>", methods=["DELETE"])
def boxeo_delete(id):
    boxeo = Boxeo.query.get(id)
    db.session.delete(boxeo)
    db.session.commit()
    return "boxeo was successfully deleted"


@app.route("/mma/<id>", methods=["DELETE"])
def mma_delete(id):
    mma = Mma.query.get(id)
    db.session.delete(mma)
    db.session.commit()
    return "mma was successfully deleted"


@app.route("/nascar/<id>", methods=["DELETE"])
def nascar_delete(id):
    nascar = Nascar.query.get(id)
    db.session.delete(nascar)
    db.session.commit()
    return "nascar was successfully deleted"

@app.route("/moto_gp/<id>", methods=["DELETE"])
def moto_gp_delete(id):
    moto_gp = Moto_GP.query.get(id)
    db.session.delete(moto_gp)
    db.session.commit()
    return "moto_gp was successfully deleted"


@app.route("/match_ups_nascar/<id>", methods=["DELETE"])
def match_ups_nascar_delete(id):
    match_ups_nascar = Match_Ups_Nacar.query.get(id)
    db.session.delete(match_ups_nascar)
    db.session.commit()
    return "match_ups_nascar was successfully deleted"


@app.route("/golf/<id>", methods=["DELETE"])
def golf_delete(id):
    golf = Golf.query.get(id)
    db.session.delete(golf)
    db.session.commit()
    return "golf was successfully deleted"


@app.route("/stats_soccer_team/<id>", methods=["DELETE"])
def stats_soccer_team_delete(id):
    stats_soccer_team = Stats_Soccer_Team.query.get(id)
    db.session.delete(stats_soccer_team)
    db.session.commit()
    return "stats_soccer_team was successfully deleted"

@app.route("/stats_soccer_player/<id>", methods=["DELETE"])
def stats_soccer_player_delete(id):
    stats_soccer_player = Stats_Soccer_Player.query.get(id)
    db.session.delete(stats_soccer_player)
    db.session.commit()
    return "stats_soccer_player was successfully deleted"

@app.route("/stats_nba_player/<id>", methods=["DELETE"])
def stats_nba_player_delete(id):
    stats_nba_player = Stats_nba_player.query.get(id)
    db.session.delete(stats_nba_player)
    db.session.commit()
    return "stats_nba_player was successfully deleted"

@app.route("/stats_ncaa_basket_player/<id>", methods=["DELETE"])
def stats_ncaa_basket_player_delete(id):
    stats_ncaa_basket_player = Stats_ncaa_basket_player.query.get(id)
    db.session.delete(stats_ncaa_basket_player)
    db.session.commit()
    return "stats_ncaa_basket_player was successfully deleted"

@app.route("/stats_ncaa_basket_team/<id>", methods=["DELETE"])
def stats_ncaa_basket_team_delete(id):
    stats_ncaa_basket_team = Stats_ncaa_basket_team.query.get(id)
    db.session.delete(stats_ncaa_basket_team)
    db.session.commit()
    return "stats_ncaa_basket_team was successfully deleted"

@app.route("/ncaa_baseball/<id>", methods=["DELETE"])
def ncaa_baseball_delete(id):
    ncaa_baseball = Ncaa_Baseball.query.get(id)
    db.session.delete(ncaa_baseball)
    db.session.commit()
    return "ncaa_baseball was successfully deleted"

@app.route("/stats_ncaa_baseball_player/<id>", methods=["DELETE"])
def stats_ncaa_baseball_player_delete(id):
    stats_ncaa_baseball_player = Stats_ncaa_baseball_player.query.get(id)
    db.session.delete(stats_ncaa_baseball_player)
    db.session.commit()
    return "stats_ncaa_baseball_player was successfully deleted"

@app.route("/stats_ncaa_baseball_team/<id>", methods=["DELETE"])
def stats_ncaa_baseball_team_delete(id):
    stats_ncaa_baseball_team = Stats_ncaa_baseball_team.query.get(id)
    db.session.delete(stats_ncaa_baseball_team)
    db.session.commit()
    return "stats_ncaa_baseball_team was successfully deleted"

@app.route("/stats_nba_team/<id>", methods=["DELETE"])
def stats_nba_team_delete(id):
    stats_nba_team = Stats_nba_team.query.get(id)
    db.session.delete(stats_nba_team)
    db.session.commit()
    return "stats_nba_team was successfully deleted"


@app.route("/stats_mlb_team/<id>", methods=["DELETE"])
def stats_mlb_team_delete(id):
    stats_mlb_team = Stats_mlb_team.query.get(id)
    db.session.delete(stats_mlb_team)
    db.session.commit()
    return "stats_mlb_team was successfully deleted"


@app.route("/stats_mlb_player/<id>", methods=["DELETE"])
def stats_mlb_player_delete(id):
    stats_mlb_player = Stats_mlb_player.query.get(id)
    db.session.delete(stats_mlb_player)
    db.session.commit()
    return "stats_mlb_player was successfully deleted"


@app.route("/stats_nhl_team/<id>", methods=["DELETE"])
def stats_nhl_team_delete(id):
    stats_nhl_team = Stats_nhl_team.query.get(id)
    db.session.delete(stats_nhl_team)
    db.session.commit()
    return "stats_nhl_team was successfully deleted"


@app.route("/stats_nhl_player/<id>", methods=["DELETE"])
def stats_nhl_player_delete(id):
    stats_nhl_player = Stats_nhl_player.query.get(id)
    db.session.delete(stats_nhl_player)
    db.session.commit()
    return "stats_nhl_player was successfully deleted"


@app.route("/stats_box_fighter/<id>", methods=["DELETE"])
def stats_box_fighter_delete(id):
    stats_box_fighter = Stats_box_fighter.query.get(id)
    db.session.delete(stats_box_fighter)
    db.session.commit()
    return "stats_box_fighter was successfully deleted"


@app.route("/stats_mma_fighter/<id>", methods=["DELETE"])
def stats_mma_fighter_delete(id):
    stats_mma_fighter = Stats_mma_fighter.query.get(id)
    db.session.delete(stats_mma_fighter)
    db.session.commit()
    return "stats_mma_fighter was successfully deleted"


@app.route("/nascar_drivers/<id>", methods=["DELETE"])
def nascar_drivers_delete(id):
    nascar_drivers = Nascar_drivers.query.get(id)
    db.session.delete(nascar_drivers)
    db.session.commit()
    return "nascar_drivers was successfully deleted"

@app.route("/moto_gp_drivers/<id>", methods=["DELETE"])
def moto_gp_drivers_delete(id):
    moto_gp_drivers = Moto_gp_drivers.query.get(id)
    db.session.delete(moto_gp_drivers)
    db.session.commit()
    return "moto_gp_drivers was successfully deleted"


@app.route("/golfer/<id>", methods=["DELETE"])
def golfer_delete(id):
    golfer = Golfer.query.get(id)
    db.session.delete(golfer)
    db.session.commit()
    return "golfer was successfully deleted"


@app.route("/stats_nfl_team/<id>", methods=["DELETE"])
def stats_nfl_team_delete(id):
    stats_nfl_team = Stats_nfl_team.query.get(id)
    db.session.delete(stats_nfl_team)
    db.session.commit()
    return "stats_nfl_team was successfully deleted"


@app.route("/stats_defensive_player_nfl/<id>", methods=["DELETE"])
def stats_defensive_player_nfl_delete(id):
    stats_defensive_player_nfl = Stats_defensive_player_nfl.query.get(id)
    db.session.delete(stats_defensive_player_nfl)
    db.session.commit()
    return "stats_defensive_player_nfl was successfully deleted"


@app.route("/stats_offensive_player_nfl/<id>", methods=["DELETE"])
def stats_offensive_player_nfl_delete(id):
    stats_offensive_player_nfl = Stats_offensive_player_nfl.query.get(id)
    db.session.delete(stats_offensive_player_nfl)
    db.session.commit()
    return "stats_offensive_player_nfl was successfully deleted"


@app.route("/stats_returning_player_nfl/<id>", methods=["DELETE"])
def stats_returning_player_nfl_delete(id):
    stats_returning_player_nfl = Stats_returning_player_nfl.query.get(id)
    db.session.delete(stats_returning_player_nfl)
    db.session.commit()
    return "stats_returning_player_nfl was successfully deleted"


@app.route("/stats_kiking_player_nfl/<id>", methods=["DELETE"])
def stats_kiking_player_nfl_delete(id):
    stats_kiking_player_nfl = Stats_kiking_player_nfl.query.get(id)
    db.session.delete(stats_kiking_player_nfl)
    db.session.commit()
    return "stats_kiking_player_nfl was successfully deleted"


@app.route("/stats_punting_player_nfl/<id>", methods=["DELETE"])
def stats_punting_player_nfl_delete(id):
    stats_punting_player_nfl = Stats_punting_player_nfl.query.get(id)
    db.session.delete(stats_punting_player_nfl)
    db.session.commit()
    return "stats_punting_player_nfl was successfully deleted"
