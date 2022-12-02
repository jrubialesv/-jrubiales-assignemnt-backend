from flask import Flask, request
from recipes_api import db, app
from recipes_api.models import Recipes


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi! This is the BACKEND SKULL! 💀'


@app.route('/recipes', methods=['POST'])
def create_account():
    name = request.json['name']
    rate = request.json['rate']
    favorite = request.json['favorite']
    status = request.json['status']

    new_recipe = Recipes(name, rate, favorite)
    db.session.add(new_recipe)
    db.session.commit()
    return format_recipe(new_recipe)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipes.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    account = Recipes.query.get(id)
    return format_recipe(account)

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipes.query.get(id)
    recipe.name = request.json['name']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipes.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(account):
    return {
        'id': account.id,
        'name': account.name,
        'rate': account.rate,
        'favorite': account.favorite,
        'created_at': account.created_at,
        'status': account.status
    }