from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.orm import registry
mapper_registry = registry()
Base = mapper_registry.generate_base()


class User(Base):
    __tablename__ = 'http_requests_2'
    id = Column(Integer, primary_key=True)
    method = Column(String(10))
    host = Column(String(20))
    timestamp = Column(DateTime)





