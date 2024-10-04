from flask import Flask
from routes.auth_routes import auth_blueprint
from routes.file_routes import file_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(file_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
