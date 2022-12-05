import pytest
from recipes_api.models import Recipes
from recipes_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    app.app_context().push()
    db.create_all()
    account = Recipes('Test Account', 4, False, 'active')
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()
    app.app_context().pop() 
        