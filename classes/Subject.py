from .Human import Human

class Subject(Human):
    def __init__(self, age, name, gold, castle, king, is_hungry=False):
        super().__init__(age, name, gold)
        self.is_hungry = is_hungry
        self.castle = castle
        self.king = king
        castle.subjects.append(self)
        king.subjects.append(self)
       
    def __repr__(self):
        return f"{self.name}, {self.age}"

    @property
    def occupation(self):
        return self._occupation
    
    @occupation.setter
    def occupation(self, new_occupation):
        
        self._occupation = new_occupation


    def pay_taxes(self, gold):
        pass