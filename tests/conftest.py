import pytest
from recipes_api.models import Recipes
from recipes_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    app.app_context().push()
    db.create_all()
    recipe = Recipes('Test Recipe', 3)
    db.session.add(recipe)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client
        
    db.drop_all()
    app.app_context().pop() 
          

    