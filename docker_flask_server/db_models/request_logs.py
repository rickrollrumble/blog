from sqlalchemy import Integer, Column, String, DateTime

from docker_flask_server.db_models.globals import Base


class Request(Base):
    __tablename__ = 'http_requests_2'
    id = Column(Integer, primary_key=True)
    method = Column(String(10))
    host = Column(String(30))
    timestamp = Column(DateTime)
