DROP TABLE IF EXISTS deposit_info;
DROP TABLE IF EXISTS withdraw_info;
DROP TABLE IF EXISTS account_info;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE account_info (
    account_id INTEGER PRIMARY KEY NOT NULL,
    acc_no TEXT NOT NULL UNIQUE,
    acc_type TEXT DEFAULT "Current" NOT NULL,
    user_id INTEGER NOT NULL,
    total_balance REAL DEFAULT 0.0 NOT NULL,
    acc_status TEXT DEFAULT "Inactive" NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE withdraw_info (
    amt_withdraw_id INTEGER PRIMARY KEY NOT NULL,
    account_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    amt_withdrawn TEXT DEFAULT 0.0 NOT NULL,
    withdraw_time DATETIME default current_timestamp,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (account_id) REFERENCES account_info(account_id)
);


CREATE TABLE deposit_info (
    amt_deposit_id INTEGER PRIMARY KEY NOT NULL,
    account_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    amt_deposit TEXT DEFAULT 0.0 NOT NULL,
    deposit_time DATETIME default current_timestamp,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (account_id) REFERENCES account_info(account_id)
);