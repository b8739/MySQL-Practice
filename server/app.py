from flask import Flask, request, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text, MetaData
from flask_mysqldb import MySQL
from config import DB_URL
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

app = Flask(__name__)
# app.config['UPLOADED_FILES_DEST'] = 'static/uploadsDB'
# configure_uploads(app,files)
engine = create_engine('mysql+mysqldb://root:root@localhost',echo = True)
# engine.execute("CREATE DATABASE newdatabase")
engine.execute("USE newdatabase")
# select new db
# use the new db
# continue with your work...

from model import *
meta = MetaData()
Base.metadata.create_all(engine)

if __name__ == '__main__':
	app.run(debug=True)