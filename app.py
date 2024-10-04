from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection function for MySQL
def connect_db():
    connection = mysql.connector.connect(
        host='35.237.29.201',  # Replace with your instance public IP
        database='myappdb',  # Replace with your database name
        user='myuser',  # Replace with your MySQL user
        password='Vivek@1999',  # Replace with your password
        port=3306  # Default MySQL port
    )
    return connection

# Function to create user table if not exists
def create_user_table():
    conn = connect_db()
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

# Function to register a new user
def register_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    insert_user_query = 'INSERT INTO users (username, password) VALUES (%s, %s)'
    cursor.execute(insert_user_query, (username, password))
    conn.commit()
    cursor.close()
    conn.close()

# Function to authenticate user login
def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    select_user_query = 'SELECT * FROM users WHERE username = %s AND password = %s'
    cursor.execute(select_user_query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

# Function to get all users
def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    select_all_users_query = 'SELECT * FROM users'
    cursor.execute(select_all_users_query)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

# Flask route for registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        register_user(username, password)
        return jsonify({'message': 'User registered successfully!'}), 201
    return jsonify({'message': 'Invalid input!'}), 400

# Flask route for login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if authenticate_user(username, password):
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid username or password!'}), 401

# Flask route to get all users
@app.route('/users', methods=['GET'])
def users():
    users = get_all_users()
    user_list = [{'id': user[0], 'username': user[1], 'password': user[2]} for user in users]
    return jsonify(user_list), 200

# Main block
if __name__ == '__main__':
    create_user_table()
    app.run(debug=True, host='0.0.0.0')
