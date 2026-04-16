from random import randint
from brain_games.cli import welcome_user


name = welcome_user()


def main():
    print(f'Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        numbers = [randint(1,100), randint(1,100)]
        a, b = numbers[0], numbers[1]
        right_answer = 1
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                right_answer = i
                break
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

