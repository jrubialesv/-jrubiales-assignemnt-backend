from recipes_api.models import Recipes
import pytest

def test_create_recipes():
    """
    GIVEN a Recipes model
    WHEN a new Recipe is created
    THEN check the name, 
    """
    recipe = Recipes('test', 3, False, 'active')
    assert recipe.name == 'test'
    assert recipe.rate == 3    
    assert recipe.favorite == False
    assert recipe.status == 'active'
