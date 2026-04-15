from random import randint
from random import choice
from cli import welcome_user

name = welcome_user()


def main():
    print(f'What is the result of the expression?')
    counter = 0
    example = [0, 'x', 0]
    symbols = ['+', '-', '*', '/']
    while counter < 3:
        for i in range(0,3):
            if i == 0 or i == 2:
                i = randint(1,1000)
            else:
                i = choice(symbols)
        op = example[1]
        if op == '+':
            right_answer = example[0] + example[2]
        elif op == '-':
            right_answer = example[0] - example[2]
        elif op == '*':
            right_answer = example[0] * example[2]
        else:
            right_answer = example[0] / example[2]
        print(f'Question: {example[0]} {example[1]} {example[2]}')
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


