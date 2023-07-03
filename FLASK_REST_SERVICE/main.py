from flask import Flask, request, jsonify
from db_connector import DBConnection


app = Flask(__name__)

db_obj = DBConnection()
db_obj.create_db_tables()


@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(db_obj.get_users())


@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(db_obj.get_user_by_id(user_id))


@app.route('/api/accounts', methods=['GET'])
def api_get_all_accounts():
    return jsonify(db_obj.get_accounts())


@app.route('/api/accounts/<account_id>', methods=['GET'])
def api_get_account(account_id):
    return jsonify(db_obj.get_account_by_id(account_id))


@app.route('/api/account_detail/<account_number>', methods=['GET'])
def api_get_account_detail(account_number):
    return jsonify(db_obj.get_account_detail_by_number(account_number))


@app.route('/api/users/add',  methods = ['POST'])
def api_add_user():
    return jsonify(db_obj.create_new_user(request.get_json()))


@app.route('/api/accounts/add',  methods = ['POST'])
def api_add_accounts():
    account = request.get_json()
    return jsonify(db_obj.create_user_account(account))


@app.route('/api/accounts/withdraws',  methods = ['POST'])
def api_amount_withdraws():
    withdraw_info = request.get_json()
    return jsonify(db_obj.account_withdraw_amount(withdraw_info))


@app.route('/api/accounts/deposits',  methods = ['POST'])
def api_amount_deposits():
    deposit_info = request.get_json()
    return jsonify(db_obj.account_deposit_amount(deposit_info))


@app.route('/api/accounts/send',  methods = ['POST'])
def api_amount_send():
    send_info = request.get_json()
    return jsonify(db_obj.send_amount(send_info))


if __name__ == "__main__":
    app.run()
