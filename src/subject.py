from human import Human

class Subject(Human):
    def __init__(self, age, name, gold, is_hungry):
        super().__init__(self, age, name, gold, is_hungry)

        self.king = []
    

    def pay_taxes(self, gold):
        pass

    @property
    def occupation(self):
        return self._occupation
    
    @occupation.setter
    def occupation(self, new_occupation):
        
        self._occupation = new_occupation