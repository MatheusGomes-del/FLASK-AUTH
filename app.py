from flask import Flask
from models.user import User
from database import db
from flask_login import LoginManager
import os

load.dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)



@app.route("/", methods=['GET'])
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)