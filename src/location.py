class Location:
    def __init__(self, terrain, castle_name, upkeep):

        self.terrain = terrain
        self.castle_name = castle_name
        self.upkeep = upkeep
        self.king = []

    def refurbish(self, gold):
        pass

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        
        self._name = new_name
        