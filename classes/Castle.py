class Castle:
    castles = []
    def __init__(self, biome, difficulty, upkeep):

        self.difficulty = difficulty
        self.upkeep = upkeep
        self.biome = biome
        self.subjects = []



    @property
    def castle_name(self):
        return self._castles_name
    
    @castle_name.setter
    def castle_name(self, new_castle_name):
        
        self._castle_name = new_castle_name
    

    def refurbish(self, gold):
        pass