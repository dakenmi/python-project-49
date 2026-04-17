from random import randint

from brain_games.cli import welcome_user

name = welcome_user()


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    trying = 0
    while trying < 3:
        number = randint(1, 1000)
        print(number)
        if number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

        print(f'Question: {number}')

        user_answer = input()

        if user_answer == answer:
            trying += 1
            if trying == 3:
                print(f'Congratulations, {name}!')
            else:
                print('Correct!')

        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()
