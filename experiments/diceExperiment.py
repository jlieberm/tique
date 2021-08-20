__all__=['dicexperiment']

class diceExperiment():
    __Ntries = 0
    def __init__(self,Ntries, sides):
        from randomElements.dice import dice
        self.__Ntries = Ntries
        self.__dice = dice(sides)

    def getProbability(self, number):
        cont=0
        for n in range(self.__Ntries):
            if self.__dice.throw() == number:
                cont = cont+1
        return cont/self.__Ntries