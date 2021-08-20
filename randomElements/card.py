__all__=["card"]

class card():
    __suit=''
    __value=''
    __name=''
    def __init__(self, suit, value):
        if value == 1:
            self.__value = 'Ace'
        elif value == 11:
            self.__value = 'J'
        elif value == 12:
            self.__value = 'Q'
        elif value == 13:
            self.__value = 'K'
        else:
            self.__value = str(value)
        self.__suit = suit
    
    def __eq__(self, other):
        if (isinstance(other, card)): 
            return self.__suit == other.__suit and self.__value == other.__value

    def suit(self):
        return self.__suit
    
    def value(self):
        return self.__value
