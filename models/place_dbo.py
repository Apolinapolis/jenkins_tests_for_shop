class PlaceDbo:

    def __init__(self, id:int, dbo:bool = False, agr:bool = False):
        self.id = id
        self.dbo = dbo
        self.agr = agr

    def set_dbo(self, value:bool):
        self.dbo = value

    def set_agr(self, value:bool):
        self.agr = value