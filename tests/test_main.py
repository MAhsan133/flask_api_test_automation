import requests
import json
from EnvironmentHelper import EnvironementSetup


class TestRestAPI:

    @classmethod
    def setup_class(cls):
        env_obj = EnvironementSetup()
        cls.BASE_URL = env_obj.get_base_url()
        cls.session = requests.session()
        cls.headers = {'Content-Type': 'application/json'}

    # GET method - ALL Users - Verify total records=0 and response=200
    def test_0001_get_all_users1(self):
        user_url = 'http://{}/api/users'.format(self.BASE_URL)
        resp = self.session.get(user_url, headers=self.headers)
        total_records = len(json.loads(resp.text))
        assert resp.status_code == 200
        assert total_records == 0

    # POST method - Create New user 1 with custom data in request body
    def test_0002_post_create_user1(self):
        user_url = 'http://{}/api/users/add'.format(self.BASE_URL)
        user_data = {
            "name": "Paul Serice",
            "email": "paul.serice@gamil.com",
            "phone": "067765434567",
            "address": "Paul Serice Street, Innsbruck",
            "country": "Austria"
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"

    # POST method - Create New user 2 with custom data in request body
    def test_0003_post_create_user2(self):
        user_url = 'http://{}/api/users/add'.format(self.BASE_URL)
        user_data = {
            "name": "James Bond",
            "email": "james.bond@gamil.com",
            "phone": "067765434567",
            "address": "James Bond Street, Innsbruck",
            "country": "Austria"
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"

    # GET method - ALL Users - Verify total records=2 and response=200
    def test_0004_get_all_users2(self):
        user_url = 'http://{}/api/users'.format(self.BASE_URL)
        resp = self.session.get(user_url, headers=self.headers)
        total_records = len(json.loads(resp.text))
        assert resp.status_code == 200
        assert total_records == 2

    # GET method - ALL Accounts - Verify total records=0 and response=200
    def test_0005_get_all_accounts1(self):
        user_url = 'http://{}/api/accounts'.format(self.BASE_URL)
        resp = self.session.get(user_url, headers=self.headers)
        total_records = len(json.loads(resp.text))
        assert resp.status_code == 200
        assert total_records == 0

    # POST method - Create New account 1 with custom data
    def test_0006_post_create_account1(self):
        user_url = 'http://{}/api/accounts/add'.format(self.BASE_URL)
        user_data = {
                "acc_no": "MEZN11223344556688",
                "acc_status": "Active",
                "total_balance": 500,
                "user_id": 1
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"

    # POST method - Create New account 2 with custom data
    def test_0007_post_create_account2(self):
        user_url = 'http://{}/api/accounts/add'.format(self.BASE_URL)
        user_data = {
            "acc_no": "SCB11223344556688",
            "acc_status": "Active",
            "total_balance": 600,
            "user_id": 2
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"

    # GET method - ALL Accounts - Verify total records=2 and response=200
    def test_0008_get_all_accounts2(self):
        user_url = 'http://{}/api/accounts'.format(self.BASE_URL)
        resp = self.session.get(user_url, headers=self.headers)
        total_records = len(json.loads(resp.text))
        assert resp.status_code == 200
        assert total_records == 2

    # POST method - Amount withdraw from account with in available balance
    def test_0009_post_withdraw_amount(self):
        user_url = 'http://{}/api/accounts/withdraws'.format(self.BASE_URL)
        user_data = {
            "acc_no": "MEZN11223344556688",
            "amt_withdrawn": 300
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"

    # GET method - Account Detail - Verify balance = 200
    def test_0010_get_account_balance(self):
        user_url = 'http://{}/api/account_detail/{}'.format(self.BASE_URL, "MEZN11223344556688")
        resp = self.session.get(user_url, headers=self.headers)
        json_resp = json.loads(resp.text)
        assert resp.status_code == 200
        assert json_resp['total_balance'] == 200

    # POST method - Amount withdraw with more than available balance
    def test_0011_post_withdraw_amount_error(self):
        user_url = 'http://{}/api/accounts/withdraws'.format(self.BASE_URL)
        user_data = {
            "acc_no": "MEZN11223344556688",
            "amt_withdrawn": 300
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Message'] == "Insufficient Balance"

    # POST method - Amount deposit
    def test_0012_post_deposit_amount(self):
        user_url = 'http://{}/api/accounts/deposits'.format(self.BASE_URL)
        user_data = {
            "acc_no": "MEZN11223344556688",
            "amt_deposit": 200
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"

    # GET method - Account Detail - Verify balance = 400
    def test_0013_get_verify_updated_account_balance(self):
        user_url = 'http://{}/api/account_detail/{}'.format(self.BASE_URL, "MEZN11223344556688")
        resp = self.session.get(user_url, headers=self.headers)
        json_resp = json.loads(resp.text)
        assert resp.status_code == 200
        assert json_resp['total_balance'] == 400

    # POST method - Send Amount to other account
    def test_0014_post_send_amount(self):
        user_url = 'http://{}/api/accounts/send'.format(self.BASE_URL)
        user_data = {
            "from_acc_no": "MEZN11223344556688",
            "to_acc_no": "SCB11223344556688",
            "amt_withdrawn": 300
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"
        assert json.loads(resp.text)['Message'] == 'Amount Transfer successfully.'

    # GET method - Account Detail - Verify Sender balance = 100
    def test_0015_get_verify_updated_sender_balance(self):
        user_url = 'http://{}/api/account_detail/{}'.format(self.BASE_URL, "MEZN11223344556688")
        resp = self.session.get(user_url, headers=self.headers)
        json_resp = json.loads(resp.text)
        assert resp.status_code == 200
        assert json_resp['total_balance'] == 100

    # GET method - Account Detail - Verify Receiver balance = 900
    def test_0016_get_verify_updated_receiver_balance(self):
        user_url = 'http://{}/api/account_detail/{}'.format(self.BASE_URL, "SCB11223344556688")
        resp = self.session.get(user_url, headers=self.headers)
        json_resp = json.loads(resp.text)
        assert resp.status_code == 200
        assert json_resp['total_balance'] == 900

    # POST method - Send Amount to other account - Insufficient balance
    def test_0017_post_send_amount_insufficient(self):
        user_url = 'http://{}/api/accounts/send'.format(self.BASE_URL)
        user_data = {
            "from_acc_no": "MEZN11223344556688",
            "to_acc_no": "SCB11223344556688",
            "amt_withdrawn": 300
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"
        assert json.loads(resp.text)['Message'] == 'Insufficient Balance.'

    # POST method - Send Amount from other account
    def test_0018_post_send_amount_from_other(self):
        user_url = 'http://{}/api/accounts/send'.format(self.BASE_URL)
        user_data = {
            "from_acc_no": "SCB11223344556688",
            "to_acc_no": "MEZN11223344556688",
            "amt_withdrawn": 500
        }
        resp = self.session.post(url=user_url, json=user_data, headers=self.headers)
        assert resp.status_code == 200
        assert json.loads(resp.text)['Status'] == "Passed"
        assert json.loads(resp.text)['Message'] == 'Amount Transfer successfully.'

    # GET method - Account Detail - Verify Sender balance = 400
    def test_0019_get_verify_other_sender_balance(self):
        user_url = 'http://{}/api/account_detail/{}'.format(self.BASE_URL, "SCB11223344556688")
        resp = self.session.get(user_url, headers=self.headers)
        json_resp = json.loads(resp.text)
        assert resp.status_code == 200
        assert json_resp['total_balance'] == 400

    # GET method - Account Detail - Verify Receiver balance = 600
    def test_0020_get_verify_updated_receiver_balance(self):
        user_url = 'http://{}/api/account_detail/{}'.format(self.BASE_URL, "MEZN11223344556688")
        resp = self.session.get(user_url, headers=self.headers)
        json_resp = json.loads(resp.text)
        assert resp.status_code == 200
        assert json_resp['total_balance'] == 600
