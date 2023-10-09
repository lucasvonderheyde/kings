class King:
    def __init__(self, name, age, gold, location, subject):

        self.name = name
        self.age = age 
        self.golf = gold
        location.king.append(self)
        subject.king.append(self)
        
    @property
    def outfit(self):
        return self._outfit

    @outfit.setter
    def outfit(self, new_outfit):

        self._outfit = new_outfit