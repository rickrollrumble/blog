from sqlalchemy import create_engine

from logs_model import mapper_registry

engine = create_engine("postgresql+psycopg2://postgres:password@postgres2:5432/postgres", echo=True, future=True)


mapper_registry.metadata.create_all(engine, checkfirst=True)
