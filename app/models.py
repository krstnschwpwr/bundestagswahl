from app import db
from flask_sqlalchemy import *
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Bundesland(db.Model):
    __tablename__ = "bundesland"

    id = Column(Integer, primary_key=True)
    name = Column(db.String(255))
    wahlkreise = relationship('Wahlkreis', back_populates="Bundesland")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Bundesland {}>'.format(self.name)


class Wahlkreis(db.Model):
    __tablename__ = "wahlkreis"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    bundesland_id = Column(Integer, ForeignKey('bundesland.id'))
    bundesland = relationship("Bundesland", back_populates="Wahlkreis")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Wahlkreis {}>'.format(self.name)


class Partei(db.Model):
    __tablename__ = "partei"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Partei {}>'.format(self.name)


class Stimmen(db.Model):
    __tablename__ = "stimmen"

    id = db.Column(db.Integer, primary_key=True)
    erststimme = db.Column(db.String(255))
    zweitstimme = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Stimmen {}>'.format(self.id)