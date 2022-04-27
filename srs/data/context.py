from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from srs.helpers.settings import config


class ContextMonitoring:
    def __init__(self):
        self.__CONNECTION_STRING = config().get('Monitoring')
        self.__engine = create_engine(self.__CONNECTION_STRING)
        self.session_marker = sessionmaker(autoflush=False, bind=self.__engine)
