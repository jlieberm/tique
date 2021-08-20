__all__=["deck"]

from randomElements.card import card
class deck():
    __cards=list()
    __suits=''
    __values=''
    def __init__(self, suits, values):
        self.__suits = suits
        self.__values = values
        for suit in suits:
            for value in values:
                self.__cards.append(card(value=value, suit=suit))

    def removeCard(self, card):
        self.__cards.remove(card)
    def addCard(self, card):
        self.__cards.append(card)
    def NCards(self):
        return len(self.__cards)
    def drawRandomCard(self):
        import numpy as np
        index = np.random.randint(len(self.__cards))
        card = self.__cards[index]
        self.__cards.remove(card)
        return card
    def listCards(self):
        for card in self.__cards:
            print (card.value() + ' of ' + card.suit())
    def reset(self):
        self.__cards.clear()
        for suit in self.__suits:
            for value in self.__values:
                self.__cards.append(card(value=value, suit=suit))



