class Lift:
    def __init__(self, name, lift_type, status, sector):
        self.name = name
        self.lift_type = lift_type
        self.status = status
        self.sector = sector

    def __str__(self):
        return self.name + " " + self.lift_type + " " + self.status + " " + self.sector
