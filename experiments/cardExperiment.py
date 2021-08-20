__all__=['cardExperiment']

class cardExperiment():
    def __init__(self,cardList, Ntries, reposition=False):
        from randomElements.deck import deck
        self.__cardList = cardList
        self.__Ntries = Ntries
        self.__suits = ['hearts','clovers','spades','diamond']
        self.__values = [i for i in range(1,14)]
        self.__reposition = reposition
        self.__deck = deck(suits=self.__suits, values=self.__values)
    
    def jointProbability(self):
        cont = 0
        for i in range(self.__Ntries):
            temp = 0
            for card in self.__cardList:
                if self.__deck.drawRandomCard() == card:
                    temp  = temp+1
                    if self.__reposition:
                        self.__deck.addCard(card)
            if temp==len(self.__cardList):
                cont = cont+1
            self.__deck.reset()
        return cont/self.__Ntries

    def Ntries(self):
        return self.__Ntries