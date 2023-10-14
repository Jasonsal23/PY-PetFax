from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ = 'facts'

    id = db.Column(db.Integer, primary_key=True)
    submitter = db.Column(db.String(50))
    fact = db.Column(db.Text)
    photo = db.Column(db.String(512))