import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy
from data.config import *

SqlAlchemyBase = orm.declarative_base()

__factory = None


def global_init(database_name):
    global __factory

    if __factory:
        return

    conn_str = sqlalchemy.URL(
        'mysql',
        username=username,
        password=password,
        host=host,
        database=database_name,
        port=3306,
        query={'charset': 'utf8mb4',
               'init_command': 'SET NAMES utf8mb4'}
    )
    engine = sa.create_engine(conn_str, pool_size=0, max_overflow=0)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
