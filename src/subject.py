class Subject:
    def __init__(self, name, age, gender, gold):

        self.name = name
        self.age = age
        self.gender = gender
        self.gold = gold
        self.king = []
    

    def pay_taxes(self, gold):
        pass

    @property
    def occupation(self):
        return self._occupation
    
    @occupation.setter
    def occupation(self, new_occupation):
        
        self._occupstion = new_occupation