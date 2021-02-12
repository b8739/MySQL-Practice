from flask import Flask, request, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from flask_mysqldb import MySQL
from config import DB_URL


app = Flask(__name__)
# app.config['UPLOADED_FILES_DEST'] = 'static/uploadsDB'
# configure_uploads(app,files)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
if __name__ == '__main__':
	app.run(debug=True)