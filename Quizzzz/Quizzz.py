from random import shuffle

class Quizzz:

    score = 0

    def __init__(self,que, crt_answ, answ):
        self.question=que
        self.correct_answer = crt_answ
        self.answers = shuffle(answ)

    def start(self):

        print()

Que = [

    'The capital of Poland',
    'The capital of USA',
    'The capital of Madagascar'
]

Correct_answs = [

    'Warshawa',
    'Washington',
    'Antananarivo'

]

Answers = [

    ['Minsk', 'Warshawa', 'Brest'],
    ['Washington', 'Kazahstan', 'Kentucky'],
    ['Wakanda', 'Disney','Antananarivo']
]


example1=Quizzz(Que, Correct_answs, Answers)