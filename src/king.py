from human import Human

class King(Human):
    def __init__(self, age, name, gold, location, subject, is_hungry):
        super().__init__(self, age, name, gold, is_hungry)

        location.king.append(self)
        subject.king.append(self)
        
    @property
    def outfit(self):
        return self._outfit

    @outfit.setter
    def outfit(self, new_outfit):

        self._outfit = new_outfit