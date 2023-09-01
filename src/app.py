import os
from flask import Flask
from functools import wraps


class App:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.app = Flask(__name__)
        return cls._instance

    @property
    def route(self):
        return self._instance.app.route

    def run(self, args):
        self._instance.app.run(**args)


app = App()
