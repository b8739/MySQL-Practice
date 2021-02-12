from flask import Flask, request, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
from flask_mysqldb import MySQL
from config import DB_URL
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import os

# EDA Packages
import pandas as pd 
import numpy as np 

Base = declarative_base()

app = Flask(__name__)
# app.config['UPLOADED_FILES_DEST'] = 'static/uploadsDB'
# configure_uploads(app,files)
engine = create_engine('mysql+mysqldb://root:root@localhost/newdatabase',echo = True)
# engine.execute("CREATE DATABASE newdatabase")
# engine.execute("USE newdatabase")
# select new db
# use the new db
# continue with your work...
# from csvConverter import *  

# create_all 작업   
# from model import *
# meta = MetaData()
# Base.metadata.create_all(engine)

# session 작업
# Session = sessionmaker(bind=engine)
# s = Session()
# john = User(user_id = '3', user_name='ssss', profile_url='b873s0.github.io')
# s.add(john)

# Commit the new User John to the database
# s.commit()
dataset_df = pd.read_csv(os.path.join('static','iris.csv'))
table_name = 'Dataset'
dataset_df.to_sql (
    table_name,
    engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    method='multi'
)


if __name__ == '__main__':
	app.run(debug=True)