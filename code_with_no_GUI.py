import random

Game_state = True

# Create a randomized list

while Game_state == True:

    random_list = ('Rock', 'Paper', 'Scissors')

    # Generate a random choice

    random_choice = random.choice(random_list)


    # Ask user to input their answer

    player_input = input('Rock, Paper, Scissors... ').capitalize()

    # Create some "rules", lol :)


    # Paper beats rock

    if player_input == 'Rock' and random_choice == 'Paper':
        print(f'Computer = {random_choice}\nPlayer = {player_input}\nComputer Wins!')
        Game_state = False
        play_again = input('Wanna play again? (Yes, or No) ').capitalize()
        if play_again == 'Yes':
            Game_state = True
        elif play_again == 'No':
            Game_state = False
        else:
            Game_state = False

    elif player_input == 'Paper' and random_choice == 'Rock':
        print(f'Computer = {random_choice}\nPlayer = {player_input}\nYou Win!')
        Game_state = False
        play_again = input('Wanna play again? (Yes, or No) ').capitalize()
        if play_again == 'Yes':
            Game_state = True
        elif play_again == 'No':
            Game_state = False
        else:
            Game_state = False

    # Rock beats scissors

    elif player_input == 'Rock' and random_choice == 'Scissors':
        print(f'Computer = {random_choice}\nPlayer = {player_input}\nYou Win!')
        Game_state = False
        play_again = input('Wanna play again? (Yes, or No) ').capitalize()
        if play_again == 'Yes':
            Game_state = True
        elif play_again == 'No':
            Game_state = False
        else:
            Game_state = False

    elif player_input == 'Scissors' and random_choice == 'Rock':
        print(f'Computer = {random_choice}\nPlayer = {player_input}\nComputer Wins!')
        Game_state = False
        play_again = input('Wanna play again? (Yes, or No) ').capitalize()
        if play_again == 'Yes':
            Game_state = True
        elif play_again == 'No':
            Game_state = False
        else:
            Game_state = False

    # Scissors beats paper

    elif player_input == 'Scissors' and random_choice == 'Paper':
        print(f'Computer = {random_choice}\nPlayer = {player_input}\nYou Win!')
        Game_state = False
        play_again = input('Wanna play again? (Yes, or No) ').capitalize()
        if play_again == 'Yes':
            Game_state = True
        elif play_again == 'No':
            Game_state = False
        else:
            Game_state = False

    elif player_input == 'Paper' and random_choice == 'Scissors':
        print(f'Computer = {random_choice}\nPlayer = {player_input}\nComputer Wins!')
        Game_state = False
        play_again = input('Wanna play again? (Yes, or No) ').capitalize()
        if play_again == 'Yes':
            Game_state = True
        elif play_again == 'No':
            Game_state = False
        else:
            Game_state = False

    # Draw

    elif player_input == random_choice:
        print('Draw')
        Game_state = False
        play_again = input('Wanna play again? (Yes, or No) ').capitalize()
        if play_again == 'Yes':
            Game_state = True
        elif play_again == 'No':
            Game_state = False
        else:
            Game_state = False

    # Help message

    else:
        print('Please input ROCK, PAPER, or SCISSORS')
        Game_state = False
        Game_state = True
