from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

demo = Flask(__name__)
db = SQLAlchemy(demo)
demo.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite://database.db'
demo.config['SECRET_KEY'] = 'thisisasecretkey'

class User(db.Model,UserMixin):
    id=db.Column(db.String,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(80), nullable=False)


@demo.route('/')
def home():
    return render_template('demo.html')

@demo.route('/')
def register():
    return render_template('register.html')

@demo.route('/')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    demo.run(debug=True)
    