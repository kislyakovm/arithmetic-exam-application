import random

num_of_correct_answers = 0
level = 0
level_info = ''


def task_generation_lvl_1():
    num_1 = random.randint(2, 9)
    num_2 = random.randint(2, 9)
    operations = ['+', '*', '-']
    operation = random.choice(operations)

    print_task(num_1, operation, num_2)
    check_input(num_1, operation, num_2)


def task_generation_lvl_2():
    num = random.randint(11, 29)
    operation = 'squaring'
    print_task(num, operation, num)
    check_input(num, operation, num)


def print_task(num_1, operation, num_2):
    if operation == '+':
        print(f'{num_1} + {num_2}')
    elif operation == '*':
        print(f'{num_1} * {num_2}')
    elif operation == '-':
        print(f'{num_1} - {num_2}')
    else:
        print(num_1)


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
    elif operation == '-':
        if user_answer == num_1 - num_2:
            print('Right!')
            num_of_correct_answers += 1
        else:
            print('Wrong!')
    else:
        if user_answer == num_1 ** 2:
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


def level_selection():
    global level_info
    if level == 1:
        level_info = '(simple operations with numbers 2-9)'
        for _ in range(5):
            task_generation_lvl_1()
    elif level == 2:
        level_info = '(integral squares of 11-29)'
        for _ in range(5):
            task_generation_lvl_2()
    else:
        print('Incorrect format')
        check_level_input()


def check_level_input():
    global level

    while True:
        print('''Which level do you want? Enter a number:
        1 - simple operations with numbers 2-9
        2 - integral squares of 11-29''')
        try:
            level = int(input())
        except ValueError:
            print('Incorrect format')
        else:
            level_selection()
            break


def write_to_file(user_name):
    file = open('results.txt', 'a', encoding='utf=8')
    file.write(f'{user_name}: {num_of_correct_answers}/5 in level {level} {level_info}\n')


def check_yes_input():
    yes = ['YES', 'Yes', 'yes', 'Y', 'y']
    user_input = input()

    if user_input in yes:
        print('What is your name?')
        user_name = input()
        print('The results are saved in "results.txt".')
        write_to_file(user_name)


check_level_input()

print(f'Your mark is {num_of_correct_answers}/5. Would you like to save the result? Enter yes or no.')
check_yes_input()
