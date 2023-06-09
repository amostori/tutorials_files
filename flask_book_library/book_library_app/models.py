from book_library_app import db
from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: {self.first_name} {self.last_name}'


class AuthorSchema(Schema):
    # serializacja danych i walidacja
    # dump_only - pomiń przy walidacji
    # id będzie wykorzystywane tylko przy serializacji
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True, validate=validate.Length(max=50))
    last_name = fields.String(required=True, validate=validate.Length(max=50))
    birth_date = fields.Date('%d-%m-%Y', required=True)

    # Tworzenie własnej funkcji walidującej
    @validates('birth_date')
    def validate_birth_date(self, value):
        if value > datetime.now().date():
            raise ValidationError('Birth day must be lower than today')


# webargs służy do parsowania i sprawdzania poprawności danych w zapytaniach http
author_schema = AuthorSchema()
