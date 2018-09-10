
class Thing:

    def __init__ ( self, key, value ):
        self.key = key
        self.value = value

    def __str__ ( self ):
        return self.key + " " + self.value

class Thing2(Thing):

    def __init__ ( self, key, value, deeper_value ):
        super().__init__(key, value)
        self.deep_value = deeper_value

    def __str__ ( self ):
        return super().__str__() + self.deep_value
