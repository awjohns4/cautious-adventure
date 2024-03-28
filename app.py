import random

# Create a enum to convert the choices to a string representating the name of the choice
class Choice:
    Rock = '1'
    Paper = '2'
    Scissors = '3'
    
play_again = 'yes'
while play_again == 'yes':
    # Show the user three options: Rock, Paper, Scissors
    print('Select an option:')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')

    # Get the user's choice
    user_choice = input('Enter your choice: ')

    # Loop until the choice is valid
    while user_choice not in ['1', '2', '3']:
        print('Invalid choice. Please try again.')
        print('Select an option:')
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        user_choice = input('Enter your choice: ')

    # Select a random choice for the computer
    computer_choice = random.choice(['1', '2', '3'])

    # Show what the computer chose using the enum
    named_choice = ""
    if computer_choice == Choice.Rock:
        named_choice = 'Rock'
    elif computer_choice == Choice.Paper:
        named_choice = 'Paper'
    else:
        named_choice = 'Scissors'
    print(f'The computer chose: {named_choice}')

    #Check who won
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == '1' and computer_choice == '3':
        print('You win! Rock beats Scissors.')
    elif user_choice == '2' and computer_choice == '1':
        print('You win! Paper beats Rock.')
    elif user_choice == '3' and computer_choice == '2':
        print('You win! Scissors beats Paper.')
    else:
        print('You lose! Computer wins.')

    # Ask the user if they want to play again if so then loop again
    play_again = input('Do you want to play again? (yes/no): ')
