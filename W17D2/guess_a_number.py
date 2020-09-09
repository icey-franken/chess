import random
randint = random.randint

playerName = input('Enter your name: ')
randNum = randint(1, 20)
numGuesses = 0
print('''
You have 6 attempts to guess a secret number.
The number is between 1 and 20.''')
while numGuesses < 6:
    numGuesses += 1
    userAnswer = int(input('''
Take a guess:
    '''))
    if userAnswer < randNum:
        print('''Your guess is too low''')
    elif userAnswer > randNum:
        print('''Your guess is too high''')
    else:
        print(f'''
        Great job {playerName}, you sonofagun!
        The secret number was {randNum}.
        You got it right in {numGuesses} guesses.
        ''')
        break
if userAnswer != randNum:
    print(f'''
Sorry {playerName}...


YOU LOSE''')
