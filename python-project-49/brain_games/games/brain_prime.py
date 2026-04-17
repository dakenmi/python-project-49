from random import randint
from brain_games.cli import welcome_user


name = welcome_user()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    while True:
        number = randint(1, 1000)
        print(f'Question: {number}')
        user_answer = input()
        right_answer = 'yes' if is_prime(number) else 'no'
        if user_answer == right_answer:
            print('Correct!')
        elif user_answer == 'exit':
            print(f'You found the secret button, see you next time, {name}!')
            break


if __name__ == "__main__":
    main()