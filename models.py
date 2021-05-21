from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = "https://d3544la1u8djza.cloudfront.net/APHI/Blog/2020/11-19/Shiba+Inu+dog+with+a+burnt+orange+collar+and+silver+tag+resting+on+carpet-min.jpg"

# Models 
class Pet(db.Model):
    """Pet Model"""
    __tablename__ = 'pets' 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=DEFAULT_IMG_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)