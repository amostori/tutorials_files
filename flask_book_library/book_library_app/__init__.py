from datetime import date
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#
#     for row in results:
#         print(row)

from book_library_app import authors
from book_library_app import models
from book_library_app import db_manage_commands
from book_library_app import errors

# a1 = models.Author(first_name="Jan", last_name="Kowalski", birth_day=date(1990, 1, 1))
# a2 = models.Author(first_name="Ola", last_name="Kowalska", birth_day=date(1991, 1, 1))

# with app.app_context():
#     db.create_all()
#     db.session.add(a1)
#     db.session.add(a2)
#     db.session.commit()
#     db.drop_all()
