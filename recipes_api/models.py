from recipes_api import db
from datetime import datetime
import string, random

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(128), nullable=False)
    steps = db.Column(db.String(128), nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    favorite = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Event %r>' % self.id

    def __init__(self, name, ingredients, steps, rate, favorite):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.rate = rate
        self.favorite = favorite
        self.created_at = datetime.utcnow()
