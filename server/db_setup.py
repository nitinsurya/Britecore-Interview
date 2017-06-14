#!./bin/python3

from models import Base, engine

Base.metadata.create_all(engine)