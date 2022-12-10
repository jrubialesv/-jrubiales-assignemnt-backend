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
def create_recipe():
    name = request.json['name']
    ingredients = request.json['ingredients']
    steps = request.json['steps']
    rate = request.json['rate']
    favorite = request.json['favorite']
    new_recipe = Recipes(name, ingredients, steps, rate, favorite)
    db.session.add(new_recipe)
    db.session.commit()
    return format_recipe(new_recipe)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipes.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipes.query.get(id)
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipes.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.steps = request.json['steps']
    recipe.rate = request.json['rate']
    recipe.favorite = request.json['favorite']    

    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipes.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'steps': recipe.steps,
        'rate': recipe.rate,
        'favorite': recipe.favorite,
        'created_at': recipe.created_at
    }