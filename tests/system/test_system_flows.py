import pytest
import time
import threading
import requests
from app import create_app




@pytest.fixture(scope='module')
def live_server():
# start flask app in a thread
app = create_app({'TESTING': True, 'DATABASE': ':memory:'})
port = 5005


server = threading.Thread(target=app.run, kwargs={'port': port})
server.daemon = True
server.start()
# give server time to start
time.sleep(1)
yield f'http://127.0.0.1:{port}'
# no explicit shutdown; thread is daemon




def test_index(live_server):
url = live_server + '/'
resp = requests.get(url)
assert resp.status_code == 200
assert resp.json().get('message') == 'Testing Demo App'




# Note: Selenium tests normally require a browser driver. This simple example uses requests to
# demonstrate a system-level test (starting the server and exercising HTTP endpoints).