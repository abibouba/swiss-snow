class Slope:
    def __init__(self, name="", slope_level="", is_open=False, sector=""):
        self.name = name
        self._slope_level = slope_level
        self._is_open = is_open
        self.sector = sector

    def __str__(self):
        return self.name + " " + self.slope_level + " " + self.status + " " + self.sector

    @property
    def slope_level(self):
        return self._slope_level

    @slope_level.setter
    def slope_level(self, slope_level):
        if ["green", "blue", "red", "black", "yellow"] in slope_level.lower():
            _slope_level = slope_level.lower()

    @property
    def is_open(self):
        return self._is_open

    @is_open.setter
    def status(self, is_open):
        if isinstance(is_open, bool):
            _is_open = is_open
