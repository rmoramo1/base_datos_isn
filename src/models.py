from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
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


class Casinos(db.Model):
    __tablename__ = 'casinos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Injuries(db.Model):
    __tablename__ = 'injuries'

    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.String(20), nullable=False)
    name_player = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(20), nullable=False)
    injurie = db.Column(db.String(20), nullable=False)
    time_injurie = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "sport": self.sport,
            "name_player": self.name_player,
            "team": self.team,
            "injurie": self.injurie,
            "time_injurie": self.time_injurie,
            "date": self.date
        }


class Futures(db.Model):
    __tablename__ = 'futures'

    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.String(20), nullable=False)
    future = db.Column(db.String(20), nullable=False)
    line = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "sport": self.sport,
            "future": self.future,
            "line": self.line,
            "date": self.date,
        }


class Props(db.Model):
    __tablename__ = 'props'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    type_prop = db.Column(db.String(30), nullable=False)
    sport = db.Column(db.String(30), nullable=False)
    feature = db.Column(db.String(30), nullable=False)
    line = db.Column(db.String(10), nullable=False)
    home = db.Column(db.String(10), nullable=False)
    away = db.Column(db.String(10), nullable=False)
    # def __repr__(self):
    #     return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "type_prop": self.type_prop,
            "sport": self.sport,
            "feature": self.feature,
            "line": self.line,
            "home": self.home,
            "away": self.away
            # do not serialize the password, its a security breach
        }


class Odds_to_win(db.Model):
    __tablename__ = 'odds_to_win'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    sport = db.Column(db.String(30), nullable=False)
    type_odd = db.Column(db.String(30), nullable=False)
    line = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(10), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    # def __repr__(self):
    #     return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "sport": self.sport,
            "type_odd": self.type_odd,
            "line": self.line,
            "team": self.team,
            "date": self.date
            # do not serialize the password, its a security breach
        }


class Logos_NFL(db.Model):
    __tablename__ = 'logos_nfl'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }


class Logos_NBA(db.Model):
    __tablename__ = 'logos_nba'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }


class Logos_MLB(db.Model):
    __tablename__ = 'logos_mlb'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }


class Logos_NHL(db.Model):
    __tablename__ = 'logos_nhl'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }


class Logos_SOCCER(db.Model):
    __tablename__ = 'logos_soccer'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }

class Logos_Ncaa_Basketball(db.Model):
    __tablename__ = 'logos_ncaa_basketball'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }

class Logos_Ncaa_Football(db.Model):
    __tablename__ = 'logos_ncaa_football'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }

class Logos_Ncaa_Baseball(db.Model):
    __tablename__ = 'logos_ncaa_baseball'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "team": self.team,
            "url": self.url,
        }

class Soccer_Tournament(db.Model):
    __tablename__ = 'soccer_tournament'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(70), nullable=False)
    tournament = db.Column(db.String(70), nullable=True)
    # def __repr__(self):
    #     return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "country": self.country,
            "tournament": self.tournament
            # do not serialize the password, its a security breach
        }


class Mlb(db.Model):
    __tablename__ = "mlb"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    hour = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    casino = db.Column(db.String(20), nullable=False)
    rotation_home = db.Column(db.String(10), nullable=False)
    rotation_away = db.Column(db.String(10), nullable=False)
    away = db.Column(db.String(30), nullable=False)
    pitcher_a = db.Column(db.String(30), nullable=False)
    home = db.Column(db.String(30), nullable=False)
    pitcher_h = db.Column(db.String(30), nullable=False)
    rl_away = db.Column(db.String(10), nullable=False)
    rl_home = db.Column(db.String(10), nullable=False)
    juice_rl_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_rl_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)
    # ------------------------------------------------------------------------
    rl_away_f5 = db.Column(db.String(10), default=0, nullable=False)
    rl_home_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_rl_away_f5 = db.Column(db.String(10), default=-110, nullable=False)
    juice_rl_home_f5 = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway_f5 = db.Column(db.String(10), default=0, nullable=False)
    moneyLineHome_f5 = db.Column(db.String(10), default=0, nullable=False)
    total_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_total_over_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    juice_total_under_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    tt_away_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_over_away_f5 = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    tt_home_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_over_home_f5 = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    fs_away_f5 = db.Column(db.String(10), default=0, nullable=False)
    fs_home_f5 = db.Column(db.String(10), default=0, nullable=False)
    # ----------------------------------------------------------------------
    sa_1inning = db.Column(db.String(10), default=0, nullable=False)
    sh_1inning = db.Column(db.String(10), default=0, nullable=False)
    sa_2inning = db.Column(db.String(10), default=0, nullable=False)
    sh_2inning = db.Column(db.String(10), default=0, nullable=False)
    sa_3inning = db.Column(db.String(10), default=0, nullable=False)
    sh_3inning = db.Column(db.String(10), default=0, nullable=False)
    sa_4inning = db.Column(db.String(10), default=0, nullable=False)
    sh_4inning = db.Column(db.String(10), default=0, nullable=False)
    sa_5inning = db.Column(db.String(10), default=0, nullable=False)
    sh_5inning = db.Column(db.String(10), default=0, nullable=False)
    sa_6inning = db.Column(db.String(10), default=0, nullable=False)
    sh_6inning = db.Column(db.String(10), default=0, nullable=False)
    sa_7inning = db.Column(db.String(10), default=0, nullable=False)
    sh_7inning = db.Column(db.String(10), default=0, nullable=False)
    sa_8inning = db.Column(db.String(10), default=0, nullable=False)
    sh_8inning = db.Column(db.String(10), default=0, nullable=False)
    sa_9inning = db.Column(db.String(10), default=0, nullable=False)
    sh_9inning = db.Column(db.String(10), default=0, nullable=False)
    sa_10inning = db.Column(db.String(10), default=0, nullable=False)
    sh_10inning = db.Column(db.String(10), default=0, nullable=False)
    sa_11inning = db.Column(db.String(10), default=0, nullable=False)
    sh_11inning = db.Column(db.String(10), default=0, nullable=False)
    sa_12inning = db.Column(db.String(10), default=0, nullable=False)
    sh_12inning = db.Column(db.String(10), default=0, nullable=False)
    sa_13inning = db.Column(db.String(10), default=0, nullable=False)
    sh_13inning = db.Column(db.String(10), default=0, nullable=False)
    sa_14inning = db.Column(db.String(10), default=0, nullable=False)
    sh_14inning = db.Column(db.String(10), default=0, nullable=False)
    sa_15inning = db.Column(db.String(10), default=0, nullable=False)
    sh_15inning = db.Column(db.String(10), default=0, nullable=False)
    sa_16inning = db.Column(db.String(10), default=0, nullable=False)
    sh_16inning = db.Column(db.String(10), default=0, nullable=False)
    sa_17inning = db.Column(db.String(10), default=0, nullable=False)
    sh_17inning = db.Column(db.String(10), default=0, nullable=False)
    sa_18inning = db.Column(db.String(10), default=0, nullable=False)
    sh_18inning = db.Column(db.String(10), default=0, nullable=False)
    sa_19inning = db.Column(db.String(10), default=0, nullable=False)
    sh_19inning = db.Column(db.String(10), default=0, nullable=False)
    sa_20inning = db.Column(db.String(10), default=0, nullable=False)
    sh_20inning = db.Column(db.String(10), default=0, nullable=False)
    sa_21inning = db.Column(db.String(10), default=0, nullable=False)
    sh_21inning = db.Column(db.String(10), default=0, nullable=False)
    sa_22inning = db.Column(db.String(10), default=0, nullable=False)
    sh_22inning = db.Column(db.String(10), default=0, nullable=False)
    sa_23inning = db.Column(db.String(10), default=0, nullable=False)
    sh_23inning = db.Column(db.String(10), default=0, nullable=False)
    sa_24inning = db.Column(db.String(10), default=0, nullable=False)
    sh_24inning = db.Column(db.String(10), default=0, nullable=False)
    sa_25inning = db.Column(db.String(10), default=0, nullable=False)
    sh_25inning = db.Column(db.String(10), default=0, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,
            "casino": self.casino,
            "away": self.away,
            "pitcher_a": self.pitcher_a,
            "home": self.home,
            "pitcher_h": self.pitcher_h,
            "rl_away": self.rl_away,
            "rl_home": self.rl_home,
            "juice_rl_away": self.juice_rl_away,
            "juice_rl_home": self.juice_rl_home,
            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,
            "total": self.total,
            "tt_away": self.tt_away,
            "tt_home": self.tt_home,
            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,
            "juice_total_over_f5": self.juice_total_over_f5,
            "juice_total_under_f5": self.juice_total_under_f5,
            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,
            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,
            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,
            "rl_away_f5": self.rl_away_f5,
            "rl_home_f5": self.rl_home_f5,
            "juice_rl_away_f5": self.juice_rl_away_f5,
            "juice_rl_home_f5": self.juice_rl_home_f5,
            "moneyLineHome_f5": self.moneyLineHome_f5,
            "moneyLineAway_f5": self.moneyLineAway_f5,
            "total_f5": self.total_f5,
            "juice_total_over_f5": self.juice_total_over_f5,
            "juice_total_under_f5": self.juice_total_under_f5,
            "tt_away_f5": self.tt_away_f5,
            "tt_home_f5": self.tt_home_f5,
            "juice_over_away_f5": self.juice_over_away_f5,
            "juice_over_home_f5": self.juice_over_home_f5,
            "juice_under_away_f5": self.juice_under_away_f5,
            "juice_under_home_f5": self.juice_under_home_f5,
            "fs_away_f5": self.fs_away_f5,
            "fs_home_f5": self.fs_home_f5,
            "sa_1inning": self.sa_1inning,
            "sh_1inning": self.sh_1inning,
            "sa_2inning": self.sa_2inning,
            "sh_2inning": self.sh_2inning,
            "sa_3inning": self.sa_3inning,
            "sh_3inning": self.sh_3inning,
            "sa_4inning": self.sa_4inning,
            "sh_4inning": self.sh_4inning,
            "sa_5inning": self.sa_5inning,
            "sh_5inning": self.sh_5inning,
            "sa_6inning": self.sa_6inning,
            "sh_6inning": self.sh_6inning,
            "sa_7inning": self.sa_7inning,
            "sh_7inning": self.sh_7inning,
            "sa_8inning": self.sa_8inning,
            "sh_8inning": self.sh_8inning,
            "sa_9inning": self.sa_9inning,
            "sh_9inning": self.sh_9inning,
            "sa_10inning": self.sa_10inning,
            "sh_10inning": self.sh_10inning,
            "sa_11inning": self.sa_11inning,
            "sh_11inning": self.sh_11inning,
            "sa_12inning": self.sa_12inning,
            "sh_12inning": self.sh_12inning,
            "sa_13inning": self.sa_13inning,
            "sh_13inning": self.sh_13inning,
            "sa_14inning": self.sa_14inning,
            "sh_14inning": self.sh_14inning,
            "sa_15inning": self.sa_15inning,
            "sh_15inning": self.sh_15inning,
            "sa_16inning": self.sa_16inning,
            "sh_16inning": self.sh_16inning,
            "sa_17inning": self.sa_17inning,
            "sh_17inning": self.sh_17inning,
            "sa_18inning": self.sa_18inning,
            "sh_18inning": self.sh_18inning,
            "sa_19inning": self.sa_19inning,
            "sh_19inning": self.sh_19inning,
            "sa_20inning": self.sa_20inning,
            "sh_20inning": self.sh_20inning,
            "sa_21inning": self.sa_21inning,
            "sh_21inning": self.sh_21inning,
            "sa_22inning": self.sa_22inning,
            "sh_22inning": self.sh_22inning,
            "sa_23inning": self.sa_23inning,
            "sh_23inning": self.sh_23inning,
            "sa_24inning": self.sa_24inning,
            "sh_24inning": self.sh_24inning,
            "sa_25inning": self.sa_24inning,
            "sh_25inning": self.sh_25inning,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Ncaa_Baseball(db.Model):
    __tablename__ = "ncaa_baseball"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    hour = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    casino = db.Column(db.String(20), nullable=False)
    rotation_home = db.Column(db.String(10), nullable=False)
    rotation_away = db.Column(db.String(10), nullable=False)
    away = db.Column(db.String(30), nullable=False)
    pitcher_a = db.Column(db.String(30), nullable=False)
    home = db.Column(db.String(30), nullable=False)
    pitcher_h = db.Column(db.String(30), nullable=False)
    rl_away = db.Column(db.String(10), nullable=False)
    rl_home = db.Column(db.String(10), nullable=False)
    juice_rl_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_rl_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)
    # ------------------------------------------------------------------------
    rl_away_f5 = db.Column(db.String(10), default=0, nullable=False)
    rl_home_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_rl_away_f5 = db.Column(db.String(10), default=-110, nullable=False)
    juice_rl_home_f5 = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway_f5 = db.Column(db.String(10), default=0, nullable=False)
    moneyLineHome_f5 = db.Column(db.String(10), default=0, nullable=False)
    total_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_total_over_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    juice_total_under_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    tt_away_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_over_away_f5 = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    tt_home_f5 = db.Column(db.String(10), default=0, nullable=False)
    juice_over_home_f5 = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home_f5 = db.Column(
        db.String(10), default=-110, nullable=False)
    fs_away_f5 = db.Column(db.String(10), default=0, nullable=False)
    fs_home_f5 = db.Column(db.String(10), default=0, nullable=False)
    # ----------------------------------------------------------------------
    sa_1inning = db.Column(db.String(10), default=0, nullable=False)
    sh_1inning = db.Column(db.String(10), default=0, nullable=False)
    sa_2inning = db.Column(db.String(10), default=0, nullable=False)
    sh_2inning = db.Column(db.String(10), default=0, nullable=False)
    sa_3inning = db.Column(db.String(10), default=0, nullable=False)
    sh_3inning = db.Column(db.String(10), default=0, nullable=False)
    sa_4inning = db.Column(db.String(10), default=0, nullable=False)
    sh_4inning = db.Column(db.String(10), default=0, nullable=False)
    sa_5inning = db.Column(db.String(10), default=0, nullable=False)
    sh_5inning = db.Column(db.String(10), default=0, nullable=False)
    sa_6inning = db.Column(db.String(10), default=0, nullable=False)
    sh_6inning = db.Column(db.String(10), default=0, nullable=False)
    sa_7inning = db.Column(db.String(10), default=0, nullable=False)
    sh_7inning = db.Column(db.String(10), default=0, nullable=False)
    sa_8inning = db.Column(db.String(10), default=0, nullable=False)
    sh_8inning = db.Column(db.String(10), default=0, nullable=False)
    sa_9inning = db.Column(db.String(10), default=0, nullable=False)
    sh_9inning = db.Column(db.String(10), default=0, nullable=False)
    sa_10inning = db.Column(db.String(10), default=0, nullable=False)
    sh_10inning = db.Column(db.String(10), default=0, nullable=False)
    sa_11inning = db.Column(db.String(10), default=0, nullable=False)
    sh_11inning = db.Column(db.String(10), default=0, nullable=False)
    sa_12inning = db.Column(db.String(10), default=0, nullable=False)
    sh_12inning = db.Column(db.String(10), default=0, nullable=False)
    sa_13inning = db.Column(db.String(10), default=0, nullable=False)
    sh_13inning = db.Column(db.String(10), default=0, nullable=False)
    sa_14inning = db.Column(db.String(10), default=0, nullable=False)
    sh_14inning = db.Column(db.String(10), default=0, nullable=False)
    sa_15inning = db.Column(db.String(10), default=0, nullable=False)
    sh_15inning = db.Column(db.String(10), default=0, nullable=False)
    sa_16inning = db.Column(db.String(10), default=0, nullable=False)
    sh_16inning = db.Column(db.String(10), default=0, nullable=False)
    sa_17inning = db.Column(db.String(10), default=0, nullable=False)
    sh_17inning = db.Column(db.String(10), default=0, nullable=False)
    sa_18inning = db.Column(db.String(10), default=0, nullable=False)
    sh_18inning = db.Column(db.String(10), default=0, nullable=False)
    sa_19inning = db.Column(db.String(10), default=0, nullable=False)
    sh_19inning = db.Column(db.String(10), default=0, nullable=False)
    sa_20inning = db.Column(db.String(10), default=0, nullable=False)
    sh_20inning = db.Column(db.String(10), default=0, nullable=False)
    sa_21inning = db.Column(db.String(10), default=0, nullable=False)
    sh_21inning = db.Column(db.String(10), default=0, nullable=False)
    sa_22inning = db.Column(db.String(10), default=0, nullable=False)
    sh_22inning = db.Column(db.String(10), default=0, nullable=False)
    sa_23inning = db.Column(db.String(10), default=0, nullable=False)
    sh_23inning = db.Column(db.String(10), default=0, nullable=False)
    sa_24inning = db.Column(db.String(10), default=0, nullable=False)
    sh_24inning = db.Column(db.String(10), default=0, nullable=False)
    sa_25inning = db.Column(db.String(10), default=0, nullable=False)
    sh_25inning = db.Column(db.String(10), default=0, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,
            "casino": self.casino,
            "away": self.away,
            "pitcher_a": self.pitcher_a,
            "home": self.home,
            "pitcher_h": self.pitcher_h,
            "rl_away": self.rl_away,
            "rl_home": self.rl_home,
            "juice_rl_away": self.juice_rl_away,
            "juice_rl_home": self.juice_rl_home,
            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,
            "total": self.total,
            "tt_away": self.tt_away,
            "tt_home": self.tt_home,
            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,
            "juice_total_over_f5": self.juice_total_over_f5,
            "juice_total_under_f5": self.juice_total_under_f5,
            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,
            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,
            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,
            "rl_away_f5": self.rl_away_f5,
            "rl_home_f5": self.rl_home_f5,
            "juice_rl_away_f5": self.juice_rl_away_f5,
            "juice_rl_home_f5": self.juice_rl_home_f5,
            "moneyLineHome_f5": self.moneyLineHome_f5,
            "moneyLineAway_f5": self.moneyLineAway_f5,
            "total_f5": self.total_f5,
            "juice_total_over_f5": self.juice_total_over_f5,
            "juice_total_under_f5": self.juice_total_under_f5,
            "tt_away_f5": self.tt_away_f5,
            "tt_home_f5": self.tt_home_f5,
            "juice_over_away_f5": self.juice_over_away_f5,
            "juice_over_home_f5": self.juice_over_home_f5,
            "juice_under_away_f5": self.juice_under_away_f5,
            "juice_under_home_f5": self.juice_under_home_f5,
            "fs_away_f5": self.fs_away_f5,
            "fs_home_f5": self.fs_home_f5,
            "sa_1inning": self.sa_1inning,
            "sh_1inning": self.sh_1inning,
            "sa_2inning": self.sa_2inning,
            "sh_2inning": self.sh_2inning,
            "sa_3inning": self.sa_3inning,
            "sh_3inning": self.sh_3inning,
            "sa_4inning": self.sa_4inning,
            "sh_4inning": self.sh_4inning,
            "sa_5inning": self.sa_5inning,
            "sh_5inning": self.sh_5inning,
            "sa_6inning": self.sa_6inning,
            "sh_6inning": self.sh_6inning,
            "sa_7inning": self.sa_7inning,
            "sh_7inning": self.sh_7inning,
            "sa_8inning": self.sa_8inning,
            "sh_8inning": self.sh_8inning,
            "sa_9inning": self.sa_9inning,
            "sh_9inning": self.sh_9inning,
            "sa_10inning": self.sa_10inning,
            "sh_10inning": self.sh_10inning,
            "sa_11inning": self.sa_11inning,
            "sh_11inning": self.sh_11inning,
            "sa_12inning": self.sa_12inning,
            "sh_12inning": self.sh_12inning,
            "sa_13inning": self.sa_13inning,
            "sh_13inning": self.sh_13inning,
            "sa_14inning": self.sa_14inning,
            "sh_14inning": self.sh_14inning,
            "sa_15inning": self.sa_15inning,
            "sh_15inning": self.sh_15inning,
            "sa_16inning": self.sa_16inning,
            "sh_16inning": self.sh_16inning,
            "sa_17inning": self.sa_17inning,
            "sh_17inning": self.sh_17inning,
            "sa_18inning": self.sa_18inning,
            "sh_18inning": self.sh_18inning,
            "sa_19inning": self.sa_19inning,
            "sh_19inning": self.sh_19inning,
            "sa_20inning": self.sa_20inning,
            "sh_20inning": self.sh_20inning,
            "sa_21inning": self.sa_21inning,
            "sh_21inning": self.sh_21inning,
            "sa_22inning": self.sa_22inning,
            "sh_22inning": self.sh_22inning,
            "sa_23inning": self.sa_23inning,
            "sh_23inning": self.sh_23inning,
            "sa_24inning": self.sa_24inning,
            "sh_24inning": self.sh_24inning,
            "sa_25inning": self.sa_24inning,
            "sh_25inning": self.sh_25inning,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Stats_ncaa_baseball_team(db.Model):
    __tablename__ = "stats_ncaa_baseball_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(20), nullable=False)
    league = db.Column(db.String(20), nullable=False)
    division = db.Column(db.String(20), nullable=False)
    w = db.Column(db.String(10), default=0, nullable=False)
    L = db.Column(db.String(10), default=0, nullable=False)
    pct = db.Column(db.String(10), default=0, nullable=False)
    gb = db.Column(db.String(10), default=0, nullable=False)
    home = db.Column(db.String(10), default=0, nullable=False)
    away = db.Column(db.String(10), default=0, nullable=False)
    rs = db.Column(db.String(10), default=0, nullable=False)
    ra = db.Column(db.String(10), default=0, nullable=False)
    diff = db.Column(db.String(10), default=0, nullable=False)
    strk = db.Column(db.String(10), default=0, nullable=False)
    L10 = db.Column(db.String(10), default=-0, nullable=False)
    poff = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "team": self.team,
            "league": self.league,
            "division": self.division,
            "w": self.w,
            "L": self.L,
            "pct": self.pct,
            "gb": self.gb,
            "home": self.home,
            "away": self.away,
            "rs": self.rs,
            "ra": self.ra,
            "diff": self.diff,
            "strk": self.strk,
            "L10": self.L10,
            "poff": self.poff
            # do not serialize the password, its a security breach
        }


class Stats_ncaa_baseball_player(db.Model):
    __tablename__ = "stats_ncaa_baseball_player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(20), nullable=False)
    dorsal = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    gp = db.Column(db.String(20), nullable=False)
    ab = db.Column(db.String(10), default=0, nullable=False)
    r = db.Column(db.String(10), default=0, nullable=False)
    h = db.Column(db.String(10), default=0, nullable=False)
    two_b = db.Column(db.String(10), default=0, nullable=False)
    three_b = db.Column(db.String(10), default=0, nullable=False)
    hb = db.Column(db.String(10), default=0, nullable=False)
    rbi = db.Column(db.String(10), default=0, nullable=False)
    tb = db.Column(db.String(10), default=0, nullable=False)
    bb = db.Column(db.String(10), default=0, nullable=False)
    so = db.Column(db.String(10), default=0, nullable=False)
    sb = db.Column(db.String(10), default=-0, nullable=False)
    avg = db.Column(db.String(10), default=0, nullable=False)
    obp = db.Column(db.String(10), default=0, nullable=False)
    slg = db.Column(db.String(10), default=0, nullable=False)
    ops = db.Column(db.String(10), default=0, nullable=False)
    war = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "season": self.season,
            "team": self.team,
            "dorsal": self.dorsal,
            "position": self.position,
            "headshot": self.headshot,
            "gp": self.gp,
            "ab": self.ab,
            "r": self.r,
            "h": self.h,
            "two_b": self.two_b,
            "three_b": self.three_b,
            "hb": self.hb,
            "rbi": self.rbi,
            "tb": self.tb,
            "bb": self.bb,
            "so": self.so,
            "sb": self.sb,
            "avg": self.avg,
            "obp": self.obp,
            "slg": self.slg,
            "ops": self.ops,
            "war": self.war
            # do not serialize the password, its a security breach
        }


class Nfl(db.Model):
    __tablename__ = "nfl"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(20), nullable=False)
    rotation_home = db.Column(db.String(10), nullable=False)
    rotation_away = db.Column(db.String(10), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    home = db.Column(db.String(50), nullable=False)
    spread_away = db.Column(db.String(10), nullable=False)
    spread_home = db.Column(db.String(10), nullable=False)
    juice_spread_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_spread_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)
# ----------
    first_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_total = db.Column(db.String(10), default=0, nullable=False)
    fh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    fh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    second_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_total = db.Column(db.String(10), default=0, nullable=False)
    sh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    sh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    q1_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q1_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q1_half_total = db.Column(db.String(10), default=0, nullable=False)
    q1_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q1_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q1_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q1_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q2_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q2_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q2_half_total = db.Column(db.String(10), default=0, nullable=False)
    q2_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q2_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q2_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q2_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q3_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q3_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q3_half_total = db.Column(db.String(10), default=0, nullable=False)
    q3_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q3_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q3_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q3_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q4_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q4_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q4_half_total = db.Column(db.String(10), default=0, nullable=False)
    q4_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q4_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q4_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q4_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "hour": self.hour,
            "week": self.week,
            "status": self.status,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,
            "casino": self.casino,
            "away": self.away,
            "home": self.home,
            "spread_away": self.spread_away,
            "spread_home": self.spread_home,
            "juice_spread_away": self.juice_spread_away,
            "juice_spread_home": self.juice_spread_home,
            "moneyLineAway": self.moneyLineAway,
            "moneyLineHome": self.moneyLineHome,
            "total": self.total,
            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,
            "tt_away": self.tt_away,
            "juice_over_away": self.juice_over_away,
            "juice_under_away": self.juice_under_away,
            "tt_home": self.tt_home,
            "juice_over_home": self.juice_over_home,
            "juice_under_home": self.juice_under_home,
            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "first_half_spread_away": self.first_half_spread_away,
            "first_half_spread_home": self.first_half_spread_home,
            "first_half_juice_spread_away": self.first_half_juice_spread_away,
            "first_half_juice_spread_home": self.first_half_juice_spread_home,
            "first_half_moneyLineAway": self.first_half_moneyLineAway,
            "first_half_moneyLineHome": self.first_half_moneyLineHome,
            "first_half_total": self.first_half_total,
            "fh_juice_total_over": self.fh_juice_total_over,
            "fh_juice_total_under": self.fh_juice_total_under,
            "first_half_tt_away": self.first_half_tt_away,
            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_tt_home": self.first_half_tt_home,
            "first_half_juice_over_home": self.first_half_juice_over_home,
            "first_half_juice_under_home": self.first_half_juice_under_home,
            "first_half_final_score_away": self.first_half_final_score_away,
            "first_half_final_score_home": self.first_half_final_score_home,

            "second_half_spread_away": self.second_half_spread_away,
            "second_half_spread_home": self.second_half_spread_home,
            "second_half_juice_spread_away": self.second_half_juice_spread_away,
            "second_half_juice_spread_home": self.second_half_juice_spread_home,
            "second_half_moneyLineAway": self.second_half_moneyLineAway,
            "second_half_moneyLineHome": self.second_half_moneyLineHome,
            "second_half_total": self.second_half_total,
            "sh_juice_total_over": self.sh_juice_total_over,
            "sh_juice_total_under": self.sh_juice_total_under,
            "second_half_tt_away": self.second_half_tt_away,
            "second_half_juice_over_away": self.second_half_juice_over_away,
            "second_half_juice_under_away": self.second_half_juice_under_away,
            "second_half_tt_home": self.second_half_tt_home,
            "second_half_juice_over_home": self.second_half_juice_over_home,
            "second_half_juice_under_home": self.second_half_juice_under_home,
            "second_half_final_score_away": self.second_half_final_score_away,
            "second_half_final_score_home": self.second_half_final_score_home,

            "q1_half_spread_away": self.q1_half_spread_away,
            "q1_half_spread_home": self.q1_half_spread_home,
            "q1_half_juice_spread_away": self.q1_half_juice_spread_away,
            "q1_half_juice_spread_home": self.q1_half_juice_spread_home,
            "q1_half_moneyLineAway": self.q1_half_moneyLineAway,
            "q1_half_moneyLineHome": self.q1_half_moneyLineHome,
            "q1_half_total": self.q1_half_total,
            "q1_juice_over": self.q1_juice_over,
            "q1_juice_under": self.q1_juice_under,
            "q1_half_tt_away": self.q1_half_tt_away,
            "q1_half_juice_over_away": self.q1_half_juice_over_away,
            "q1_half_juice_under_away": self.q1_half_juice_under_away,
            "q1_half_tt_home": self.q1_half_tt_home,
            "q1_half_juice_over_home": self.q1_half_juice_over_home,
            "q1_half_juice_under_home": self.q1_half_juice_under_home,
            "q1_half_final_score_away": self.q1_half_final_score_away,
            "q1_half_final_score_home": self.q1_half_final_score_home,

            "q2_half_spread_away": self.q2_half_spread_away,
            "q2_half_spread_home": self.q2_half_spread_home,
            "q2_half_juice_spread_away": self.q2_half_juice_spread_away,
            "q2_half_juice_spread_home": self.q2_half_juice_spread_home,
            "q2_half_moneyLineAway": self.q2_half_moneyLineAway,
            "q2_half_moneyLineHome": self.q2_half_moneyLineHome,
            "q2_half_total": self.q2_half_total,
            "q2_juice_over": self.q2_juice_over,
            "q2_juice_under": self.q2_juice_under,
            "q2_half_tt_away": self.q2_half_tt_away,
            "q2_half_juice_over_away": self.q2_half_juice_over_away,
            "q2_half_juice_under_away": self.q2_half_juice_under_away,
            "q2_half_tt_home": self.q2_half_tt_home,
            "q2_half_juice_over_home": self.q2_half_juice_over_home,
            "q2_half_juice_under_home": self.q2_half_juice_under_home,
            "q2_half_final_score_away": self.q2_half_final_score_away,
            "q2_half_final_score_home": self.q2_half_final_score_home,

            "q3_half_spread_away": self.q3_half_spread_away,
            "q3_half_spread_home": self.q3_half_spread_home,
            "q3_half_juice_spread_away": self.q3_half_juice_spread_away,
            "q3_half_juice_spread_home": self.q3_half_juice_spread_home,
            "q3_half_moneyLineAway": self.q3_half_moneyLineAway,
            "q3_half_moneyLineHome": self.q3_half_moneyLineHome,
            "q3_half_total": self.q3_half_total,
            "q3_juice_over": self.q3_juice_over,
            "q3_juice_under": self.q3_juice_under,
            "q3_half_tt_away": self.q3_half_tt_away,
            "q3_half_juice_over_away": self.q3_half_juice_over_away,
            "q3_half_juice_under_away": self.q3_half_juice_under_away,
            "q3_half_tt_home": self.q3_half_tt_home,
            "q3_half_juice_over_home": self.q3_half_juice_over_home,
            "q3_half_juice_under_home": self.q3_half_juice_under_home,
            "q3_half_final_score_away": self.q3_half_final_score_away,
            "q3_half_final_score_home": self.q3_half_final_score_home,

            "q4_half_spread_away": self.q4_half_spread_away,
            "q4_half_spread_home": self.q4_half_spread_home,
            "q4_half_juice_spread_away": self.q4_half_juice_spread_away,
            "q4_half_juice_spread_home": self.q4_half_juice_spread_home,
            "q4_half_moneyLineAway": self.q4_half_moneyLineAway,
            "q4_half_moneyLineHome": self.q4_half_moneyLineHome,
            "q4_half_total": self.q4_half_total,
            "q4_juice_over": self.q4_juice_over,
            "q4_juice_under": self.q4_juice_under,
            "q4_half_tt_away": self.q4_half_tt_away,
            "q4_half_juice_over_away": self.q4_half_juice_over_away,
            "q4_half_juice_under_away": self.q4_half_juice_under_away,
            "q4_half_tt_home": self.q4_half_tt_home,
            "q4_half_juice_over_home": self.q4_half_juice_over_home,
            "q4_half_juice_under_home": self.q4_half_juice_under_home,
            "q4_half_final_score_away": self.q4_half_final_score_away,
            "q4_half_final_score_home": self.q4_half_final_score_home,
            # do not serialize the password, its a security breach
        }


class Ncaa_Football(db.Model):
    __tablename__ = "ncaa_football"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(20), nullable=False)
    rotation_home = db.Column(db.String(10), nullable=False)
    rotation_away = db.Column(db.String(10), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    home = db.Column(db.String(50), nullable=False)
    spread_away = db.Column(db.String(10), nullable=False)
    spread_home = db.Column(db.String(10), nullable=False)
    juice_spread_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_spread_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)
# ----------
    first_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_total = db.Column(db.String(10), default=0, nullable=False)
    fh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    fh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    second_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_total = db.Column(db.String(10), default=0, nullable=False)
    sh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    sh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    q1_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q1_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q1_half_total = db.Column(db.String(10), default=0, nullable=False)
    q1_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q1_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q1_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q1_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q2_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q2_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q2_half_total = db.Column(db.String(10), default=0, nullable=False)
    q2_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q2_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q2_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q2_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q3_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q3_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q3_half_total = db.Column(db.String(10), default=0, nullable=False)
    q3_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q3_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q3_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q3_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q4_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q4_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q4_half_total = db.Column(db.String(10), default=0, nullable=False)
    q4_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q4_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q4_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q4_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "hour": self.hour,
            "week": self.week,
            "status": self.status,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,
            "casino": self.casino,
            "away": self.away,
            "home": self.home,
            "spread_away": self.spread_away,
            "spread_home": self.spread_home,
            "juice_spread_away": self.juice_spread_away,
            "juice_spread_home": self.juice_spread_home,
            "moneyLineAway": self.moneyLineAway,
            "moneyLineHome": self.moneyLineHome,
            "total": self.total,
            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,
            "tt_away": self.tt_away,
            "juice_over_away": self.juice_over_away,
            "juice_under_away": self.juice_under_away,
            "tt_home": self.tt_home,
            "juice_over_home": self.juice_over_home,
            "juice_under_home": self.juice_under_home,
            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "first_half_spread_away": self.first_half_spread_away,
            "first_half_spread_home": self.first_half_spread_home,
            "first_half_juice_spread_away": self.first_half_juice_spread_away,
            "first_half_juice_spread_home": self.first_half_juice_spread_home,
            "first_half_moneyLineAway": self.first_half_moneyLineAway,
            "first_half_moneyLineHome": self.first_half_moneyLineHome,
            "first_half_total": self.first_half_total,
            "fh_juice_total_over": self.fh_juice_total_over,
            "fh_juice_total_under": self.fh_juice_total_under,
            "first_half_tt_away": self.first_half_tt_away,
            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_tt_home": self.first_half_tt_home,
            "first_half_juice_over_home": self.first_half_juice_over_home,
            "first_half_juice_under_home": self.first_half_juice_under_home,
            "first_half_final_score_away": self.first_half_final_score_away,
            "first_half_final_score_home": self.first_half_final_score_home,

            "second_half_spread_away": self.second_half_spread_away,
            "second_half_spread_home": self.second_half_spread_home,
            "second_half_juice_spread_away": self.second_half_juice_spread_away,
            "second_half_juice_spread_home": self.second_half_juice_spread_home,
            "second_half_moneyLineAway": self.second_half_moneyLineAway,
            "second_half_moneyLineHome": self.second_half_moneyLineHome,
            "second_half_total": self.second_half_total,
            "sh_juice_total_over": self.sh_juice_total_over,
            "sh_juice_total_under": self.sh_juice_total_under,
            "second_half_tt_away": self.second_half_tt_away,
            "second_half_juice_over_away": self.second_half_juice_over_away,
            "second_half_juice_under_away": self.second_half_juice_under_away,
            "second_half_tt_home": self.second_half_tt_home,
            "second_half_juice_over_home": self.second_half_juice_over_home,
            "second_half_juice_under_home": self.second_half_juice_under_home,
            "second_half_final_score_away": self.second_half_final_score_away,
            "second_half_final_score_home": self.second_half_final_score_home,

            "q1_half_spread_away": self.q1_half_spread_away,
            "q1_half_spread_home": self.q1_half_spread_home,
            "q1_half_juice_spread_away": self.q1_half_juice_spread_away,
            "q1_half_juice_spread_home": self.q1_half_juice_spread_home,
            "q1_half_moneyLineAway": self.q1_half_moneyLineAway,
            "q1_half_moneyLineHome": self.q1_half_moneyLineHome,
            "q1_half_total": self.q1_half_total,
            "q1_juice_over": self.q1_juice_over,
            "q1_juice_under": self.q1_juice_under,
            "q1_half_tt_away": self.q1_half_tt_away,
            "q1_half_juice_over_away": self.q1_half_juice_over_away,
            "q1_half_juice_under_away": self.q1_half_juice_under_away,
            "q1_half_tt_home": self.q1_half_tt_home,
            "q1_half_juice_over_home": self.q1_half_juice_over_home,
            "q1_half_juice_under_home": self.q1_half_juice_under_home,
            "q1_half_final_score_away": self.q1_half_final_score_away,
            "q1_half_final_score_home": self.q1_half_final_score_home,

            "q2_half_spread_away": self.q2_half_spread_away,
            "q2_half_spread_home": self.q2_half_spread_home,
            "q2_half_juice_spread_away": self.q2_half_juice_spread_away,
            "q2_half_juice_spread_home": self.q2_half_juice_spread_home,
            "q2_half_moneyLineAway": self.q2_half_moneyLineAway,
            "q2_half_moneyLineHome": self.q2_half_moneyLineHome,
            "q2_half_total": self.q2_half_total,
            "q2_juice_over": self.q2_juice_over,
            "q2_juice_under": self.q2_juice_under,
            "q2_half_tt_away": self.q2_half_tt_away,
            "q2_half_juice_over_away": self.q2_half_juice_over_away,
            "q2_half_juice_under_away": self.q2_half_juice_under_away,
            "q2_half_tt_home": self.q2_half_tt_home,
            "q2_half_juice_over_home": self.q2_half_juice_over_home,
            "q2_half_juice_under_home": self.q2_half_juice_under_home,
            "q2_half_final_score_away": self.q2_half_final_score_away,
            "q2_half_final_score_home": self.q2_half_final_score_home,

            "q3_half_spread_away": self.q3_half_spread_away,
            "q3_half_spread_home": self.q3_half_spread_home,
            "q3_half_juice_spread_away": self.q3_half_juice_spread_away,
            "q3_half_juice_spread_home": self.q3_half_juice_spread_home,
            "q3_half_moneyLineAway": self.q3_half_moneyLineAway,
            "q3_half_moneyLineHome": self.q3_half_moneyLineHome,
            "q3_half_total": self.q3_half_total,
            "q3_juice_over": self.q3_juice_over,
            "q3_juice_under": self.q3_juice_under,
            "q3_half_tt_away": self.q3_half_tt_away,
            "q3_half_juice_over_away": self.q3_half_juice_over_away,
            "q3_half_juice_under_away": self.q3_half_juice_under_away,
            "q3_half_tt_home": self.q3_half_tt_home,
            "q3_half_juice_over_home": self.q3_half_juice_over_home,
            "q3_half_juice_under_home": self.q3_half_juice_under_home,
            "q3_half_final_score_away": self.q3_half_final_score_away,
            "q3_half_final_score_home": self.q3_half_final_score_home,

            "q4_half_spread_away": self.q4_half_spread_away,
            "q4_half_spread_home": self.q4_half_spread_home,
            "q4_half_juice_spread_away": self.q4_half_juice_spread_away,
            "q4_half_juice_spread_home": self.q4_half_juice_spread_home,
            "q4_half_moneyLineAway": self.q4_half_moneyLineAway,
            "q4_half_moneyLineHome": self.q4_half_moneyLineHome,
            "q4_half_total": self.q4_half_total,
            "q4_juice_over": self.q4_juice_over,
            "q4_juice_under": self.q4_juice_under,
            "q4_half_tt_away": self.q4_half_tt_away,
            "q4_half_juice_over_away": self.q4_half_juice_over_away,
            "q4_half_juice_under_away": self.q4_half_juice_under_away,
            "q4_half_tt_home": self.q4_half_tt_home,
            "q4_half_juice_over_home": self.q4_half_juice_over_home,
            "q4_half_juice_under_home": self.q4_half_juice_under_home,
            "q4_half_final_score_away": self.q4_half_final_score_away,
            "q4_half_final_score_home": self.q4_half_final_score_home,
            # do not serialize the password, its a security breach
        }


class Stats_ncaa_football_team(db.Model):
    __tablename__ = "stats_ncaa_football_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    conference = db.Column(db.String(30), nullable=False)
    division = db.Column(db.String(30), nullable=False)
    TP = db.Column(db.String(10), nullable=False)
    ttpg = db.Column(db.String(10), nullable=False)
    t_td = db.Column(db.String(10), nullable=False)
    t_1_down = db.Column(db.String(10), nullable=False)
    Russ_1_d = db.Column(db.String(10), nullable=False)
    pass_1_d = db.Column(db.String(10), nullable=False)
    down_1_penal = db.Column(db.String(10), nullable=False)
    down_3_eff = db.Column(db.String(10), nullable=False)
    down_3_AVG = db.Column(db.String(10), nullable=False)
    down_4_eff = db.Column(db.String(10), nullable=False)
    down_4_AVG = db.Column(db.String(10), nullable=False)
    comp_att = db.Column(db.String(10), nullable=False)
    net_pass_y = db.Column(db.String(10), nullable=False)
    y_p_pas_attps = db.Column(db.String(10), nullable=False)
    net_pass_y_pg = db.Column(db.String(10), nullable=False)
    pass_td = db.Column(db.String(10), nullable=False)
    interceptions = db.Column(db.String(10), nullable=False)
    sacks_y_lost = db.Column(db.String(10), nullable=False)
    russ_attps = db.Column(db.String(10), nullable=False)
    russ_y = db.Column(db.String(10), nullable=False)
    y_p_russ_attp = db.Column(db.String(10), nullable=False)
    russ_y_pg = db.Column(db.String(10), nullable=False)
    russ_td = db.Column(db.String(10), nullable=False)
    total_of_plays = db.Column(db.String(10), nullable=False)
    total_y = db.Column(db.String(10), nullable=False)
    y_pg = db.Column(db.String(10), nullable=False)
    kickoffs_t = db.Column(db.String(10), nullable=False)
    AVG_kickoff_return_y = db.Column(db.String(10), nullable=False)
    punt_t = db.Column(db.String(10), nullable=False)
    AVG_punt_ruturn_y = db.Column(db.String(10), nullable=False)
    int_t = db.Column(db.String(10), nullable=False)
    AVG_intercept_y = db.Column(db.String(10), nullable=False)
    net_AVG_punt_y = db.Column(db.String(10), nullable=False)
    punt_ty = db.Column(db.String(10), nullable=False)
    fg_goog_attps = db.Column(db.String(10), nullable=False)
    touchback_percent = db.Column(db.String(10), nullable=False)
    penal_ty = db.Column(db.String(10), nullable=False)
    penal_y_AVG_pg = db.Column(db.String(10), nullable=False)
    possesion_time = db.Column(db.String(10), nullable=False)
    fumbles_lost = db.Column(db.String(10), nullable=False)
    turnover_ratio = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "team": self.team,
            "conference": self.conference,
            "division": self.division,
            "TP": self.TP,
            "ttpg": self.ttpg,
            "t_td": self.t_td,
            "t_1_down": self.t_1_down,
            "Russ_1_d": self.Russ_1_d,
            "pass_1_d": self.pass_1_d,
            "down_1_penal": self.down_1_penal,
            "down_3_eff": self.down_3_eff,
            "down_3_AVG": self.down_3_AVG,
            "down_4_eff": self.down_4_eff,
            "down_4_AVG": self.down_4_AVG,
            "comp_att": self.comp_att,
            "net_pass_y": self.net_pass_y,
            "y_p_pas_attps": self.y_p_pas_attps,
            "net_pass_y_pg": self.net_pass_y_pg,
            "pass_td": self.pass_td,
            "interceptions": self.interceptions,
            "sacks_y_lost": self.sacks_y_lost,
            "russ_attps": self.russ_attps,
            "russ_y": self.russ_y,
            "y_p_russ_attp": self.y_p_russ_attp,
            "russ_y_pg": self.russ_y_pg,
            "russ_td": self.russ_td,
            "total_of_plays": self.total_of_plays,
            "total_y": self.total_y,
            "y_pg": self.y_pg,
            "kickoffs_t": self.kickoffs_t,
            "AVG_kickoff_return_y": self.AVG_kickoff_return_y,
            "punt_t": self.punt_t,
            "AVG_punt_ruturn_y": self.AVG_punt_ruturn_y,
            "int_t": self.int_t,
            "AVG_intercept_y": self.AVG_intercept_y,
            "net_AVG_punt_y": self.net_AVG_punt_y,
            "punt_ty": self.punt_ty,
            "fg_goog_attps": self.fg_goog_attps,
            "touchback_percent": self.touchback_percent,
            "penal_ty": self.penal_ty,
            "penal_y_AVG_pg": self.penal_y_AVG_pg,
            "possesion_time": self.possesion_time,
            "fumbles_lost": self.fumbles_lost,
            "turnover_ratio": self.turnover_ratio
            # do not serialize the password, its a security breach
        }


class Stats_defensive_player_ncca_football(db.Model):
    __tablename__ = "stats_defensive_player_ncca_football"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    tack_solo = db.Column(db.String(10), nullable=False)
    tack_ast = db.Column(db.String(10), nullable=False)

    tack_total = db.Column(db.String(10), nullable=False)
    sacks = db.Column(db.String(10), nullable=False)
    sacks_yards = db.Column(db.String(10), nullable=False)
    tfl = db.Column(db.String(10), nullable=False)
    pd = db.Column(db.String(10), nullable=False)
    Int = db.Column(db.String(10), nullable=False)
    yds = db.Column(db.String(10), nullable=False)
    ing = db.Column(db.String(10), nullable=False)
    td = db.Column(db.String(10), nullable=False)
    ff = db.Column(db.String(10), nullable=False)
    fr = db.Column(db.String(10), nullable=False)
    ftd = db.Column(db.String(10), nullable=False)
    kb = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "tack_solo": self.tack_solo,
            "tack_ast": self.tack_ast,
            "tack_total": self.tack_total,
            "sacks": self.sacks,
            "sacks_yards": self.sacks_yards,
            "tfl": self.tfl,
            "pd": self.pd,
            "Int": self.Int,
            "yds": self.yds,
            "ing": self.ing,
            "td": self.td,
            "ff": self.ff,
            "fr": self.fr,
            "ftd": self.ftd,
            "kb": self.kb,
            # do not serialize the password, its a security breach
        }


class Stats_offensive_player_ncaa_football(db.Model):
    __tablename__ = "Stats_offensive_player_ncaa_football"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    Cmp = db.Column(db.String(10), nullable=False)
    pass_att = db.Column(db.String(10), nullable=False)
    cmp_AVG = db.Column(db.String(10), nullable=False)
    yards = db.Column(db.String(10), nullable=False)
    yards_AVG = db.Column(db.String(10), nullable=False)
    yards_pg = db.Column(db.String(10), nullable=False)
    pass_td = db.Column(db.String(10), nullable=False)
    Int = db.Column(db.String(10), nullable=False)
    asck = db.Column(db.String(10), nullable=False)
    syl = db.Column(db.String(10), nullable=False)
    rtg = db.Column(db.String(10), nullable=False)
    russ_att = db.Column(db.String(10), nullable=False)
    russ_yards = db.Column(db.String(10), nullable=False)
    yards_p_russ = db.Column(db.String(10), nullable=False)
    big = db.Column(db.String(10), nullable=False)

    rush_tt = db.Column(db.String(10), nullable=False)
    rush_yard_pg = db.Column(db.String(10), nullable=False)
    fum = db.Column(db.String(10), nullable=False)
    lst = db.Column(db.String(10), nullable=False) 
    long_pass = db.Column(db.String(10), nullable=False) 
    fd = db.Column(db.String(10), nullable=False)
    rec = db.Column(db.String(10), nullable=False)
    r_tgts = db.Column(db.String(10), nullable=False)
    r_yards = db.Column(db.String(10), nullable=False)
    yards_p_r = db.Column(db.String(10), nullable=False)
    r_td = db.Column(db.String(10), nullable=False)
    lr = db.Column(db.String(10), nullable=False)
    r_big = db.Column(db.String(10), nullable=False)
    r_ypg = db.Column(db.String(10), nullable=False)
    r_fl = db.Column(db.String(10), nullable=False)
    r_yac = db.Column(db.String(10), nullable=False)
    r_fd = db.Column(db.String(10), nullable=False)
    pts = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "Cmp": self.Cmp,
            "pass_att": self.pass_att,
            "cmp_AVG": self.cmp_AVG,
            "yards": self.yards,
            "yards_AVG": self.yards_AVG,
            "yards_pg": self.yards_pg,
            "pass_td": self.pass_td,
            "Int": self.Int,
            "asck": self.asck,
            "syl": self.syl,
            "rtg": self.rtg,
            "russ_att": self.russ_att,
            "russ_yards": self.russ_yards,
            "yards_p_russ": self.yards_p_russ,
            "big": self.big,
            "rush_tt": self.rush_tt,
            "rush_yard_pg": self.rush_yard_pg,
            "fum": self.fum,
            "lst": self.lst,
            "long_pass": self.long_pass,
            "fd": self.fd,
            "rec": self.rec,
            "r_tgts": self.r_tgts,
            "r_yards": self.r_yards,
            "yards_p_r": self.yards_p_r,
            "r_td": self.r_td,
            "lr": self.lr,
            "r_big": self.r_big,
            "r_big": self.r_big,
            "r_ypg": self.r_ypg,
            "r_fl": self.r_fl,
            "r_yac": self.r_yac,
            "r_fd": self.r_fd,
            "pts": self.pts,
            # do not serialize the password, its a security breach
        }


class Stats_returning_player_ncaa_football(db.Model):
    __tablename__ = "stats_returning_player_ncaa_football"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    kick_returns = db.Column(db.String(10), nullable=False)
    kick_returns_yards = db.Column(db.String(10), nullable=False)
    yards_p_k_p = db.Column(db.String(10), nullable=False)
    l_k_r = db.Column(db.String(10), nullable=False)
    k_r_td = db.Column(db.String(10), nullable=False)
    punt_r = db.Column(db.String(10), nullable=False)
    punt_r_y = db.Column(db.String(10), nullable=False)
    y_ppr = db.Column(db.String(10), nullable=False)
    lpr = db.Column(db.String(10), nullable=False)
    pr_td = db.Column(db.String(10), nullable=False)
    punt_r_fair_carches = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "kick_returns": self.kick_returns,
            "kick_returns_yards": self.kick_returns_yards,
            "yards_p_k_p": self.yards_p_k_p,
            "l_k_r": self.l_k_r,
            "k_r_td": self.k_r_td,
            "punt_r": self.punt_r,
            "punt_r_y": self.punt_r_y,
            "y_ppr": self.y_ppr,
            "lpr": self.lpr,
            "pr_td": self.pr_td,
            "punt_r_fair_carches": self.punt_r_fair_carches,
            # do not serialize the password, its a security breach
        }


class Stats_kiking_player_ncaa_football(db.Model):
    __tablename__ = "stats_kiking_player_ncaa_football"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    fgm = db.Column(db.String(10), nullable=False)
    fga = db.Column(db.String(10), nullable=False)
    fg_AVG = db.Column(db.String(10), nullable=False)
    lng = db.Column(db.String(10), nullable=False)
    yars_f_goals_1_19 = db.Column(db.String(10), nullable=False)
    yars_f_goals_20_29 = db.Column(db.String(10), nullable=False)
    yars_f_goals_30_49 = db.Column(db.String(10), nullable=False)
    yars_f_goals_40_49 = db.Column(db.String(10), nullable=False)
    more_50 = db.Column(db.String(10), nullable=False)
    xpm = db.Column(db.String(10), nullable=False)
    xpa = db.Column(db.String(10), nullable=False)
    xp_AVG = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "fgm": self.fgm,
            "fga": self.fga,
            "fg_AVG": self.fg_AVG,
            "lng": self.lng,
            "yars_f_goals_1_19": self.yars_f_goals_1_19,
            "yars_f_goals_20_29": self.yars_f_goals_20_29,
            "yars_f_goals_30_49": self.yars_f_goals_30_49,
            "yars_f_goals_40_49": self.yars_f_goals_40_49,
            "more_50": self.more_50,
            "xpm": self.xpm,
            "xpa": self.xpa,
            "xp_AVG": self.xp_AVG,
            # do not serialize the password, its a security breach
        }


class Stats_punting_player_ncaa_football(db.Model):
    __tablename__ = "stats_punting_player_ncaa_football"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    punts = db.Column(db.String(10), nullable=False)
    yards = db.Column(db.String(10), nullable=False)
    lng = db.Column(db.String(10), nullable=False)
    AVG = db.Column(db.String(10), nullable=False)
    net = db.Column(db.String(10), nullable=False)
    p_blk = db.Column(db.String(10), nullable=False)
    IN_20 = db.Column(db.String(10), nullable=False)
    tb = db.Column(db.String(10), nullable=False)
    fc = db.Column(db.String(10), nullable=False)
    att = db.Column(db.String(10), nullable=False)
    punt_return_yds = db.Column(db.String(10), nullable=False)
    AVG_punt_retun_yards = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "punts": self.punts,
            "yards": self.yards,
            "AVG": self.AVG,
            "lng": self.lng,
            "net": self.net,
            "p_blk": self.p_blk,
            "IN_20": self.IN_20,
            "tb": self.tb,
            "fc": self.fc,
            "att": self.att,
            "punt_return_yds": self.punt_return_yds,
            "AVG_punt_retun_yards": self.AVG_punt_retun_yards,
            # do not serialize the password, its a security breach
        }


class Nba(db.Model):
    __tablename__ = "nba"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(20), nullable=False)
    rotation_home = db.Column(db.String(10), nullable=False)
    rotation_away = db.Column(db.String(10), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    home = db.Column(db.String(50), nullable=False)
    spread_away = db.Column(db.String(10), nullable=False)
    spread_home = db.Column(db.String(10), nullable=False)
    juice_spread_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_spread_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)
# ----------
    first_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_total = db.Column(db.String(10), default=0, nullable=False)
    fh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    fh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    second_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_total = db.Column(db.String(10), default=0, nullable=False)
    sh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    sh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    q1_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q1_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q1_half_total = db.Column(db.String(10), default=0, nullable=False)
    q1_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q1_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q1_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q1_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q2_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q2_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q2_half_total = db.Column(db.String(10), default=0, nullable=False)
    q2_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q2_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q2_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q2_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q3_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q3_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q3_half_total = db.Column(db.String(10), default=0, nullable=False)
    q3_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q3_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q3_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q3_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q4_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q4_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q4_half_total = db.Column(db.String(10), default=0, nullable=False)
    q4_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q4_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q4_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q4_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "hour": self.hour,
            "week": self.week,
            "status": self.status,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,
            "casino": self.casino,
            "away": self.away,
            "home": self.home,
            "spread_away": self.spread_away,
            "spread_home": self.spread_home,
            "juice_spread_away": self.juice_spread_away,
            "juice_spread_home": self.juice_spread_home,
            "moneyLineAway": self.moneyLineAway,
            "moneyLineHome": self.moneyLineHome,
            "total": self.total,
            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,
            "tt_away": self.tt_away,
            "juice_over_away": self.juice_over_away,
            "juice_under_away": self.juice_under_away,
            "tt_home": self.tt_home,
            "juice_over_home": self.juice_over_home,
            "juice_under_home": self.juice_under_home,
            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "first_half_spread_away": self.first_half_spread_away,
            "first_half_spread_home": self.first_half_spread_home,
            "first_half_juice_spread_away": self.first_half_juice_spread_away,
            "first_half_juice_spread_home": self.first_half_juice_spread_home,
            "first_half_moneyLineAway": self.first_half_moneyLineAway,
            "first_half_moneyLineHome": self.first_half_moneyLineHome,
            "first_half_total": self.first_half_total,
            "fh_juice_total_over": self.fh_juice_total_over,
            "fh_juice_total_under": self.fh_juice_total_under,
            "first_half_tt_away": self.first_half_tt_away,
            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_tt_home": self.first_half_tt_home,
            "first_half_juice_over_home": self.first_half_juice_over_home,
            "first_half_juice_under_home": self.first_half_juice_under_home,
            "first_half_final_score_away": self.first_half_final_score_away,
            "first_half_final_score_home": self.first_half_final_score_home,

            "second_half_spread_away": self.second_half_spread_away,
            "second_half_spread_home": self.second_half_spread_home,
            "second_half_juice_spread_away": self.second_half_juice_spread_away,
            "second_half_juice_spread_home": self.second_half_juice_spread_home,
            "second_half_moneyLineAway": self.second_half_moneyLineAway,
            "second_half_moneyLineHome": self.second_half_moneyLineHome,
            "second_half_total": self.second_half_total,
            "sh_juice_total_over": self.sh_juice_total_over,
            "sh_juice_total_under": self.sh_juice_total_under,
            "second_half_tt_away": self.second_half_tt_away,
            "second_half_juice_over_away": self.second_half_juice_over_away,
            "second_half_juice_under_away": self.second_half_juice_under_away,
            "second_half_tt_home": self.second_half_tt_home,
            "second_half_juice_over_home": self.second_half_juice_over_home,
            "second_half_juice_under_home": self.second_half_juice_under_home,
            "second_half_final_score_away": self.second_half_final_score_away,
            "second_half_final_score_home": self.second_half_final_score_home,

            "q1_half_spread_away": self.q1_half_spread_away,
            "q1_half_spread_home": self.q1_half_spread_home,
            "q1_half_juice_spread_away": self.q1_half_juice_spread_away,
            "q1_half_juice_spread_home": self.q1_half_juice_spread_home,
            "q1_half_moneyLineAway": self.q1_half_moneyLineAway,
            "q1_half_moneyLineHome": self.q1_half_moneyLineHome,
            "q1_half_total": self.q1_half_total,
            "q1_juice_over": self.q1_juice_over,
            "q1_juice_under": self.q1_juice_under,
            "q1_half_tt_away": self.q1_half_tt_away,
            "q1_half_juice_over_away": self.q1_half_juice_over_away,
            "q1_half_juice_under_away": self.q1_half_juice_under_away,
            "q1_half_tt_home": self.q1_half_tt_home,
            "q1_half_juice_over_home": self.q1_half_juice_over_home,
            "q1_half_juice_under_home": self.q1_half_juice_under_home,
            "q1_half_final_score_away": self.q1_half_final_score_away,
            "q1_half_final_score_home": self.q1_half_final_score_home,

            "q2_half_spread_away": self.q2_half_spread_away,
            "q2_half_spread_home": self.q2_half_spread_home,
            "q2_half_juice_spread_away": self.q2_half_juice_spread_away,
            "q2_half_juice_spread_home": self.q2_half_juice_spread_home,
            "q2_half_moneyLineAway": self.q2_half_moneyLineAway,
            "q2_half_moneyLineHome": self.q2_half_moneyLineHome,
            "q2_half_total": self.q2_half_total,
            "q2_juice_over": self.q2_juice_over,
            "q2_juice_under": self.q2_juice_under,
            "q2_half_tt_away": self.q2_half_tt_away,
            "q2_half_juice_over_away": self.q2_half_juice_over_away,
            "q2_half_juice_under_away": self.q2_half_juice_under_away,
            "q2_half_tt_home": self.q2_half_tt_home,
            "q2_half_juice_over_home": self.q2_half_juice_over_home,
            "q2_half_juice_under_home": self.q2_half_juice_under_home,
            "q2_half_final_score_away": self.q2_half_final_score_away,
            "q2_half_final_score_home": self.q2_half_final_score_home,

            "q3_half_spread_away": self.q3_half_spread_away,
            "q3_half_spread_home": self.q3_half_spread_home,
            "q3_half_juice_spread_away": self.q3_half_juice_spread_away,
            "q3_half_juice_spread_home": self.q3_half_juice_spread_home,
            "q3_half_moneyLineAway": self.q3_half_moneyLineAway,
            "q3_half_moneyLineHome": self.q3_half_moneyLineHome,
            "q3_half_total": self.q3_half_total,
            "q3_juice_over": self.q3_juice_over,
            "q3_juice_under": self.q3_juice_under,
            "q3_half_tt_away": self.q3_half_tt_away,
            "q3_half_juice_over_away": self.q3_half_juice_over_away,
            "q3_half_juice_under_away": self.q3_half_juice_under_away,
            "q3_half_tt_home": self.q3_half_tt_home,
            "q3_half_juice_over_home": self.q3_half_juice_over_home,
            "q3_half_juice_under_home": self.q3_half_juice_under_home,
            "q3_half_final_score_away": self.q3_half_final_score_away,
            "q3_half_final_score_home": self.q3_half_final_score_home,

            "q4_half_spread_away": self.q4_half_spread_away,
            "q4_half_spread_home": self.q4_half_spread_home,
            "q4_half_juice_spread_away": self.q4_half_juice_spread_away,
            "q4_half_juice_spread_home": self.q4_half_juice_spread_home,
            "q4_half_moneyLineAway": self.q4_half_moneyLineAway,
            "q4_half_moneyLineHome": self.q4_half_moneyLineHome,
            "q4_half_total": self.q4_half_total,
            "q4_juice_over": self.q4_juice_over,
            "q4_juice_under": self.q4_juice_under,
            "q4_half_tt_away": self.q4_half_tt_away,
            "q4_half_juice_over_away": self.q4_half_juice_over_away,
            "q4_half_juice_under_away": self.q4_half_juice_under_away,
            "q4_half_tt_home": self.q4_half_tt_home,
            "q4_half_juice_over_home": self.q4_half_juice_over_home,
            "q4_half_juice_under_home": self.q4_half_juice_under_home,
            "q4_half_final_score_away": self.q4_half_final_score_away,
            "q4_half_final_score_home": self.q4_half_final_score_home,
            # do not serialize the password, its a security breach
        }


class Ncaa_Basketball(db.Model):
    __tablename__ = "ncaa_basketball"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(20), nullable=False)
    rotation_home = db.Column(db.String(10), nullable=False)
    rotation_away = db.Column(db.String(10), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    home = db.Column(db.String(50), nullable=False)
    spread_away = db.Column(db.String(10), nullable=False)
    spread_home = db.Column(db.String(10), nullable=False)
    juice_spread_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_spread_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)
# ----------
    first_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_total = db.Column(db.String(10), default=0, nullable=False)
    fh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    fh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    first_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    first_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    first_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    second_half_spread_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_spread_home = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_moneyLineAway = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_moneyLineHome = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_total = db.Column(db.String(10), default=0, nullable=False)
    sh_juice_total_over = db.Column(
        db.String(10), default=-110, nullable=False)
    sh_juice_total_under = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    second_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    second_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    second_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
# ------------------------------------------------------------------------------
    q1_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q1_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q1_half_total = db.Column(db.String(10), default=0, nullable=False)
    q1_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q1_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q1_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q1_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q1_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q1_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q2_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q2_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q2_half_total = db.Column(db.String(10), default=0, nullable=False)
    q2_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q2_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q2_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q2_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q2_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q2_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q3_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q3_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q3_half_total = db.Column(db.String(10), default=0, nullable=False)
    q3_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q3_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q3_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q3_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q3_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q3_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------
    q4_half_spread_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_spread_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_spread_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_spread_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_moneyLineAway = db.Column(db.String(10), default=0, nullable=False)
    q4_half_moneyLineHome = db.Column(db.String(10), default=0, nullable=False)
    q4_half_total = db.Column(db.String(10), default=0, nullable=False)
    q4_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    q4_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    q4_half_tt_away = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_away = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_tt_home = db.Column(db.String(10), default=0, nullable=False)
    q4_half_juice_over_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_juice_under_home = db.Column(
        db.String(10), default=-110, nullable=False)
    q4_half_final_score_away = db.Column(
        db.String(10), default=0, nullable=False)
    q4_half_final_score_home = db.Column(
        db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "hour": self.hour,
            "week": self.week,
            "status": self.status,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,
            "casino": self.casino,
            "away": self.away,
            "home": self.home,
            "spread_away": self.spread_away,
            "spread_home": self.spread_home,
            "juice_spread_away": self.juice_spread_away,
            "juice_spread_home": self.juice_spread_home,
            "moneyLineAway": self.moneyLineAway,
            "moneyLineHome": self.moneyLineHome,
            "total": self.total,
            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,
            "tt_away": self.tt_away,
            "juice_over_away": self.juice_over_away,
            "juice_under_away": self.juice_under_away,
            "tt_home": self.tt_home,
            "juice_over_home": self.juice_over_home,
            "juice_under_home": self.juice_under_home,
            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "first_half_spread_away": self.first_half_spread_away,
            "first_half_spread_home": self.first_half_spread_home,
            "first_half_juice_spread_away": self.first_half_juice_spread_away,
            "first_half_juice_spread_home": self.first_half_juice_spread_home,
            "first_half_moneyLineAway": self.first_half_moneyLineAway,
            "first_half_moneyLineHome": self.first_half_moneyLineHome,
            "first_half_total": self.first_half_total,
            "fh_juice_total_over": self.fh_juice_total_over,
            "fh_juice_total_under": self.fh_juice_total_under,
            "first_half_tt_away": self.first_half_tt_away,
            "first_half_juice_over_away": self.first_half_juice_over_away,
            "first_half_juice_under_away": self.first_half_juice_under_away,
            "first_half_tt_home": self.first_half_tt_home,
            "first_half_juice_over_home": self.first_half_juice_over_home,
            "first_half_juice_under_home": self.first_half_juice_under_home,
            "first_half_final_score_away": self.first_half_final_score_away,
            "first_half_final_score_home": self.first_half_final_score_home,

            "second_half_spread_away": self.second_half_spread_away,
            "second_half_spread_home": self.second_half_spread_home,
            "second_half_juice_spread_away": self.second_half_juice_spread_away,
            "second_half_juice_spread_home": self.second_half_juice_spread_home,
            "second_half_moneyLineAway": self.second_half_moneyLineAway,
            "second_half_moneyLineHome": self.second_half_moneyLineHome,
            "second_half_total": self.second_half_total,
            "sh_juice_total_over": self.sh_juice_total_over,
            "sh_juice_total_under": self.sh_juice_total_under,
            "second_half_tt_away": self.second_half_tt_away,
            "second_half_juice_over_away": self.second_half_juice_over_away,
            "second_half_juice_under_away": self.second_half_juice_under_away,
            "second_half_tt_home": self.second_half_tt_home,
            "second_half_juice_over_home": self.second_half_juice_over_home,
            "second_half_juice_under_home": self.second_half_juice_under_home,
            "second_half_final_score_away": self.second_half_final_score_away,
            "second_half_final_score_home": self.second_half_final_score_home,

            "q1_half_spread_away": self.q1_half_spread_away,
            "q1_half_spread_home": self.q1_half_spread_home,
            "q1_half_juice_spread_away": self.q1_half_juice_spread_away,
            "q1_half_juice_spread_home": self.q1_half_juice_spread_home,
            "q1_half_moneyLineAway": self.q1_half_moneyLineAway,
            "q1_half_moneyLineHome": self.q1_half_moneyLineHome,
            "q1_half_total": self.q1_half_total,
            "q1_juice_over": self.q1_juice_over,
            "q1_juice_under": self.q1_juice_under,
            "q1_half_tt_away": self.q1_half_tt_away,
            "q1_half_juice_over_away": self.q1_half_juice_over_away,
            "q1_half_juice_under_away": self.q1_half_juice_under_away,
            "q1_half_tt_home": self.q1_half_tt_home,
            "q1_half_juice_over_home": self.q1_half_juice_over_home,
            "q1_half_juice_under_home": self.q1_half_juice_under_home,
            "q1_half_final_score_away": self.q1_half_final_score_away,
            "q1_half_final_score_home": self.q1_half_final_score_home,

            "q2_half_spread_away": self.q2_half_spread_away,
            "q2_half_spread_home": self.q2_half_spread_home,
            "q2_half_juice_spread_away": self.q2_half_juice_spread_away,
            "q2_half_juice_spread_home": self.q2_half_juice_spread_home,
            "q2_half_moneyLineAway": self.q2_half_moneyLineAway,
            "q2_half_moneyLineHome": self.q2_half_moneyLineHome,
            "q2_half_total": self.q2_half_total,
            "q2_juice_over": self.q2_juice_over,
            "q2_juice_under": self.q2_juice_under,
            "q2_half_tt_away": self.q2_half_tt_away,
            "q2_half_juice_over_away": self.q2_half_juice_over_away,
            "q2_half_juice_under_away": self.q2_half_juice_under_away,
            "q2_half_tt_home": self.q2_half_tt_home,
            "q2_half_juice_over_home": self.q2_half_juice_over_home,
            "q2_half_juice_under_home": self.q2_half_juice_under_home,
            "q2_half_final_score_away": self.q2_half_final_score_away,
            "q2_half_final_score_home": self.q2_half_final_score_home,

            "q3_half_spread_away": self.q3_half_spread_away,
            "q3_half_spread_home": self.q3_half_spread_home,
            "q3_half_juice_spread_away": self.q3_half_juice_spread_away,
            "q3_half_juice_spread_home": self.q3_half_juice_spread_home,
            "q3_half_moneyLineAway": self.q3_half_moneyLineAway,
            "q3_half_moneyLineHome": self.q3_half_moneyLineHome,
            "q3_half_total": self.q3_half_total,
            "q3_juice_over": self.q3_juice_over,
            "q3_juice_under": self.q3_juice_under,
            "q3_half_tt_away": self.q3_half_tt_away,
            "q3_half_juice_over_away": self.q3_half_juice_over_away,
            "q3_half_juice_under_away": self.q3_half_juice_under_away,
            "q3_half_tt_home": self.q3_half_tt_home,
            "q3_half_juice_over_home": self.q3_half_juice_over_home,
            "q3_half_juice_under_home": self.q3_half_juice_under_home,
            "q3_half_final_score_away": self.q3_half_final_score_away,
            "q3_half_final_score_home": self.q3_half_final_score_home,

            "q4_half_spread_away": self.q4_half_spread_away,
            "q4_half_spread_home": self.q4_half_spread_home,
            "q4_half_juice_spread_away": self.q4_half_juice_spread_away,
            "q4_half_juice_spread_home": self.q4_half_juice_spread_home,
            "q4_half_moneyLineAway": self.q4_half_moneyLineAway,
            "q4_half_moneyLineHome": self.q4_half_moneyLineHome,
            "q4_half_total": self.q4_half_total,
            "q4_juice_over": self.q4_juice_over,
            "q4_juice_under": self.q4_juice_under,
            "q4_half_tt_away": self.q4_half_tt_away,
            "q4_half_juice_over_away": self.q4_half_juice_over_away,
            "q4_half_juice_under_away": self.q4_half_juice_under_away,
            "q4_half_tt_home": self.q4_half_tt_home,
            "q4_half_juice_over_home": self.q4_half_juice_over_home,
            "q4_half_juice_under_home": self.q4_half_juice_under_home,
            "q4_half_final_score_away": self.q4_half_final_score_away,
            "q4_half_final_score_home": self.q4_half_final_score_home,
            # do not serialize the password, its a security breach
        }


class Stats_ncaa_basket_team(db.Model):
    __tablename__ = "stats_ncaa_basket_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    conference = db.Column(db.String(30), nullable=False)
    division = db.Column(db.String(30), nullable=False)

    w = db.Column(db.String(10), default=0, nullable=False)
    L = db.Column(db.String(10), default=0, nullable=False)
    ptc = db.Column(db.String(10), default=0, nullable=False)
    gb = db.Column(db.String(10), default=0, nullable=False)
    home = db.Column(db.String(10), default=0, nullable=False)
    away = db.Column(db.String(10), default=0, nullable=False)
    div = db.Column(db.String(10), default=0, nullable=False)
    conf = db.Column(db.String(10), default=0, nullable=False)
    ppg = db.Column(db.String(10), default=0, nullable=False)
    opp_ppg = db.Column(db.String(10), default=0, nullable=False)
    diff = db.Column(db.String(10), default=0, nullable=False)
    strk = db.Column(db.String(10), default=0, nullable=False)
    l10 = db.Column(db.String(10), default=-0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "team": self.team,
            "conference": self.conference,
            "division": self.division,

            "w": self.w,
            "L": self.L,
            "ptc": self.ptc,
            "gb": self.gb,
            "home": self.home,
            "away": self.away,
            "div": self.div,
            "conf": self.conf,
            "ppg": self.ppg,
            "opp_ppg": self.opp_ppg,
            "diff": self.diff,
            "strk": self.strk,
            "l10": self.l10
            # do not serialize the password, its a security breach
        }


class Stats_ncaa_basket_player(db.Model):
    __tablename__ = "stats_ncaa_basket_player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    college = db.Column(db.String(30), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    dorsal = db.Column(db.String(5), nullable=False)
    minutes = db.Column(db.String(10), default=0, nullable=False)
    position = db.Column(db.String(5), default=0, nullable=False)
    gp = db.Column(db.String(10), default=0, nullable=False)
    gs = db.Column(db.String(10), default=0, nullable=False)
    fg = db.Column(db.String(10), default=0, nullable=False)
    fg_AVG = db.Column(db.String(10), default=0, nullable=False)
    three_pt = db.Column(db.String(10), default=0, nullable=False)
    three_pt_AVG = db.Column(db.String(10), default=0, nullable=False)
    ft = db.Column(db.String(10), default=0, nullable=False)
    ft_AVG = db.Column(db.String(10), default=0, nullable=False)
    Or = db.Column(db.String(10), default=0, nullable=False)
    dr = db.Column(db.String(10), default=0, nullable=False)
    reb = db.Column(db.String(10), default=0, nullable=False)
    ast = db.Column(db.String(10), default=0, nullable=False)
    stl = db.Column(db.String(10), default=0, nullable=False)
    blk = db.Column(db.String(10), default=0, nullable=False)
    to = db.Column(db.String(10), default=0, nullable=False)
    pf = db.Column(db.String(10), default=0, nullable=False)
    pts = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "college": self.college,
            "season": self.season,
            "team": self.team,
            "dorsal": self.dorsal,
            "minutes": self.minutes,
            "position": self.position,
            "headshot": self.headshot,
            "gp": self.gp,
            "gs": self.gs,
            "fg": self.fg,
            "fg_AVG": self.fg_AVG,
            "three_pt": self.three_pt,
            "three_pt_AVG": self.three_pt_AVG,
            "ft": self.ft,
            "Or": self.Or,
            "dr": self.dr,
            "ft_AVG": self.ft_AVG,
            "reb": self.reb,
            "ast": self.ast,
            "stl": self.stl,
            "blk": self.blk,
            "to": self.to,
            "pf": self.pf,
            "pts": self.pts
            # do not serialize the password, its a security breach
        }


class Nhl(db.Model):
    __tablename__ = "nhl"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    rotation_away = db.Column(db.String(15), nullable=False)
    rotation_home = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(15), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    home = db.Column(db.String(50), nullable=False)
    puck_line_away = db.Column(db.String(10), nullable=False)
    puck_line_home = db.Column(db.String(10), nullable=False)
    juice_puck_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_puck_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), default=0, nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), default=0, nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), default=0, nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)

# -----------------------------------------------------------------------
    puck_away_1Q = db.Column(db.String(10), default=0, nullable=False)
    puck_home_1Q = db.Column(db.String(10), default=0, nullable=False)
    juice_puck_away_1Q = db.Column(db.String(10), default=-110, nullable=False)
    juice_puck_home_1Q = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway_1Q = db.Column(db.String(10), default=0, nullable=False)
    moneyLineHome_1Q = db.Column(db.String(10), default=0, nullable=False)
    total_1Q = db.Column(db.String(10), default=0, nullable=False)
    Q1_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    Q1_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away_1Q = db.Column(db.String(10), default=0, nullable=False)
    juice_over_away_1Q = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away_1Q = db.Column(
        db.String(10), default=-110, nullable=False)
    tt_home_1Q = db.Column(db.String(10), default=0, nullable=False)
    juice_over_home_1Q = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home_1Q = db.Column(
        db.String(10), default=-110, nullable=False)

# ----------------------------------------------------------------------
    sa_1Q = db.Column(db.String(10), default=0, nullable=False)
    sh_1Q = db.Column(db.String(10), default=0, nullable=False)
    sa_2Q = db.Column(db.String(10), default=0, nullable=False)
    sh_2Q = db.Column(db.String(10), default=0, nullable=False)
    sa_3Q = db.Column(db.String(10), default=0, nullable=False)
    sh_3Q = db.Column(db.String(10), default=0, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "casino": self.casino,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,
            "away": self.away,
            "home": self.home,

            "puck_line_away": self.puck_line_away,
            "puck_line_home": self.puck_line_home,

            "juice_puck_away": self.juice_puck_away,
            "juice_puck_home": self.juice_puck_home,

            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,

            "total": self.total,

            "tt_away": self.tt_away,
            "tt_home": self.tt_home,

            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,

            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,

            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,

            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "puck_away_1Q": self.puck_away_1Q,
            "puck_home_1Q": self.puck_home_1Q,

            "juice_puck_away_1Q": self.juice_puck_away_1Q,
            "juice_puck_home_1Q": self.juice_puck_home_1Q,

            "Q1_juice_over": self.Q1_juice_over,
            "Q1_juice_under": self.Q1_juice_under,

            "moneyLineHome_1Q": self.moneyLineHome_1Q,
            "moneyLineAway_1Q": self.moneyLineAway_1Q,

            "total_1Q": self.total_1Q,
            "tt_home_1Q": self.tt_home_1Q,

            "tt_away_1Q": self.tt_away_1Q,
            "tt_home_1Q": self.tt_home_1Q,

            "juice_over_away_1Q": self.juice_over_away_1Q,
            "juice_over_home_1Q": self.juice_over_home_1Q,

            "juice_under_away_1Q": self.juice_under_away_1Q,
            "juice_under_home_1Q": self.juice_under_home_1Q,

            "sa_1Q": self.sa_1Q,
            "sh_1Q": self.sh_1Q,
            "sa_2Q": self.sa_2Q,
            "sh_2Q": self.sh_2Q,
            "sa_3Q": self.sa_3Q,
            "sh_3Q": self.sh_3Q,
            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Boxeo(db.Model):
    __tablename__ = "boxeo"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(15), nullable=False)
    rotation_number = db.Column(db.String(10), nullable=False)
    event = db.Column(db.String(50), nullable=False)
    rounds = db.Column(db.String(50), nullable=False)
    location_Fight = db.Column(db.String(100), nullable=False)
    fighter_One = db.Column(db.String(50), nullable=False)
    money_Line_One = db.Column(db.String(10), nullable=False)
    fighter_Two = db.Column(db.String(50), nullable=False)
    money_Line_Two = db.Column(db.String(10), nullable=False)
    winner = db.Column(db.String(50), nullable=False)
    finish_by = db.Column(db.String(50), nullable=False)

    r1_result = db.Column(db.String(50), nullable=False)
    r2_result = db.Column(db.String(50), nullable=False)
    r3_result = db.Column(db.String(50), nullable=False)
    r4_result = db.Column(db.String(50), nullable=False)
    r5_result = db.Column(db.String(50), nullable=False)
    r6_result = db.Column(db.String(50), nullable=False)
    r7_result = db.Column(db.String(50), nullable=False)
    r8_result = db.Column(db.String(50), nullable=False)
    r9_result = db.Column(db.String(50), nullable=False)
    r10_result = db.Column(db.String(50), nullable=False)
    r11_result = db.Column(db.String(50), nullable=False)
    r12_result = db.Column(db.String(50), nullable=False)
    r13_result = db.Column(db.String(50), nullable=False)
    r14_result = db.Column(db.String(50), nullable=False)
    r15_result = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "casino": self.casino,
            "rotation_number": self.rotation_number,
            "event": self.event,
            "rounds": self.rounds,
            "location_Fight": self.location_Fight,
            "fighter_One": self.fighter_One,
            "fighter_Two": self.fighter_Two,
            "money_Line_One": self.money_Line_One,
            "money_Line_Two": self.money_Line_Two,
            "winner": self.winner,
            "week": self.week,
            "finish_by": self.finish_by,

            "r1_result": self.r1_result,
            "r2_result": self.r2_result,
            "r3_result": self.r3_result,
            "r4_result": self.r4_result,
            "r5_result": self.r5_result,
            "r6_result": self.r6_result,
            "r7_result": self.r7_result,
            "r8_result": self.r8_result,
            "r9_result": self.r9_result,
            "r10_result": self.r10_result,
            "r11_result": self.r11_result,
            "r12_result": self.r12_result,
            "r13_result": self.r13_result,
            "r14_result": self.r14_result,
            "r15_result": self.r15_result,

            "date": self.date,
            "hour": self.hour
        }


class Mma(db.Model):
    __tablename__ = "mma"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(15), nullable=False)
    rotation_number = db.Column(db.String(10), nullable=False)
    event = db.Column(db.String(50), nullable=False)
    rounds = db.Column(db.String(50), nullable=False)
    location_Fight = db.Column(db.String(100), nullable=False)
    fighter_One = db.Column(db.String(50), nullable=False)
    money_Line_One = db.Column(db.String(10), nullable=False)
    fighter_Two = db.Column(db.String(50), nullable=False)
    money_Line_Two = db.Column(db.String(10), nullable=False)
    winner = db.Column(db.String(50), nullable=False)
    finish_by = db.Column(db.String(50), nullable=False)

    r1_result = db.Column(db.String(50), nullable=False)
    r2_result = db.Column(db.String(50), nullable=False)
    r3_result = db.Column(db.String(50), nullable=False)
    r4_result = db.Column(db.String(50), nullable=False)
    r5_result = db.Column(db.String(50), nullable=False)
    r6_result = db.Column(db.String(50), nullable=False)
    r7_result = db.Column(db.String(50), nullable=False)
    r8_result = db.Column(db.String(50), nullable=False)
    r9_result = db.Column(db.String(50), nullable=False)
    r10_result = db.Column(db.String(50), nullable=False)
    r11_result = db.Column(db.String(50), nullable=False)
    r12_result = db.Column(db.String(50), nullable=False)
    r13_result = db.Column(db.String(50), nullable=False)
    r14_result = db.Column(db.String(50), nullable=False)
    r15_result = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "casino": self.casino,
            "rotation_number": self.rotation_number,
            "event": self.event,
            "rounds": self.rounds,
            "location_Fight": self.location_Fight,
            "fighter_One": self.fighter_One,
            "fighter_Two": self.fighter_Two,
            "money_Line_One": self.money_Line_One,
            "money_Line_Two": self.money_Line_Two,
            "winner": self.winner,
            "week": self.week,
            "finish_by": self.finish_by,

            "r1_result": self.r1_result,
            "r2_result": self.r2_result,
            "r3_result": self.r3_result,
            "r4_result": self.r4_result,
            "r5_result": self.r5_result,
            "r6_result": self.r6_result,
            "r7_result": self.r7_result,
            "r8_result": self.r8_result,
            "r9_result": self.r9_result,
            "r10_result": self.r10_result,
            "r11_result": self.r11_result,
            "r12_result": self.r12_result,
            "r13_result": self.r13_result,
            "r14_result": self.r14_result,
            "r15_result": self.r15_result,

            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Nascar(db.Model):
    __tablename__ = "nascar"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(15), nullable=False)
    rotation_number = db.Column(db.String(10), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    event = db.Column(db.String(50), nullable=False)
    track = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    place1 = db.Column(db.String(50), nullable=False)
    place2 = db.Column(db.String(50), nullable=False)
    place3 = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "hour": self.hour,
            "week": self.week,
            "status": self.status,
            "casino": self.casino,
            "rotation_number": self.rotation_number,
            "race": self.race,
            "event": self.event,
            "track": self.track,
            "location": self.location,
            "place1": self.place1,
            "place2": self.place2,
            "place3": self.place3,
            "date": self.date,
            # do not serialize the password, its a security breach
        }

class Moto_GP(db.Model):
    __tablename__ = "moto_gp"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(15), nullable=False)
    rotation_number = db.Column(db.String(10), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    track = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    place1 = db.Column(db.String(50), nullable=False)
    place2 = db.Column(db.String(50), nullable=False)
    place3 = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "hour": self.hour,
            "week": self.week,
            "status": self.status,
            "casino": self.casino,
            "rotation_number": self.rotation_number,
            "race": self.race,
            "track": self.track,
            "location": self.location,
            "place1": self.place1,
            "place2": self.place2,
            "place3": self.place3,
            "date": self.date,
            # do not serialize the password, its a security breach
        }

class Match_Ups_Nacar(db.Model):
    __tablename__ = "match_ups_nascar"
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(50), nullable=False)
    mu1 = db.Column(db.String(50), nullable=False)
    name2 = db.Column(db.String(50), nullable=False)
    mu2 = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name1": self.name1,
            "name2": self.name2,
            "mu1": self.mu1,
            "mu2": self.mu2,
            # do not serialize the password, its a security breach
        }


class Golf(db.Model):
    __tablename__ = "golf"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    week = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(15), nullable=False)
    rotation_number = db.Column(db.String(10), nullable=False)
    event = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    place1 = db.Column(db.String(50), nullable=False)
    place2 = db.Column(db.String(50), nullable=False)
    place3 = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "casino": self.casino,
            "event": self.event,
            "rotation_number": self.rotation_number,
            "location": self.location,
            "place1": self.place1,
            "place2": self.place2,
            "place3": self.place3,
            "date": self.date,
            "hour": self.hour,
            "week": self.week,
            # do not serialize the password, its a security breach
        }


class Soccer(db.Model):
    __tablename__ = "soccer"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    casino = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    tournament = db.Column(db.String(15), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    home = db.Column(db.String(50), nullable=False)
    rotation_away = db.Column(db.String(15), nullable=False)
    rotation_home = db.Column(db.String(15), nullable=False)
    goal_line_away = db.Column(db.String(10), nullable=False)
    goal_line_home = db.Column(db.String(10), nullable=False)
    juice_goal_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_goal_home = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway = db.Column(db.String(10), nullable=False)
    moneyLineHome = db.Column(db.String(10), nullable=False)
    total = db.Column(db.String(10), default=0, nullable=False)
    juice_total_over = db.Column(db.String(10), default=-110, nullable=False)
    juice_total_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away = db.Column(db.String(10), default=0, nullable=False)
    juice_over_away = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away = db.Column(db.String(10), default=-110, nullable=False)
    tt_home = db.Column(db.String(10), default=0, nullable=False)
    juice_over_home = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home = db.Column(db.String(10), default=-110, nullable=False)
    final_score_away = db.Column(db.String(10), default=0, nullable=False)
    final_score_home = db.Column(db.String(10), default=0, nullable=False)

# -----------------------------------------------------------------------
    goal_away_1H = db.Column(db.String(10), default=0, nullable=False)
    goal_home_1H = db.Column(db.String(10), default=0, nullable=False)
    juice_goal_away_1H = db.Column(db.String(10), default=-110, nullable=False)
    juice_goal_home_1H = db.Column(db.String(10), default=-110, nullable=False)
    moneyLineAway_1H = db.Column(db.String(10), default=0, nullable=False)
    moneyLineHome_1H = db.Column(db.String(10), default=0, nullable=False)
    total_1H = db.Column(db.String(10), default=0, nullable=False)
    H1_juice_over = db.Column(db.String(10), default=-110, nullable=False)
    H1_juice_under = db.Column(db.String(10), default=-110, nullable=False)
    tt_away_1H = db.Column(db.String(10), default=0, nullable=False)
    juice_over_away_1H = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_away_1H = db.Column(
        db.String(10), default=-110, nullable=False)
    tt_home_1H = db.Column(db.String(10), default=0, nullable=False)
    juice_over_home_1H = db.Column(db.String(10), default=-110, nullable=False)
    juice_under_home_1H = db.Column(
        db.String(10), default=-110, nullable=False)

# ----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "casino": self.casino,
            "country": self.country,
            "tournament": self.tournament,
            "away": self.away,
            "home": self.home,
            "rotation_away": self.rotation_away,
            "rotation_home": self.rotation_home,

            "goal_line_away": self.goal_line_away,
            "goal_line_home": self.goal_line_home,

            "juice_goal_away": self.juice_goal_away,
            "juice_goal_home": self.juice_goal_home,

            "moneyLineHome": self.moneyLineHome,
            "moneyLineAway": self.moneyLineAway,

            "total": self.total,

            "tt_away": self.tt_away,
            "tt_home": self.tt_home,

            "juice_over_away": self.juice_over_away,
            "juice_over_home": self.juice_over_home,

            "juice_under_away": self.juice_under_away,
            "juice_under_home": self.juice_under_home,

            "juice_total_over": self.juice_total_over,
            "juice_total_under": self.juice_total_under,

            "final_score_away": self.final_score_away,
            "final_score_home": self.final_score_home,

            "goal_away_1H": self.goal_away_1H,
            "goal_home_1H": self.goal_home_1H,

            "juice_goal_away_1H": self.juice_goal_away_1H,
            "juice_goal_home_1H": self.juice_goal_home_1H,

            "H1_juice_over": self.H1_juice_over,
            "H1_juice_under": self.H1_juice_under,

            "moneyLineHome_1H": self.moneyLineHome_1H,
            "moneyLineAway_1H": self.moneyLineAway_1H,

            "total_1H": self.total_1H,
            "tt_home_1H": self.tt_home_1H,

            "tt_away_1H": self.tt_away_1H,
            "tt_home_1H": self.tt_home_1H,

            "juice_over_away_1H": self.juice_over_away_1H,
            "juice_over_home_1H": self.juice_over_home_1H,

            "juice_under_away_1H": self.juice_under_away_1H,
            "juice_under_home_1H": self.juice_under_home_1H,

            "date": self.date,
            "hour": self.hour
            # do not serialize the password, its a security breach
        }


class Stats_nba_player(db.Model):
    __tablename__ = "stats_nba_player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    college = db.Column(db.String(30), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    dorsal = db.Column(db.String(5), nullable=False)
    minutes = db.Column(db.String(10), default=0, nullable=False)
    position = db.Column(db.String(5), default=0, nullable=False)
    gp = db.Column(db.String(10), default=0, nullable=False)
    gs = db.Column(db.String(10), default=0, nullable=False)
    fg = db.Column(db.String(10), default=0, nullable=False)
    fg_AVG = db.Column(db.String(10), default=0, nullable=False)
    three_pt = db.Column(db.String(10), default=0, nullable=False)
    three_pt_AVG = db.Column(db.String(10), default=0, nullable=False)
    ft = db.Column(db.String(10), default=0, nullable=False)
    ft_AVG = db.Column(db.String(10), default=0, nullable=False)
    Or = db.Column(db.String(10), default=0, nullable=False)
    dr = db.Column(db.String(10), default=0, nullable=False)
    reb = db.Column(db.String(10), default=0, nullable=False)
    ast = db.Column(db.String(10), default=0, nullable=False)
    stl = db.Column(db.String(10), default=0, nullable=False)
    blk = db.Column(db.String(10), default=0, nullable=False)
    to = db.Column(db.String(10), default=0, nullable=False)
    pf = db.Column(db.String(10), default=0, nullable=False)
    pts = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "college": self.college,
            "season": self.season,
            "team": self.team,
            "dorsal": self.dorsal,
            "minutes": self.minutes,
            "position": self.position,
            "headshot": self.headshot,
            "gp": self.gp,
            "gs": self.gs,
            "fg": self.fg,
            "fg_AVG": self.fg_AVG,
            "three_pt": self.three_pt,
            "three_pt_AVG": self.three_pt_AVG,
            "ft": self.ft,
            "Or": self.Or,
            "dr": self.dr,
            "ft_AVG": self.ft_AVG,
            "reb": self.reb,
            "ast": self.ast,
            "stl": self.stl,
            "blk": self.blk,
            "to": self.to,
            "pf": self.pf,
            "pts": self.pts
            # do not serialize the password, its a security breach
        }


class Stats_nba_team(db.Model):
    __tablename__ = "stats_nba_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    conference = db.Column(db.String(30), nullable=False)
    division = db.Column(db.String(30), nullable=False)
    season_type = db.Column(db.String(20), nullable=False)
    group_type_comparation = db.Column(db.String(20), nullable=False)

    w = db.Column(db.String(10), default=0, nullable=False)
    L = db.Column(db.String(10), default=0, nullable=False)
    ptc = db.Column(db.String(10), default=0, nullable=False)
    gb = db.Column(db.String(10), default=0, nullable=False)
    home = db.Column(db.String(10), default=0, nullable=False)
    away = db.Column(db.String(10), default=0, nullable=False)
    div = db.Column(db.String(10), default=0, nullable=False)
    conf = db.Column(db.String(10), default=0, nullable=False)
    ppg = db.Column(db.String(10), default=0, nullable=False)
    opp_ppg = db.Column(db.String(10), default=0, nullable=False)
    diff = db.Column(db.String(10), default=0, nullable=False)
    strk = db.Column(db.String(10), default=0, nullable=False)
    l10 = db.Column(db.String(10), default=-0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "team": self.team,
            "conference": self.conference,
            "division": self.division,
            "season_type": self.season_type,
            "group_type_comparation": self.group_type_comparation,

            "w": self.w,
            "L": self.L,
            "ptc": self.ptc,
            "gb": self.gb,
            "home": self.home,
            "away": self.away,
            "div": self.div,
            "conf": self.conf,
            "ppg": self.ppg,
            "opp_ppg": self.opp_ppg,
            "diff": self.diff,
            "strk": self.strk,
            "l10": self.l10
            # do not serialize the password, its a security breach
        }


class Stats_mlb_team(db.Model):
    __tablename__ = "stats_mlb_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(10), nullable=False)
    season_type = db.Column(db.String(20), nullable=False)
    group_type_comparation = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(20), nullable=False)
    league = db.Column(db.String(20), nullable=False)
    division = db.Column(db.String(20), nullable=False)
    w = db.Column(db.String(10), default=0, nullable=False)
    L = db.Column(db.String(10), default=0, nullable=False)
    pct = db.Column(db.String(10), default=0, nullable=False)
    gb = db.Column(db.String(10), default=0, nullable=False)
    home = db.Column(db.String(10), default=0, nullable=False)
    away = db.Column(db.String(10), default=0, nullable=False)
    rs = db.Column(db.String(10), default=0, nullable=False)
    ra = db.Column(db.String(10), default=0, nullable=False)
    diff = db.Column(db.String(10), default=0, nullable=False)
    strk = db.Column(db.String(10), default=0, nullable=False)
    L10 = db.Column(db.String(10), default=-0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "season_type": self.season_type,
            "group_type_comparation": self.group_type_comparation,
            "team": self.team,
            "league": self.league,
            "division": self.division,
            "w": self.w,
            "L": self.L,
            "pct": self.pct,
            "gb": self.gb,
            "home": self.home,
            "away": self.away,
            "rs": self.rs,
            "ra": self.ra,
            "diff": self.diff,
            "strk": self.strk,
            "L10": self.L10
            # do not serialize the password, its a security breach
        }


class Stats_mlb_player(db.Model):
    __tablename__ = "stats_mlb_player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(20), nullable=False)
    dorsal = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    gp = db.Column(db.String(20), nullable=False)
    ab = db.Column(db.String(10), default=0, nullable=False)
    r = db.Column(db.String(10), default=0, nullable=False)
    h = db.Column(db.String(10), default=0, nullable=False)
    two_b = db.Column(db.String(10), default=0, nullable=False)
    three_b = db.Column(db.String(10), default=0, nullable=False)
    hb = db.Column(db.String(10), default=0, nullable=False)
    rbi = db.Column(db.String(10), default=0, nullable=False)
    tb = db.Column(db.String(10), default=0, nullable=False)
    bb = db.Column(db.String(10), default=0, nullable=False)
    so = db.Column(db.String(10), default=0, nullable=False)
    sb = db.Column(db.String(10), default=-0, nullable=False)
    avg = db.Column(db.String(10), default=0, nullable=False)
    obp = db.Column(db.String(10), default=0, nullable=False)
    slg = db.Column(db.String(10), default=0, nullable=False)
    ops = db.Column(db.String(10), default=0, nullable=False)
    war = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "season": self.season,
            "team": self.team,
            "dorsal": self.dorsal,
            "position": self.position,
            "headshot": self.headshot,
            "gp": self.gp,
            "ab": self.ab,
            "r": self.r,
            "h": self.h,
            "two_b": self.two_b,
            "three_b": self.three_b,
            "hb": self.hb,
            "rbi": self.rbi,
            "tb": self.tb,
            "bb": self.bb,
            "so": self.so,
            "sb": self.sb,
            "avg": self.avg,
            "obp": self.obp,
            "slg": self.slg,
            "ops": self.ops,
            "war": self.war
            # do not serialize the password, its a security breach
        }


class Stats_nhl_team(db.Model):
    __tablename__ = "stats_nhl_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(10), nullable=False)
    season_type = db.Column(db.String(20), nullable=False)
    group_type_comparation = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(20), nullable=False)
    conference = db.Column(db.String(20), nullable=False)
    division = db.Column(db.String(20), nullable=False)
    gp = db.Column(db.String(20), nullable=False)
    w = db.Column(db.String(10), default=0, nullable=False)
    L = db.Column(db.String(10), default=0, nullable=False)

    otl = db.Column(db.String(10), default=0, nullable=False)
    pts = db.Column(db.String(10), default=0, nullable=False)
    rw = db.Column(db.String(10), default=0, nullable=False)
    row = db.Column(db.String(10), default=0, nullable=False)
    sow = db.Column(db.String(10), default=0, nullable=False)
    sol = db.Column(db.String(10), default=0, nullable=False)
    home = db.Column(db.String(10), default=0, nullable=False)
    away = db.Column(db.String(10), default=0, nullable=False)
    gf = db.Column(db.String(10), default=-0, nullable=False)
    ga = db.Column(db.String(10), default=0, nullable=False)
    diff = db.Column(db.String(10), default=0, nullable=False)
    l10 = db.Column(db.String(10), default=0, nullable=False)
    strk = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "team": self.team,
            "conference": self.conference,
            "division": self.division,
            "season_type": self.season_type,
            "group_type_comparation": self.group_type_comparation,
            "gp": self.gp,
            "w": self.w,
            "L": self.L,

            "otl": self.otl,
            "pts": self.pts,
            "rw": self.rw,
            "row": self.row,
            "sow": self.sow,
            "sol": self.sol,
            "home": self.home,
            "away": self.away,
            "gf": self.gf,
            "ga": self.ga,
            "diff": self.diff,
            "l10": self.l10,
            "strk": self.strk
            # do not serialize the password, its a security breach
        }


class Stats_nhl_player(db.Model):
    __tablename__ = "stats_nhl_player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(20), nullable=False)
    dorsal = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)
    gp = db.Column(db.String(20), nullable=False)

    g = db.Column(db.String(10), default=0, nullable=False)
    a = db.Column(db.String(10), default=0, nullable=False)
    pts = db.Column(db.String(10), default=0, nullable=False)
    p_m_rating = db.Column(db.String(10), default=0, nullable=False)
    pim = db.Column(db.String(10), default=0, nullable=False)
    sog = db.Column(db.String(10), default=0, nullable=False)
    spct = db.Column(db.String(10), default=0, nullable=False)
    ppg = db.Column(db.String(10), default=0, nullable=False)
    ppa = db.Column(db.String(10), default=0, nullable=False)
    shg = db.Column(db.String(10), default=0, nullable=False)
    sha = db.Column(db.String(10), default=0, nullable=False)
    gwg = db.Column(db.String(10), default=0, nullable=False)
    gtg = db.Column(db.String(10), default=0, nullable=False)
    toi_g = db.Column(db.String(10), default=0, nullable=False)
    prod = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "season": self.season,
            "team": self.team,
            "dorsal": self.dorsal,
            "position": self.position,
            "headshot": self.headshot,
            "gp": self.gp,
            "g": self.g,
            "a": self.a,
            "pts": self.pts,
            "p_m_rating": self.p_m_rating,
            "pim": self.pim,
            "sog": self.sog,
            "spct": self.spct,
            "ppg": self.ppg,
            "ppa": self.ppa,
            "shg": self.shg,
            "sha": self.sha,
            "gwg": self.gwg,
            "gtg": self.gtg,
            "toi_g": self.toi_g,
            "prod": self.prod,
            # do not serialize the password, its a security breach
        }


class Stats_box_fighter(db.Model):
    __tablename__ = "stats_box_fighter"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    season = db.Column(db.String(20), nullable=False)
    association = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    w = db.Column(db.String(10), default=0, nullable=False)
    w_by = db.Column(db.String(10), default=0, nullable=False)
    L = db.Column(db.String(10), default=0, nullable=False)
    L_by = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "nickname": self.nickname,
            "headshot": self.headshot,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "country": self.country,
            "season": self.season,
            "association": self.association,
            "category": self.category,
            "w": self.w,
            "w_by": self.w_by,
            "L": self.L,
            "L_by": self.L_by,
            # do not serialize the password, its a security breach
        }


class Stats_mma_fighter(db.Model):
    __tablename__ = "stats_mma_fighter"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    season = db.Column(db.String(20), nullable=False)
    association = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    w = db.Column(db.String(10), default=0, nullable=False)
    w_by = db.Column(db.String(10), default=0, nullable=False)
    L = db.Column(db.String(10), default=0, nullable=False)
    L_by = db.Column(db.String(10), default=0, nullable=False)
    # -----------------------------------------------------------------------

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "nickname": self.nickname,
            "headshot": self.headshot,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "country": self.country,
            "season": self.season,
            "association": self.association,
            "category": self.category,
            "w": self.w,
            "w_by": self.w_by,
            "L": self.L,
            "L_by": self.L_by,
            # do not serialize the password, its a security breach
        }


class Nascar_drivers(db.Model):
    __tablename__ = "nascar_drivers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    birth = db.Column(db.String(50), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    sponsor = db.Column(db.String(100), nullable=False)
    engine = db.Column(db.String(50), nullable=False)
    number_car = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.String(50), nullable=False)
    starts = db.Column(db.String(50), nullable=False)
    poles = db.Column(db.String(50), nullable=False)
    top5 = db.Column(db.String(50), nullable=False)
    top10 = db.Column(db.String(50), nullable=False)
    laps_lead = db.Column(db.String(50), nullable=False)
    pts = db.Column(db.String(50), nullable=False)
    AVG_laps = db.Column(db.String(50), nullable=False)
    AVG_finish = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "birth": self.birth,
            "headshot": self.headshot,
            "sponsor": self.sponsor,
            "engine": self.engine,
            "number_car": self.number_car,
            "rank": self.rank,
            "starts": self.starts,
            "poles": self.poles,
            "top5": self.top5,
            "top10": self.top10,
            "laps_lead": self.laps_lead,
            "pts": self.pts,
            "AVG_laps": self.AVG_laps,
            "AVG_finish": self.AVG_finish,
            # do not serialize the password, its a security breach
        }

class Moto_gp_drivers(db.Model):
    __tablename__ = "moto_gp_drivers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    birth = db.Column(db.String(50), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    sponsor = db.Column(db.String(100), nullable=False)
    engine = db.Column(db.String(50), nullable=False)
    number_car = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.String(50), nullable=False)
    starts = db.Column(db.String(50), nullable=False)
    poles = db.Column(db.String(50), nullable=False)
    top5 = db.Column(db.String(50), nullable=False)
    top10 = db.Column(db.String(50), nullable=False)
    laps_lead = db.Column(db.String(50), nullable=False)
    pts = db.Column(db.String(50), nullable=False)
    AVG_laps = db.Column(db.String(50), nullable=False)
    AVG_finish = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "birth": self.birth,
            "headshot": self.headshot,
            "sponsor": self.sponsor,
            "engine": self.engine,
            "number_car": self.number_car,
            "rank": self.rank,
            "starts": self.starts,
            "poles": self.poles,
            "top5": self.top5,
            "top10": self.top10,
            "laps_lead": self.laps_lead,
            "pts": self.pts,
            "AVG_laps": self.AVG_laps,
            "AVG_finish": self.AVG_finish,
            # do not serialize the password, its a security breach
        }

class Golfer(db.Model):
    __tablename__ = "golfer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    season = db.Column(db.String(50), nullable=False)
    swing = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)
    cuts = db.Column(db.String(10), nullable=False)
    top10 = db.Column(db.String(10), nullable=False)
    w = db.Column(db.String(10), nullable=False)
    rnds = db.Column(db.String(10), nullable=False)
    holes = db.Column(db.String(10), nullable=False)
    avg = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "season": self.season,
            "headshot": self.headshot,
            "swing": self.swing,
            "birth": self.birth,
            "cuts": self.cuts,
            "top10": self.top10,
            "w": self.w,
            "rnds": self.rnds,
            "holes": self.holes,
            "avg": self.avg,
            # do not serialize the password, its a security breach
        }


class Stats_nfl_team(db.Model):
    __tablename__ = "stats_nfl_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(20), nullable=False)
    season_type = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    conference = db.Column(db.String(30), nullable=False)
    division = db.Column(db.String(30), nullable=False)
    TP = db.Column(db.String(10), nullable=False)
    ttpg = db.Column(db.String(10), nullable=False)
    t_td = db.Column(db.String(10), nullable=False)
    t_1_down = db.Column(db.String(10), nullable=False)
    Russ_1_d = db.Column(db.String(10), nullable=False)
    pass_1_d = db.Column(db.String(10), nullable=False)
    down_1_penal = db.Column(db.String(10), nullable=False)
    down_3_eff = db.Column(db.String(10), nullable=False)
    down_3_AVG = db.Column(db.String(10), nullable=False)
    down_4_eff = db.Column(db.String(10), nullable=False)
    down_4_AVG = db.Column(db.String(10), nullable=False)
    comp_att = db.Column(db.String(10), nullable=False)
    net_pass_y = db.Column(db.String(10), nullable=False)
    y_p_pas_attps = db.Column(db.String(10), nullable=False)
    net_pass_y_pg = db.Column(db.String(10), nullable=False)
    pass_td = db.Column(db.String(10), nullable=False)
    interceptions = db.Column(db.String(10), nullable=False)
    sacks_y_lost = db.Column(db.String(10), nullable=False)
    russ_attps = db.Column(db.String(10), nullable=False)
    russ_y = db.Column(db.String(10), nullable=False)
    y_p_russ_attp = db.Column(db.String(10), nullable=False)
    russ_y_pg = db.Column(db.String(10), nullable=False)
    russ_td = db.Column(db.String(10), nullable=False)
    total_of_plays = db.Column(db.String(10), nullable=False)
    total_y = db.Column(db.String(10), nullable=False)
    y_pg = db.Column(db.String(10), nullable=False)
    kickoffs_t = db.Column(db.String(10), nullable=False)
    AVG_kickoff_return_y = db.Column(db.String(10), nullable=False)
    punt_t = db.Column(db.String(10), nullable=False)
    AVG_punt_ruturn_y = db.Column(db.String(10), nullable=False)
    int_t = db.Column(db.String(10), nullable=False)
    AVG_intercept_y = db.Column(db.String(10), nullable=False)
    net_AVG_punt_y = db.Column(db.String(10), nullable=False)
    punt_ty = db.Column(db.String(10), nullable=False)
    fg_goog_attps = db.Column(db.String(10), nullable=False)
    touchback_percent = db.Column(db.String(10), nullable=False)
    penal_ty = db.Column(db.String(10), nullable=False)
    penal_y_AVG_pg = db.Column(db.String(10), nullable=False)
    possesion_time = db.Column(db.String(10), nullable=False)
    fumbles_lost = db.Column(db.String(10), nullable=False)
    turnover_ratio = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "season_type": self.season_type,
            "team": self.team,
            "conference": self.conference,
            "division": self.division,
            "TP": self.TP,
            "ttpg": self.ttpg,
            "t_td": self.t_td,
            "t_1_down": self.t_1_down,
            "Russ_1_d": self.Russ_1_d,
            "pass_1_d": self.pass_1_d,
            "down_1_penal": self.down_1_penal,
            "down_3_eff": self.down_3_eff,
            "down_3_AVG": self.down_3_AVG,
            "down_4_eff": self.down_4_eff,
            "down_4_AVG": self.down_4_AVG,
            "comp_att": self.comp_att,
            "net_pass_y": self.net_pass_y,
            "y_p_pas_attps": self.y_p_pas_attps,
            "net_pass_y_pg": self.net_pass_y_pg,
            "pass_td": self.pass_td,
            "interceptions": self.interceptions,
            "sacks_y_lost": self.sacks_y_lost,
            "russ_attps": self.russ_attps,
            "russ_y": self.russ_y,
            "y_p_russ_attp": self.y_p_russ_attp,
            "russ_y_pg": self.russ_y_pg,
            "russ_td": self.russ_td,
            "total_of_plays": self.total_of_plays,
            "total_y": self.total_y,
            "y_pg": self.y_pg,
            "kickoffs_t": self.kickoffs_t,
            "AVG_kickoff_return_y": self.AVG_kickoff_return_y,
            "punt_t": self.punt_t,
            "AVG_punt_ruturn_y": self.AVG_punt_ruturn_y,
            "int_t": self.int_t,
            "AVG_intercept_y": self.AVG_intercept_y,
            "net_AVG_punt_y": self.net_AVG_punt_y,
            "punt_ty": self.punt_ty,
            "fg_goog_attps": self.fg_goog_attps,
            "touchback_percent": self.touchback_percent,
            "penal_ty": self.penal_ty,
            "penal_y_AVG_pg": self.penal_y_AVG_pg,
            "possesion_time": self.possesion_time,
            "fumbles_lost": self.fumbles_lost,
            "turnover_ratio": self.turnover_ratio
            # do not serialize the password, its a security breach
        }


class Stats_defensive_player_nfl(db.Model):
    __tablename__ = "stats_defensive_player_nfl"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    tack_solo = db.Column(db.String(10), nullable=False)
    tack_ast = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    tack_total = db.Column(db.String(10), nullable=False)
    sacks = db.Column(db.String(10), nullable=False)
    sacks_yards = db.Column(db.String(10), nullable=False)
    tfl = db.Column(db.String(10), nullable=False)
    pd = db.Column(db.String(10), nullable=False)
    Int = db.Column(db.String(10), nullable=False)
    yds = db.Column(db.String(10), nullable=False)
    ing = db.Column(db.String(10), nullable=False)
    td = db.Column(db.String(10), nullable=False)
    ff = db.Column(db.String(10), nullable=False)
    fr = db.Column(db.String(10), nullable=False)
    ftd = db.Column(db.String(10), nullable=False)
    kb = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "tack_solo": self.tack_solo,
            "tack_ast": self.tack_ast,
            "tack_total": self.tack_total,
            "sacks": self.sacks,
            "sacks_yards": self.sacks_yards,
            "tfl": self.tfl,
            "pd": self.pd,
            "Int": self.Int,
            "yds": self.yds,
            "ing": self.ing,
            "td": self.td,
            "ff": self.ff,
            "fr": self.fr,
            "ftd": self.ftd,
            "kb": self.kb,
            # do not serialize the password, its a security breach
        }


class Stats_offensive_player_nfl(db.Model):
    __tablename__ = "stats_offensive_player_nfl"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    Cmp = db.Column(db.String(10), nullable=False)
    pass_att = db.Column(db.String(10), nullable=False)
    cmp_AVG = db.Column(db.String(10), nullable=False)
    yards = db.Column(db.String(10), nullable=False)
    yards_AVG = db.Column(db.String(10), nullable=False)
    yards_pg = db.Column(db.String(10), nullable=False)
    pass_td = db.Column(db.String(10), nullable=False)
    Int = db.Column(db.String(10), nullable=False)
    asck = db.Column(db.String(10), nullable=False)
    syl = db.Column(db.String(10), nullable=False)
    rtg = db.Column(db.String(10), nullable=False)
    russ_att = db.Column(db.String(10), nullable=False)
    russ_yards = db.Column(db.String(10), nullable=False)
    yards_p_russ = db.Column(db.String(10), nullable=False)
    big = db.Column(db.String(10), nullable=False)

    rush_tt = db.Column(db.String(10), nullable=False)
    rush_yard_pg = db.Column(db.String(10), nullable=False)
    fum = db.Column(db.String(10), nullable=False)
    lst = db.Column(db.String(10), nullable=False)
    long_pass = db.Column(db.String(10), nullable=False)
    fd = db.Column(db.String(10), nullable=False)
    rec = db.Column(db.String(10), nullable=False)
    r_tgts = db.Column(db.String(10), nullable=False)
    r_yards = db.Column(db.String(10), nullable=False)
    yards_p_r = db.Column(db.String(10), nullable=False)
    r_td = db.Column(db.String(10), nullable=False)
    lr = db.Column(db.String(10), nullable=False)
    r_big = db.Column(db.String(10), nullable=False)
    r_ypg = db.Column(db.String(10), nullable=False)
    r_fl = db.Column(db.String(10), nullable=False)
    r_yac = db.Column(db.String(10), nullable=False)
    r_fd = db.Column(db.String(10), nullable=False)
    pts = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "Cmp": self.Cmp,
            "pass_att": self.pass_att,
            "cmp_AVG": self.cmp_AVG,
            "yards": self.yards,
            "yards_AVG": self.yards_AVG,
            "yards_pg": self.yards_pg,
            "pass_td": self.pass_td,
            "Int": self.Int,
            "asck": self.asck,
            "syl": self.syl,
            "rtg": self.rtg,
            "russ_att": self.russ_att,
            "russ_yards": self.russ_yards,
            "yards_p_russ": self.yards_p_russ,
            "big": self.big,
            "rush_tt": self.rush_tt,
            "rush_yard_pg": self.rush_yard_pg,
            "fum": self.fum,
            "lst": self.lst,
            "long_pass": self.long_pass,
            "fd": self.fd,
            "rec": self.rec,
            "r_tgts": self.r_tgts,
            "r_yards": self.r_yards,
            "yards_p_r": self.yards_p_r,
            "r_td": self.r_td,
            "lr": self.lr,
            "r_big": self.r_big,
            "r_big": self.r_big,
            "r_ypg": self.r_ypg,
            "r_fl": self.r_fl,
            "r_yac": self.r_yac,
            "r_fd": self.r_fd,
            "pts": self.pts,
            # do not serialize the password, its a security breach
        }


class Stats_returning_player_nfl(db.Model):
    __tablename__ = "stats_returning_player_nfl"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    kick_returns = db.Column(db.String(10), nullable=False)
    kick_returns_yards = db.Column(db.String(10), nullable=False)
    yards_p_k_p = db.Column(db.String(10), nullable=False)
    l_k_r = db.Column(db.String(10), nullable=False)
    k_r_td = db.Column(db.String(10), nullable=False)
    punt_r = db.Column(db.String(10), nullable=False)
    punt_r_y = db.Column(db.String(10), nullable=False)
    y_ppr = db.Column(db.String(10), nullable=False)
    lpr = db.Column(db.String(10), nullable=False)
    pr_td = db.Column(db.String(10), nullable=False)
    punt_r_fair_carches = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "kick_returns": self.kick_returns,
            "kick_returns_yards": self.kick_returns_yards,
            "yards_p_k_p": self.yards_p_k_p,
            "l_k_r": self.l_k_r,
            "k_r_td": self.k_r_td,
            "punt_r": self.punt_r,
            "punt_r_y": self.punt_r_y,
            "y_ppr": self.y_ppr,
            "lpr": self.lpr,
            "pr_td": self.pr_td,
            "punt_r_fair_carches": self.punt_r_fair_carches,
            # do not serialize the password, its a security breach
        }


class Stats_kiking_player_nfl(db.Model):
    __tablename__ = "stats_kiking_player_nfl"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    fgm = db.Column(db.String(10), nullable=False)
    fga = db.Column(db.String(10), nullable=False)
    fg_AVG = db.Column(db.String(10), nullable=False)
    lng = db.Column(db.String(10), nullable=False)
    yars_f_goals_1_19 = db.Column(db.String(10), nullable=False)
    yars_f_goals_20_29 = db.Column(db.String(10), nullable=False)
    yars_f_goals_30_49 = db.Column(db.String(10), nullable=False)
    yars_f_goals_40_49 = db.Column(db.String(10), nullable=False)
    more_50 = db.Column(db.String(10), nullable=False)
    xpm = db.Column(db.String(10), nullable=False)
    xpa = db.Column(db.String(10), nullable=False)
    xp_AVG = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "fgm": self.fgm,
            "fga": self.fga,
            "fg_AVG": self.fg_AVG,
            "lng": self.lng,
            "yars_f_goals_1_19": self.yars_f_goals_1_19,
            "yars_f_goals_20_29": self.yars_f_goals_20_29,
            "yars_f_goals_30_49": self.yars_f_goals_30_49,
            "yars_f_goals_40_49": self.yars_f_goals_40_49,
            "more_50": self.more_50,
            "xpm": self.xpm,
            "xpa": self.xpa,
            "xp_AVG": self.xp_AVG,
            # do not serialize the password, its a security breach
        }


class Stats_punting_player_nfl(db.Model):
    __tablename__ = "stats_punting_player_nfl"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    punts = db.Column(db.String(10), nullable=False)
    yards = db.Column(db.String(10), nullable=False)
    lng = db.Column(db.String(10), nullable=False)
    AVG = db.Column(db.String(10), nullable=False)
    net = db.Column(db.String(10), nullable=False)
    p_blk = db.Column(db.String(10), nullable=False)
    IN_20 = db.Column(db.String(10), nullable=False)
    tb = db.Column(db.String(10), nullable=False)
    fc = db.Column(db.String(10), nullable=False)
    att = db.Column(db.String(10), nullable=False)
    punt_return_yds = db.Column(db.String(10), nullable=False)
    AVG_punt_retun_yards = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "punts": self.punts,
            "yards": self.yards,
            "AVG": self.AVG,
            "lng": self.lng,
            "net": self.net,
            "p_blk": self.p_blk,
            "IN_20": self.IN_20,
            "tb": self.tb,
            "fc": self.fc,
            "att": self.att,
            "punt_return_yds": self.punt_return_yds,
            "AVG_punt_retun_yards": self.AVG_punt_retun_yards,
            # do not serialize the password, its a security breach
        }


class Stats_Soccer_Team(db.Model):
    __tablename__ = "stats_soccer_team"
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    league = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    matches = db.Column(db.String(10), nullable=False)
    win = db.Column(db.String(5), nullable=False)
    loss = db.Column(db.String(10), nullable=False)
    pts = db.Column(db.String(10), nullable=False)
    goals_for = db.Column(db.String(10), nullable=False)
    goals_against = db.Column(db.String(10), nullable=False)
    more_2_5_goals = db.Column(db.String(10), nullable=False)
    less_2_5_goals = db.Column(db.String(10), nullable=False)
    zero_goal_against = db.Column(db.String(10), nullable=False)
    zero_goals_for = db.Column(db.String(10), nullable=False)
    ties = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "name": self.name,
            "league": self.league,
            "position": self.position,
            "matches": self.matches,
            "win": self.win,
            "loss": self.loss,
            "pts": self.pts,
            "goals_for": self.goals_for,
            "goals_against": self.goals_against,
            "more_2_5_goals": self.more_2_5_goals,
            "less_2_5_goals": self.less_2_5_goals,
            "zero_goal_against": self.zero_goal_against,
            "zero_goals_for": self.zero_goals_for,
            "ties": self.ties

            # do not serialize the password, its a security breach
        }


class Stats_Soccer_Player(db.Model):
    __tablename__ = "stats_soccer_player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    height = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(5), nullable=False)
    dorsal = db.Column(db.String(10), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    team = db.Column(db.String(30), nullable=False)
    games = db.Column(db.String(10), nullable=False)
    headshot = db.Column(db.String(30), nullable=False)

    strt = db.Column(db.String(10), nullable=False)
    fc = db.Column(db.String(10), nullable=False)
    fa = db.Column(db.String(10), nullable=False)
    yc = db.Column(db.String(10), nullable=False)
    rc = db.Column(db.String(10), nullable=False)
    goals = db.Column(db.String(10), nullable=False)
    ast = db.Column(db.String(10), nullable=False)
    sh = db.Column(db.String(10), nullable=False)
    st = db.Column(db.String(10), nullable=False)
    off = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "birth": self.birth,
            "position": self.position,
            "headshot": self.headshot,
            "dorsal": self.dorsal,
            "season": self.season,
            "team": self.team,
            "games": self.games,
            "strt": self.strt,
            "fc": self.fc,
            "fa": self.fa,
            "yc": self.yc,
            "rc": self.rc,
            "goals": self.goals,
            "ast": self.ast,
            "sh": self.sh,
            "st": self.st,
            "off": self.off

            # do not serialize the password, its a security breach
        }
