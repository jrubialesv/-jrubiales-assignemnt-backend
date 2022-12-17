import pytest
from recipes_api.models import Recipes
from recipes_api import db, app

@pytest.fixture
def testing_client(scope='module'):
    
    db.create_all()
    account = Recipes('Test Account', 'test', 'test', 3, False)
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()
        
