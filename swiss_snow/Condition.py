class Condition:
    def __init__(self, location="", altitude="", snow_height="", snow_fresh=""):
        self.location = location
        self.altitude = altitude
        self.snow_height = snow_height
        self.snow_fresh = snow_fresh

    def __str__(self):
        return self.location + " (" + self.altitude + "): " + self.snow_height + " - Fresh snow: " + self.snow_fresh
