class Castle:
    def __init__(self, biome, upkeep):

        self.upkeep = upkeep
        self.biome = biome
        self.king = []

    def refurbish(self, gold):
        pass

    @property
    def castle_name(self):
        return self._castle_name
    
    @castle_name.setter
    def castle_name(self, new_castle_name):
        
        self._castle_name = new_castle_name
        