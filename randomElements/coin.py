__all__ = ['coin']

class coin():
    __side = ''
    def __init__(self):
        self.__side = ''
        
    def side(self):
        return self.__side

    def flip(self):
        import numpy as np
        value = np.random.randint(2)
        if value == 0:
            self.__side = 'tails'
        else:
            self.__side = 'heads'
        return self.__side
