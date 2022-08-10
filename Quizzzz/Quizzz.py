from random import shuffle

class Quizzz:

    score = 0

    def __init__(self, que, crt_answ, answ):
        self.question=que
        self.correct_answer=crt_answ
        self.answers=answ
        for i in range(len(self.answers)):
            self.answers.insert(i, f"{i + 1}. {self.answers[i]}")
            self.answers.pop(i + 1)



    @property
    def start(self):

        if self.answers[0][int(input("Enter the answer number - ")) - 1] == self.correct_answer:
            Quizzz.score += 1
            return True
        else:
            return False

    def __repr__(self):
        return "\n" + self.question + "\n" + "\n".join(self.answers) + "\n" + f"Your points --> {Quizzz.score}"


example1 = Quizzz(que='What is the capital of Poland?', crt_answ="Warsaw",
              answ=['Minsk', 'Warsaw', 'Brest'])
example2 = Quizzz(que='What is the capital of USA?', crt_answ="Washington",
              answ=['Washington', 'Kazakhstan', 'Kentucky'])
example3 = Quizzz(que='What is the capital of Madagascar?', crt_answ="Antananarivo",
              answ=['Wakanda', 'Disney','Antananarivo'])

