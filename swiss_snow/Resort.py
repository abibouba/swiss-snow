from datetime import datetime

from .Condition import Condition


class Resort:
    def __init__(self):
        """Initialize the ResortStatus object."""
        self._name = ""
        self._slopes_open = 0
        self._slopes_total = 0
        self._lifts_open = 0
        self._lifts_total = 0
        self._avalanche_level = 0
        self.conditions = []
        self._last_update = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def slopes_open(self):
        return self._slopes_open

    @slopes_open.setter
    def slopes_open(self, slopes_open):
        if slopes_open.isdigit():
            self._slopes_open = int(slopes_open)

    @property
    def slopes_total(self):
        return self._slopes_total

    @slopes_total.setter
    def slopes_total(self, slopes_total):
        if slopes_total.isdigit():
            self._slopes_total = int(slopes_total)

    @property
    def lifts_open(self):
        return self._lifts_open

    @lifts_open.setter
    def lifts_open(self, lifts_open):
        if lifts_open.isdigit():
            self._lifts_open = int(lifts_open)

    @property
    def lifts_total(self):
        return self._lifts_total

    @lifts_total.setter
    def lifts_total(self, lifts_total):
        if lifts_total.isdigit():
            self._lifts_total = int(lifts_total)

    @property
    def avalanche_level(self):
        return self._avalanche_level

    @avalanche_level.setter
    def avalanche_level(self, avalanche_level):
        if avalanche_level.isdigit():
            if 0 <= avalanche_level <= 5:
                self._avalanche_level = avalanche_level

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        if isinstance(last_update, datetime):
            self._last_update = last_update

    def add_condition(self, location, altitude, snow_height, snow_fresh):
        condition = Condition(location=location, altitude=altitude, snow_height=snow_height, snow_fresh=snow_fresh)
        self.conditions.append(condition)

    def __str__(self):
        return self.name + " - Avalanche risk: " + str(self.avalanche_level) + " - Open slopes: " \
               + str(self.slopes_open) + "/" + str(self.slopes_total) + " - Open lifts: " + str(self.lifts_open) + "/" + \
               str(self.lifts_total) + " - Last update: " + str(self.last_update)
