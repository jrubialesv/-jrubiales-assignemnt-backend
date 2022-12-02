from recipes_api.models import Recipes
import pytest

def test_create_recipes():
    """
    GIVEN a Recipes model
    WHEN a new Recipe is created
    THEN check the name, 
    """
    account = Recipes('test', 3, False)
    assert account.name == 'test'
    assert account.rate == 3    
    assert account.favorite == False