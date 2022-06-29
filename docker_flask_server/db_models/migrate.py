from sqlalchemy import create_engine
from sqlalchemy.future import Engine
from sqlalchemy.orm import Session

from docker_flask_server.db_models.globals import mapper_registry

PROJECT_NAME = "docker_flask_server"

engine: Engine = create_engine(
    f"mariadb+pymysql://root:blog1234@{PROJECT_NAME}-database-1:3306/blog_schema?charset=utf8mb4",
    echo=True,
    future=True)


def make_migrations() -> object:
    mapper_registry.metadata.create_all(engine, checkfirst=True)


def __get_engine() -> object:
    return engine


def get_db_session():
    return Session(__get_engine())
