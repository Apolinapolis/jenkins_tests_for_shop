class PlaceDbo:
    """Имитирует place из БД"""
    def __init__(self, name:str, dbo:bool = False, agr:bool = False):
        self.name = name
        self.dbo = dbo
        self.agr = agr