import os
from flask_admin import Admin
from models import db, User, Noticias,Noticias_Skins, Skin , Deporte

from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'slate'
    admin = Admin(app, name='Admin', template_mode='bootstrap3')
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Noticias, db.session))
    admin.add_view(ModelView(Noticias_Skins, db.session))
    admin.add_view(ModelView(Skin, db.session))
    admin.add_view(ModelView(Deporte, db.session))
    

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
