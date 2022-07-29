import random

class Dice:

    def throw(faces=6):

        ur_int = random.randint(1, faces)
        print(ur_int)

Dice.throw()


