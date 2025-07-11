python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'varsayilan-secret')
    DEBUG = True
    DATABASE_URI = 'sqlite:///db.sqlite3'