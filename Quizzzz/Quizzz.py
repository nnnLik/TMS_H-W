from random import shuffle

class Quizzz:

    score = 0

    def __init__(self, que, crt_answ, answ):
        self.question=que
        self.correct_answer=crt_answ
        self.answers=answ
        shuffle(self.answers)
        self.list_out()

    def list_out(self):
        for i in range(len(self.answers)):
            self.answers.insert(i, f"{i + 1}. {self.answers[i]}")
            self.answers.pop(i + 1)

    @property
    def start(self):
        if self.answers[int(input("Enter the answer number - ")) - 1][3:] == self.correct_answer:
            Quizzz.score += 1
            return True
        else:
            return False

    def __str__(self):
        return "\n" + self.question + "\n" + "\n".join(self.answers) + "\n" + f"Your points --> {Quizzz.score}"

Que = [

    'The capital of Poland',
    'The capital of USA',
    'The capital of Madagascar'
]

Correct_answs = [

    'Warsaw',
    'Washington',
    'Antananarivo'

]

Answers = [

    ['Minsk', 'Warshawa', 'Brest'],
    ['Washington', 'Kazakhstan', 'Kentucky'],
    ['Wakanda', 'Disney','Antananarivo']
]


example1=Quizzz(Que, Correct_answs, Answers)

print(example1.start)