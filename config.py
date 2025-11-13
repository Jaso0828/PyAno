

DATABASE_PATH = 'data_store/db/py_ano.db'

class AppConfig:
    def __init__(self, db_path: str = DATABASE_PATH):
       self.db_path = db_path
    