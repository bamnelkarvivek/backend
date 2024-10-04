import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='35.237.29.201',
        user='myuser',
        password='Vivek@1999',
        database='myappdb',
        port=3306
    )

# Function to register a new user
def register_user(username, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(insert_user_query, (username, password))
        conn.commit()  # Commit the transaction
        return True  # Return True if registration is successful
    except mysql.connector.Error as err:
        print(f"Error: {err}")  # Print the error message for debugging
        return False  # Return False if there is an error
    finally:
        # Ensure connection is closed even if an error occurs
        cursor.close()
        conn.close()


# Function to authenticate user login
def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

# **New Function** to get all users from the database
def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()  # Fetch all users
    cursor.close()
    conn.close()
    return users
