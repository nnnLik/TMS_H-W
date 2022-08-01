Que = [

    'Is it true that turtles cry?',
    'Is it true that Pushkin wrote the fairy tale "The Seven-Flowered Man"?',
    'Is it true that the very first cars were two-wheeled?',
    'Is it true that crocodiles can pretend to be logs to escape their enemies?',
    'Is it true that Australia is the largest continent?',
    'Is it true that pancakes are baked from rye flour?',
    'Is it true that Mars is the nearest planet to the Sun?',
    'Is it true that the Earth has more salt water than fresh water?',
    'Is it true that the jackal is a relative of the dog?',
    'Is it true that clay is used to make glass?',
    'Is it true that man has a middle ear?',
    'Is it true that an angry ladybug can bite?',
    'Is it true that archaeologists design buildings?',
    'Is it true that in chess the queen is more important than the queen?',
    'Is it true that polar bears, when hunting seals, cover their black noses with their paws?',
    'Is it true that the Japanese invented paper?',
    'Is it true that they saw with a hacksaw?',
    'Is it true that chickens bathe in dust - is it for good weather?',
    'Is it true that brown is made by mixing red and green?',
    'Is it true that there are ten vowel sounds in the Russian language?',

]

Answ = [

    'Yes', 'No', 'No', 'No',
    'No', 'No', 'No', 'Yes',
    'Yes', 'No', 'Yes', 'No',
    'No', 'No', 'No', 'No',
    ' Yes', 'No', 'Yes', 'No'

]
x = 0
cor_incor_counter = [0,0]

for i in Que:
    per_answ = str(input(i + ' (yes/no)\n')).lower()
    if per_answ == Answ[x].lower():
        print('correct')
        cor_incor_counter[0] += 1
    else:
        print('incorrect')
        cor_incor_counter[1] += 1

print(f'\nCorrect answer: {cor_incor_counter[0]} and Incorrect answer: {cor_incor_counter[1]}')

