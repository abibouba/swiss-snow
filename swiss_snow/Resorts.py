from .parse_data import *


class Resorts:
    def __init__(self):
        self._list_resorts = ["Verbier"]

    @property
    def list_resorts(self):
        return self._list_resorts

    def conditions(self, resort):
        if resort.lower() == "verbier":
            return parse_website_verbier()
