from recipes_api import db
from datetime import datetime
import string, random

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    favorite = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.id

    def __init__(self, name, rate, favorite, status):
        self.name = name
        self.rate = rate
        self.favorite = favorite
        self.status = status
        self.created_at = datetime.utcnow()