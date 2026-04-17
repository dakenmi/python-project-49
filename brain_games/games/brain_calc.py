from random import choice, randint

from brain_games.cli import welcome_user

name = welcome_user()


def main():
    print('What is the result of the expression?')
    counter = 0
    example = [0, 'x', 0]
    symbols = ['+', '-', '*']
    while counter < 3:
        example[0] = randint(1, 50)
        example[2] = randint(1, 50)
        example[1] = choice(symbols)
        op = example[1]
        if op == '+':
            right_answer = example[0] + example[2]
        elif op == '-':
            right_answer = example[0] - example[2]
        else:
            right_answer = example[0] * example[2]
        print(f'Question: {example[0]} {example[1]} {example[2]}')
        user_answer = int(input())
        if user_answer == right_answer and counter < 2:
            print('Correct!')
            counter += 1
        elif user_answer == right_answer and counter == 2:
            print(f'Congratulations, {name}!')
            counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()
