from sqlalchemy import create_engine

from docker_pgsql.logs_model import mapper_registry

engine = create_engine("postgresql+psycopg2://postgres:password@localhost:10432/postgres", echo=True, future=True)


mapper_registry.metadata.create_all(engine, checkfirst=True)
