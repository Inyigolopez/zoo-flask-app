import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'mysql-server-ilp.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'my-sqldb-ilp'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'inyigolopez'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'barLopi5622!'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storageaccountilp'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '6JeUsguKqs4y5Rou1fny1uIFTNJD2K/+FjmcJgHPF2hSGDF507nYw+iOI0xN6ouKsjvTuk8RjLHpXiRrqYIxyQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
