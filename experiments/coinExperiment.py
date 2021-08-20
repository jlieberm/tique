__all__=['coinExperiment']

class coinExperiment():
    def __init__(self, Ntries):
        from randomElements import coin
        self.__coin = coin()
        self.__Ntries = Ntries
    
    def getProbability(self,side):
        cont = 0
        for n in range(self.__Ntries):
            self.__coin.flip()
            if self.__coin.side() == side:
                cont=cont+1
        return cont/self.__Ntries
