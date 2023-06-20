from os import getcwd
from os.path import join, isfile

from database.db.base_db import Base, engine
from database.cryptocurrency_model import CryptoData


def init_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    db_name = "crypto_db.sqlite"
    db_file_path = join(getcwd(), db_name)
    if not isfile(db_file_path):
        init_db()
