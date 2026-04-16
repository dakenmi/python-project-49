from random import randint
from brain_games.cli import welcome_user


name = welcome_user()



def current_element():
    start = randint(1,20)
    step = randint(1, 9)
    progression = []
    for index in range(10):
        progression.append(start + step * index)
    return progression


def main():
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        progression = current_element()
        random = randint(0, 8)
        right_answer = progression[random]
        progression[random] = '..'
        question = ' '.join(map(str,progression))
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
