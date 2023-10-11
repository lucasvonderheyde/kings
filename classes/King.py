from .Human import Human

class King(Human):
    def __init__(self, age, name, gold, difficulty, location, subject):
        super().__init__(age, name, gold)
        self.difficulty = difficulty
        location.king.append(self)
        subject.king.append(self)
        
    @property
    def outfit(self):
        return self._outfit

    @outfit.setter
    def outfit(self, new_outfit):

        self._outfit = new_outfit