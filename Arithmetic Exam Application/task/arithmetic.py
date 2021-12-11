import random
num_of_correct_answers = 0


def task_generation():
    num_1 = random.randint(2, 9)
    num_2 = random.randint(2, 9)
    operations = ['+', '*', '-']
    operation = random.choice(operations)

    print_task(num_1, operation, num_2)
    check_input(num_1, operation, num_2)


def print_task(num_1, operation, num_2):
    if operation == '+':
        print(f'{num_1} + {num_2}')
    elif operation == '*':
        print(f'{num_1} * {num_2}')
    else:
        print(f'{num_1} - {num_2}')


def check_solution(num_1, operation, num_2, user_answer):
    global num_of_correct_answers

    if operation == '+':
        if user_answer == num_1 + num_2:
            print('Right!')
            num_of_correct_answers += 1
        else:
            print('Wrong!')
    elif operation == '*':
        if user_answer == num_1 * num_2:
            print('Right!')
            num_of_correct_answers += 1
        else:
            print('Wrong!')
    else:
        if user_answer == num_1 - num_2:
            print('Right!')
            num_of_correct_answers += 1
        else:
            print('Wrong!')


def check_input(num_1, operation, num_2):
    while True:
        try:
            user_answer = int(input())
        except ValueError:
            print('Incorrect format')
        else:
            check_solution(num_1, operation, num_2, user_answer)
            break


for i in range(5):
    task_generation()

print(f'Your mark is {num_of_correct_answers}/5')
