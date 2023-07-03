import requests
from datetime import datetime
from EnvironmentHelper import EnvironementSetup


env_obj = EnvironementSetup()
BASE_URL = env_obj.get_base_url()
session = requests.session()
headers = {'Content-Type': 'application/json'}


def run(count):
    user_url = 'http://{}/api/users'.format(BASE_URL)
    start_date = datetime.now()
    for i in range(count):
        session.get(user_url, headers=headers)
    end_date = datetime.now()
    date_diff = end_date - start_date
    total_sec = date_diff.total_seconds()
    return total_sec

assert run(5000) < 5, "Time exceed than 5 seconds"
