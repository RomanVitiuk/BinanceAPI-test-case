from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    url="sqlite:///crypto_db.sqlite", connect_args={"check_same_thread": False}
)

Base = declarative_base()
