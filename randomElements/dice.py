__all__=['dice']

class dice():
    __sides = 0
    def __init__(self, sides):
        self.__sides = sides
    def throw(self):
        import numpy as np
        randomSide = np.random.randint(1,self.__sides+1)
        return randomSide
    def side(self):
        return self.__sides
    