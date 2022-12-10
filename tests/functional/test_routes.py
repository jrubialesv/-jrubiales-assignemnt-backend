from recipes_api import app, Recipes
import pytest

def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/recipes')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/recipes', json={'name': 'test', 'ingredients': 'test', 'steps': 'test', 'rate': 3, 'favorite': False})
    assert response.status_code == 200

def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<int:id>' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/recipes/1')
    assert response.status_code == 200

def test_update_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<int:id>' page is updated (PUT)
    THEN check the response is valid
    """
    response = testing_client.put('/recipes/1', json={'name': 'test', 'ingredients': 'test', 'steps': 'test', 'rate': 3, 'favorite': False})
    assert response.status_code == 200

def test_delete_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<int:id>' page is deleted (DELETE)
    THEN check the response is valid
    """
    response = testing_client.delete('/recipes/1')
    assert response.status_code == 200

def test_main_post(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is sent to (POST)
    THEN check the response is not valid
    """
    response = testing_client.post('/', json={'name': 'test', 'ingredients': 'test', 'steps': 'test', 'rate': 3, 'favorite': False})
    assert response.status_code == 405