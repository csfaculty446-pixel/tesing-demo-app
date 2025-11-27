import os
import tempfile
import pytest
from app import create_app
from app.database import get_db




@pytest.fixture
def app(tmp_path):
db_file = tmp_path / 'test_app.sqlite'
app = create_app({'TESTING': True, 'DATABASE': str(db_file)})
with app.app_context():
# init_db called in create_app
pass
yield app




@pytest.fixture
def client(app):
return app.test_client()




def test_signup_and_login(client):
# signup
resp = client.post('/signup', json={'username': 'tester', 'password': 'secret'})
assert resp.status_code == 201


# successful login
resp = client.post('/login', json={'username': 'tester', 'password': 'secret'})
assert resp.status_code == 200
assert resp.json['status'] == 'ok'


# bad login
resp = client.post('/login', json={'username': 'tester', 'password': 'wrong'})
assert resp.status_code == 401