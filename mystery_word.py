import random
import time
import string
import pathlib



quit_game = False
game_start = False
difficuly = 1
mystery_words_bank = []

"""mystery words text file "words.txt" needs to be included to play!"""
"""*** words.txt must be in the same directory as mystery_word.py ***"""

with open(str(pathlib.Path.cwd())+"/words.txt") as text_file:
    mystery_words_bank = text_file.read()
    mystery_words_bank = mystery_words_bank.lower().splitlines()


def mystery_word_menu():
    """start menu before entering a game"""
    """start | difficulty: 1-5 | quit"""
    print(
    '\n'
    '\n=============================================='
    '\n|                                            |'
    '\n|            Mystery Word Game!              |'
    '\n|                                            |'
    '\n|                                            |'
    '\n|                  START!                    |'
    '\n|                                            |'
    '\n|                                            |'
    '\n|              Difficulty: 1 - 3             |'
    f"\n|                 (   {difficuly}   )                  |"
    '\n|                                            |'
    '\n|                                            |'
    '\n|                   Quit.                    |'
    '\n|                                            |'
    '\n=============================================='
    )
    user_input = input('\nType "Start", 1 - 3, or "Quit": ')
    print(user_input)
    handle_menu_user_input(user_input)
    pass

def flashy_start():
    """flashy user feedback the game has started"""
    print(
        '\n'
        '\n'
        '\n=============================================='
        '\n ######  ########    ###    ########  ########'
        '\n##    ##    ##      ## ##   ##     ##    ##   '
        '\n##          ##      ## ##   ##     ##    ##   '
        '\n ######     ##    ##     ## ########     ##   '
        '\n      ##    ##    ######### ##   ##      ##   '
        '\n##    ##    ##    ##     ## ##    ##     ##   '
        '\n ######     ##    ##     ## ##     ##    ##   '
        '\n=============================================='
        '\n'
        '\n'
    )




def mystery_word_game():
    """main body that holds the game state the game"""
    global mystery_words_bank
    mystery_word = get_mystery_word(mystery_words_bank)
    guessed_letters = []
    display_word = []
    player_life = 8
    for letter in mystery_word: display_word.append('_')
    while not quit_game:
        user_input = display_game_board(guessed_letters, display_word, player_life)
        handle_game_user_input(user_input, guessed_letters, display_word, mystery_word, player_life)
        pass

def handle_menu_user_input(user_input):
    """processes the user's input and directs flow of control at the game menu"""
    difficulty = ['1', '2', '3',]
    if user_input in difficulty:
        select_difficulty(user_input)
    elif user_input.lower() == "start":
        global game_start
        game_start = True
        flashy_start()
        mystery_word_game()
    elif user_input.lower() == "quit":
        quit_game = True
    else:
        catch_input = input('\nInvalid Input! Try: "start", "1", "2", "3", or "quit"')
        handle_menu_user_input(catch_input)

def handle_game_user_input(user_input, guessed_letters, display_word, mystery_word, player_life):
    """takes user input, checks game conditions, and updates display word and player life"""
    user_input = user_input.lower()
    if user_input == 'quit':
        global quit_game
        quit_game = True
    elif user_input not in string.ascii_lowercase:
        catch_input = input(f'\n"{user_input}" is not a valid letter, try again or "Quit": ')
        print(catch_input)
        handle_game_user_input(catch_input, guessed_letters, display_word, mystery_word, player_life)
    elif user_input in guessed_letters:
        catch_input = input(f'\nYou have already guessed "{user_input}", try again or "Quit": ')
        print(catch_input)
        handle_game_user_input(catch_input, guessed_letters, display_word, mystery_word, player_life)
    elif user_input in mystery_word:
        letters_revealed = 0
        for counter in range(len(mystery_word)):
            if user_input == mystery_word[counter]:
                display_word[counter] = user_input
                letters_revealed += 1
            counter += 1
        print(f'\nYou revealed {letters_revealed} letter "{user_input.upper()}"!')
        if display_word.count('_') > 0:
            guessed_letters.append(user_input)
            new_user_input = display_game_board(guessed_letters, display_word, player_life)
            handle_game_user_input(new_user_input, guessed_letters, display_word, mystery_word, player_life)
        else:
            display_win()
            catch_input = input('You Win! Play Again (Y/N)? ')
            play_again(catch_input)
    else:
        if player_life - 1 == 0:
            catch_input = input(f'\n\n You Lose! The word was {mystery_word}. Try Again (Y/N): ')
            play_again(catch_input)
        else:
            print(f'\nIncorrect! The Mystery Word does NOT include "{user_input.upper()}". Lose 1 Life!')
            guessed_letters.append(user_input)
            player_life -= 1
            time.sleep(1)
            new_user_input = display_game_board(guessed_letters, display_word, player_life)
            handle_game_user_input(new_user_input, guessed_letters, display_word, mystery_word, player_life)

def play_again(input):
    global game_start
    global quit_game
    if input.lower() == 'y':
        game_start = False
        mystery_word_menu()
    elif input.lower() == 'quit':
        game_start = False
        quit_game = True
    elif input.lower() == 'n':
        game_start = False
        quit_game = True
    else:
        catch_input = input(f'\nError! "{input}" is invalid! Try "Y", "N", or "Quit"')
        play_again(catch_input)

def select_difficulty(user_input):
    """takes the processed, valid user input to change difficulty"""
    """and sets the global difficulty variable 'difficulty' to the input value"""
    global difficuly
    difficuly = int(user_input)
    mystery_word_menu()


def display_game_board(guessed_letters, display_word, player_life):
    word_display = ''
    for letter in display_word:
        word_display += ' ' + letter

    print('\n')
    print('\n==============================================')
    print('\n\n\n')
    print(word_display.center(42))
    print(
        '\n'
        '\n'
        '\nGuessed Letters: '
    )
    guessed_letters.sort()
    print(*guessed_letters, sep=", ")
    print('\nLives Remaining: ')
    print(player_life)
    print('\n==============================================')
    user_input = input('\nEnter a letter or "Quit": ')
    return user_input


def display_win():
    print(
        '\n\n'
        '\n====================================================='
        '\n##      ## #### ##    ## ##    ## ######## ########  '
        '\n##  ##  ##  ##  ###   ## ###   ## ##       ##     ## '
        '\n##  ##  ##  ##  ####  ## ####  ## ##       ##     ## '
        '\n##  ##  ##  ##  ## ## ## ## ## ## ######   ########  '
        '\n##  ##  ##  ##  ##  #### ##  #### ##       ##   ##   '
        '\n##  ##  ##  ##  ##   ### ##   ### ##       ##    ##  '
        '\n ###  ###  #### ##    ## ##    ## ######## ##     ## '
        '\n====================================================='
        '\n\n'
    )
    pass


def get_mystery_word(list_of_words):
    #get word from words.txt at random and check that its not "start" or "quit"
    #return word in string form, lower case
    good_word = False
    mystery_word = list_of_words[random.randrange(0, len(list_of_words))].lower()
    while not good_word:
        if difficuly == 1:
            if len(mystery_word) > 4 and len(mystery_word) < 6:
                good_word = True
            else:
                mystery_word = list_of_words[random.randrange(0, len(list_of_words))].lower()
        elif difficuly == 2:
            if len(mystery_word) > 6 and len(mystery_word) < 8:
                good_word = True
            else:
                mystery_word = list_of_words[random.randrange(0, len(list_of_words))].lower()
        else:
            if len(mystery_word) > 8:
                good_word = True
            else:
                mystery_word = list_of_words[random.randrange(0, len(list_of_words))].lower()
    return mystery_word


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='A Myster Word Game!')
    args = parser.parse_args()

    mystery_word_menu()