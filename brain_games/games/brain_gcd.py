from random import randint
from hexlet_projects.brain_games.scripts.cli import welcome_user


name = welcome_user()


def main():
    print(f'Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        numbers = [randint(1,1000), randint(1,1000)]
        if numbers[0] > numbers[1]:
            for i in range(numbers[1], 0):
                if numbers[0] % i == 0 and numbers[1] % i == 0:
                    right_answer = i
        elif numbers[1] > numbers[0]:
            for i in range(numbers[0], 0):
                if numbers[1] % i == 0 and numbers[0] % i == 0:
                    right_answer = i
        else:
            right_answer = numbers[0]
        print(f'Question: {numbers[0]} {numbers[1]}')
        user_answer = int(input())
        if user_answer == right_answer:
            if counter < 2:
                print('Correct!')
                counter += 1
            else:
                print(f'Congratulations, {name}!')
                counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break

