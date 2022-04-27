from betterconf import Config, field
from betterconf.config import AbstractProvider

import json


class JsonProvider(AbstractProvider):
    SETTINGS_JSON_FILE = "srs/appsettings.json"

    def __init__(self):
        with open(self.SETTINGS_JSON_FILE, "r") as settings:
            self._settings = json.load(settings)

    def get(self, name):
        return self._settings.get(
            name)


class ConnectionString(Config):
    __CONNECTION_STRING = field("ConnectionStrings", provider=JsonProvider())

    def get(self, name):
        return self.__CONNECTION_STRING[name]


def config():
    return ConnectionString()
