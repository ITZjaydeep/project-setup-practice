import os
import sys
# import pickle
import numpy as np
import pandas as pd
import pymysql
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from dotenv import load_dotenv
# from sklearn.model_selection import GridSearchCV
# from sklearn.metrics import r2_score

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('SELECT * FROM students',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)