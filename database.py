python
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base

engine = create_engine('sqlite:///db.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base.query = db_session.query_property()
Base.metadata.create_all(bind=engine)