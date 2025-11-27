from flask import Flask
from .database import init_db




def create_app(test_config=None):
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
SECRET_KEY='dev',
DATABASE=app.instance_path + '/app.sqlite',
)


if test_config:
app.config.update(test_config)


try:
import os
os.makedirs(app.instance_path, exist_ok=True)
except OSError:
pass


# initialize database
init_db(app)


from .main import bp as main_bp
app.register_blueprint(main_bp)


return app