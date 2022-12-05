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
<<<<<<< HEAD
        
    db.drop_all()
    app.app_context().pop() 
          

    
=======

    db.drop_all()
>>>>>>> 306cb88c730a326a788116c7a0d9adb81f072f19
