from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id: {}, name:{}>'.format(self.id, self.name)
