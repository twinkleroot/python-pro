import random

def input_number(min, max):
    random_number = int(input('Enter the number of your choice: '))
    if(min > random_number or random_number > max):
        random_number = int(input(f'Enter the number of your choice from {min} to {max}: '))
    return options[random_number - 1]

def judge_rock_paper_scissors(human_choice, win_to_human_choice, lose_to_human_choice):
    if human_choice == human_choice:
        if computer_choice == win_to_human_choice:
            print(f'Sorry, {win_to_human_choice} beat {human_choice}')
        elif computer_choice == lose_to_human_choice:
            print(f'Yes, {human_choice} beat {lose_to_human_choice}')
        else:
            print('Draw!')

options = ['rock', 'paper', 'scissors']
print('(1) Rock\n(2) Paper\n(3) Scissors')
human_choice = input_number(1, len(options))
print(f'You chose {human_choice}')
computer_choice = random.choice(options)
print(f'The computer chose {computer_choice}')
judge_rock_paper_scissors(human_choice, )
# if human_choice == 'rock':
#     if computer_choice == 'paper':
#         print('Sorry, paper beat rock')
#     elif computer_choice == 'scissors':
#         print('Yes, rock beat scissors')
#     else:
#         print('Draw!')
# elif human_choice == 'paper':
#     if computer_choice == 'scissors':
#         print('Sorry, scissors beat paper')
#     elif computer_choice == 'rock':
#         print('Yes, paper beat rock')
#     else:
#         print('Draw!')
# elif human_choice == 'scissors':
#     if computer_choice == 'rock':
#         print('Sorry, rock beat scissors')
#     elif computer_choice == 'paper':
#         print('Yes, scissors beat paper')
#     else:
#         print('Draw!')