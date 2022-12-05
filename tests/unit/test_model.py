from recipes_api.models import Recipes
import pytest

def test_create_recipes():
    """
    GIVEN a Recipes model
    WHEN a new Recipe is created
    THEN check the name, 
    """
<<<<<<< HEAD
    recipe = Recipes('test', 3, False)
    assert recipe.name == 'test'
    assert recipe.rate == 3    
    assert recipe.favorite == False
=======
    recipe = Recipes('test', 3, False, 'active')
    assert recipe.name == 'test'
    assert recipe.rate == 3    
    assert recipe.favorite == False
    assert recipe.status == 'active'
>>>>>>> 306cb88c730a326a788116c7a0d9adb81f072f19
