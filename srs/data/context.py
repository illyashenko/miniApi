from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from srs.helpers.settings import config


class ContextMonitoring:
    def __init__(self):
        self.__CONNECTION_STRING = config.get('Monitoring')
        self.engine = create_engine(self.__CONNECTION_STRING)
        self.session = Session(self.engine)
