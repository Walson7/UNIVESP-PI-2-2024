from database import get_db_connection

def add_user(username, password):
    conn = get_db_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def get_user(username):
    conn = get_db_connection()
    if conn is None:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def add_account(user_id, name, balance):
    conn = get_db_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO accounts (user_id, name, balance) VALUES (%s, %s, %s)', (user_id, name, balance))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def add_transaction(account_id, amount, description, date):
    conn = get_db_connection()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO transactions (account_id, amount, description, date) VALUES (%s, %s, %s, %s)', (account_id, amount, description, date))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def get_accounts(user_id):
    conn = get_db_connection()
    if conn is None:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM accounts WHERE user_id = %s', (user_id,))
    accounts = cursor.fetchall()
    cursor.close()
    conn.close()
    return accounts

def get_transactions(account_id):
    conn = get_db_connection()
    if conn is None:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM transactions WHERE account_id = %s', (account_id,))
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return transactions
