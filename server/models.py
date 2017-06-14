from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///iws.db', echo=True)
Base = declarative_base()

class FeatureRequest(Base):
    __tablename__ = 'feature_requests'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    client = Column(String)
    client_priority = Column(Integer)
    date = Column(Date)
    product_area = Column(String)

    def __repr__(self):
        return "<FeatureRequest(title='%s', description='%s', client='%s')>" % (
            self.title, self.description, self.client)