from random import randint
from cli import welcome_user


name = welcome_user()



def currentElement():
    start = randint(1,20)
    step = randint(1, 9)
    progression = [start]
    for index in range(1,9):
        progression.append(start + step)
    return progression


def main():
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        progression = currentElement()
        random = randint(0, 9)
        right_answer = progression[random]
        progression[random] = '..'
        question = ' '.join(progression)
        print(f"Question: {question}")
        user_answer = int(input())
        if user_answer == right_answer and counter < 2:
            print('Correct!')
            counter += 1
        elif user_answer == right_answer and counter == 2:
            print(f'Congratulations, {name}!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
