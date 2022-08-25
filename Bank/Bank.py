from random import choice
from string import digits

class Card:
    def __init__(self, pin):
        self.__bank_acc = 0
        self.__pin = pin

    @property
    def acc(self):
        if self.__pin == int(input()):
            return self.__bank_acc

    @acc.setter
    def acc(self, val):
        self.__bank_acc = val

my_acc = Card(1234)
my_acc.acc += 1213
print(my_acc.acc)