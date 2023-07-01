#!/usr/bin/python
import sqlite3


class DBConnection(object):
    def __init__(self):
        self.db_name = 'database.db'

    def connect_to_db(self):
        conn = sqlite3.connect(self.db_name)
        return conn

    def create_db_tables(self):
        connection = self.connect_to_db()
        with open('schema.sql') as f:
            connection.executescript(f.read())
        connection.close()

    def create_new_user(self, user):
        inserted_user = {}
        connection = self.connect_to_db()
        try:
            cur = connection.cursor()
            cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)", (
                user['name'], user['email'], user['phone'], user['address'], user['country']))
            connection.commit()
            inserted_user = self.get_user_by_id(cur.lastrowid)
        except:
            connection.rollback()
        finally:
            connection.close()
        return inserted_user

    def create_user_account(self, account_info):
        inserted_account = {}
        connection = self.connect_to_db()
        try:
            cur = connection.cursor()
            cur.execute("INSERT INTO account_info (acc_no, acc_status, total_balance, user_id) VALUES (?, ?, ?, ?)", (
                account_info['acc_no'], account_info['acc_status'], account_info['total_balance'],
                account_info['user_id']))
            connection.commit()
            inserted_account = self.get_account_by_id(cur.lastrowid)
        except:
            connection.rollback()
        finally:
            connection.close()
        return inserted_account

    def update_user_balance(self, connection, cur, account_id, balance):
        try:
            cur.execute("UPDATE account_info SET total_balance = ? WHERE account_id = ?;", (balance, account_id))
            connection.commit()
        except:
            connection.rollback()

    def account_withdraw_amount(self, account_info):
        withdraw_amount = {}
        connection = self.connect_to_db()
        try:
            cur = connection.cursor()
            account_dict = self.get_account_by_id(account_info['account_id'])
            if account_dict['total_balance'] >= account_info['amt_withdrawn']:
                balance = account_dict['total_balance'] - account_info['amt_withdrawn']
                self.update_user_balance(connection, cur, account_info['account_id'], balance)
                cur.execute("INSERT INTO withdraw_info (account_id, user_id, amt_withdrawn) VALUES (?, ?, ?)", (
                    account_info['account_id'], account_dict['user_id'], account_info['amt_withdrawn']))
                connection.commit()
                withdraw_amount = self.get_amount_withdraw_by_id(account_info['account_id'])
            else:
                withdraw_amount = {"Message": "Insufficient Balance"}
        except:
            connection.rollback()
        finally:
            connection.close()
        return withdraw_amount

    def account_deposit_amount(self, account_info):
        deposit_amount = {}
        connection = self.connect_to_db()
        try:
            cur = connection.cursor()
            account_dict = self.get_account_by_id(account_info['account_id'])
            balance = account_dict['total_balance'] + account_info['amt_deposit']
            self.update_user_balance(connection, cur, account_info['account_id'], balance)
            cur.execute("INSERT INTO deposit_info (account_id, user_id, amt_deposit) VALUES (?, ?, ?)", (
                account_info['account_id'], account_dict['user_id'], account_info['amt_deposit']))
            connection.commit()
            deposit_amount = self.get_amount_deposit_by_id(account_info['account_id'])
        except:
            connection.rollback()
        finally:
            connection.close()
        return deposit_amount

    def get_users(self):
        users = []
        try:
            conn = self.connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            for i in rows:
                user = {"user_id": i["user_id"], "name": i["name"], "email": i["email"], "phone": i["phone"],
                        "address": i["address"], "country": i["country"]}
                users.append(user)
        except:
            users = []
        return users

    def get_user_by_id(self, user_id):
        user = {}
        try:
            conn = self.connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = cur.fetchone()
            user["user_id"] = row["user_id"]
            user["name"] = row["name"]
            user["email"] = row["email"]
            user["phone"] = row["phone"]
            user["address"] = row["address"]
            user["country"] = row["country"]
        except:
            user = {}
        return user

    def get_account_by_id(self, account_id):
        account = {}
        try:
            conn = self.connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM account_info WHERE account_id = ?", (account_id,))
            row = cur.fetchone()
            account["account_id"] = row["account_id"]
            account["user_id"] = row["user_id"]
            account["acc_no"] = row["acc_no"]
            account["acc_type"] = row["acc_type"]
            account["total_balance"] = row["total_balance"]
            account["acc_status"] = row["acc_status"]
        except:
            account = {}
        return account

    def get_amount_withdraw_by_id(self, account_id):
        wd_account = {}
        try:
            conn = self.connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM withdraw_info WHERE account_id = ?", (account_id,))
            row = cur.fetchone()
            wd_account["amt_withdraw_id"] = row["amt_withdraw_id"]
            wd_account["user_id"] = row["user_id"]
            wd_account["amt_withdrawn"] = row["amt_withdrawn"]
            wd_account["withdraw_time"] = row["withdraw_time"]
        except:
            wd_account = {}
        return wd_account

    def get_amount_deposit_by_id(self, account_id):
        wd_account = {}
        try:
            conn = self. connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM deposit_info WHERE account_id = ?", (account_id,))
            row = cur.fetchone()
            wd_account["amt_deposit_id"] = row["amt_deposit_id"]
            wd_account["user_id"] = row["user_id"]
            wd_account["amt_deposit"] = row["amt_deposit"]
            wd_account["deposit_time"] = row["deposit_time"]
        except:
            wd_account = {}
        return wd_account
