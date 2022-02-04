'''The TicTacToe Game!'''
# python "Downloads\Project_TicTacToe.py"
import random
import time
from os import system, name


# from IPython.display import clear_output


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def game_rule():
    '''
    Explains the game rules.
    '''
    print("\n\nThe TicTacToe Game!")
    print("\n>> This game is made for two people using the same device.")
    print(">> Each player will take turns to mark the 3x3 grid with either an X or an O.")
    print(">> The first player to get a row or column")
    print("  or diagonal filled with his/her unique marker, wins the game!")
    print("made by Pranjal Pratosh")
    print("Type 'end' anytime to exit.")


def choose_first():
    '''
    Randomly chooses the first player
    '''
    starter = random.randint(1, 2)
    if starter == 1:
        print('\nPlayer 1 will begin.')
        return 'Player1'
    else:
        print('\nPlayer 2 will begin.')
        return 'Player2'


def marker_assign():
    '''
    Requires the players to choose their respective markers
    '''
    global player1_marker
    global player2_marker
    mark1 = True
    while mark1:
        player1_marker = input("\nPlayer 1: Do you want to be X or O: ").upper()
        if player1_marker.lower() in ['end']:
            confirm()
            mark1 = False
        if player1_marker.upper() not in ['X', 'O']:
            # clear_output()
            print('\n'*100)
            clear()
            print("\nWrong input! Please choose between X (or) O")
            continue
        else:
            mark1 = False
            # clear_output()
            print('\n'*100)
            clear()
            if player1_marker == 'X':
                player2_marker = 'O'
            else:
                player2_marker = 'X'



def place_marker(board, marker, position):
    '''
    Determines the marker position on the board
    '''
    board[position] = marker


def display_board(board):
    """
    Displays the current board
    """
    clear()
    print('\n' * 100)

    print('    |     |')
    print(f" {board[0]}  |  {board[1]}  |  {board[2]} ")
    print('    |     |')
    print('****|*****|****')
    print('    |     |')
    print(f" {board[3]}  |  {board[4]}  |  {board[5]} ")
    print('    |     |')
    print('****|*****|****')
    print('    |     |')
    print(f" {board[6]}  |  {board[7]}  |  {board[8]} ")
    print('    |     |')


def board_test():
    """
    (Only used once), to show the user the board layout
    """
    # clear_output()
    print('\n'*100)
    clear()
    print(f"Player 1 is '{player1_marker}', Player 2 is '{player2_marker}'.")
    print('\nThe board will look something like this:')
    print('    |     |')
    print(" 1  |  2  |  3 ")
    print('    |     |')
    print('****|*****|****')
    print('    |     |')
    print(" 4  |  5  |  6 ")
    print('    |     |')
    print('****|*****|****')
    print('    |     |')
    print(" 7  |  8  |  9 ")
    print('    |     |')
    print("\nThe numbers represent the grid-box value, you will need")
    print("to type the number of the grid-box")
    print("in which you would like to place your marker.")


def space_check(board, position):
    '''
    Check's for empty spaces on the board, on a certain grid-box
    '''
    return board[position] == ' '


def full_board_check(board):
    """
    Check's the entire board for empty cells
    """
    for i in range(0, 9):
        if space_check(board, i):
            return False
    return True


def win_check(board, mark):
    """
    Contains all patters for winning the game,
    cross-checks each time player validates their marker
    """
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or  # across the top
            (board[3] == mark and board[4] == mark and board[5] == mark) or  # across the middle
            (board[6] == mark and board[7] == mark and board[8] == mark) or  # across the bottom
            (board[0] == mark and board[3] == mark and board[6] == mark) or  # down the left side
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the right side
            (board[0] == mark and board[4] == mark and board[8] == mark) or  # diagonal tl-br
            (board[2] == mark and board[4] == mark and board[6] == mark))  # diagonal tr-bl


# ___________________________________________________________________________________________________
############# GAME STARTS HERE ######################################################################
def game_run():
    """
    Main game mechanic- A while loop that takes to turn to
    give each player a chance to place their marker
    """
    turn = choose_first()
    game_status = True
    print('The game has started!')
    while game_status:
        if turn == 'Player1':
            if not full_board_check(e_board):
                print(f"Your marker is {player1_marker}")
                player = input(f"Choose your position, {turn} (1~9): ")
                if player.lower() in ['end']:
                    confirm()
                    game_status = False
                if not player.isdigit():
                    print('Sorry, I think you miss clicked. Try typing in a number this time.')
                    continue
                elif player.isdigit():
                    if not int(player) in range(1, 10):
                        print("Sorry, your input is Out of Bounds! Try again.")
                        continue
                if space_check(e_board, int(player) - 1):
                    place_marker(e_board, player1_marker, int(player) - 1)
                    display_board(e_board)
                    if win_check(e_board, player1_marker):
                        print('\nCongratulation Player 1, You have won the game!'.upper())
                        game_status = False
                    else:
                        turn = 'Player2'
                        continue
                else:
                    print('This grid-slot is already occupied, please choose another one.')
                    turn = 'Player1'
                    continue

            else:
                if win_check(e_board, player1_marker):
                    print('\nCongratulation Player 1, You have won the game!'.upper())
                    game_status = False
                elif win_check(e_board, player2_marker):
                    print('\nCongratulation Player 2, You have won the game!'.upper())
                    game_status = False
                else:
                    print("\nSorry, the game was a Draw!".upper())
                    game_status = False

        if turn == 'Player2':
            if not full_board_check(e_board):
                print(f"Your marker is {player2_marker}")
                player = input(f'Choose your position, {turn} (1~9):')
                if player.lower() in ['end']:
                    confirm()
                    game_status = False
                if not player.isdigit():
                    print('Sorry, I think you miss clicked. Try typing in a number this time.')
                    continue
                elif player.isdigit():
                    if not int(player) in range(1, 10):
                        print("Sorry, your input is Out of Bounds! Try again.")
                        continue
                if space_check(e_board, int(player) - 1):
                    place_marker(e_board, player2_marker, int(player) - 1)
                    display_board(e_board)
                    if win_check(e_board, player2_marker):
                        print("\nCongratulation Player 2, You have won the game!".upper())
                        game_status = False
                    else:
                        turn = 'Player1'
                        continue
                else:
                    print('This grid-slot is already occupied, please choose another one.')
                    turn = 'Player2'
                    continue
            else:
                if win_check(e_board, player2_marker):
                    print('\nCongratulation Player 2, You have won the game!'.upper())
                    game_status = False
                elif win_check(e_board, player1_marker):
                    print('\nCongratulation Player 1, You have won the game!'.upper())
                    game_status = False
                else:
                    print("\nSorry, the game was a Draw!".upper())
                    game_status = False


def confirm():
    """
    Confirmation from player to commence the game.
    """
    ans = input('\nShall we start? (Yes/No)')
    if ans.lower() in ['yes', 'y', 'yea', 'ya', 'ye']:
        clear()
        print('\n'*100)
        game_run()
    elif ans.lower() in ['no', 'nah', 'nope', 'n', 'na']:
        clear()
        print('\n'*100)
        print("")
        retry1 = input('Are you ready to leave? ')
        if retry1.lower() in ['no', 'nah', 'nope', 'n', 'na']:
            retry()
        elif retry1.lower() in ['yes', 'y', 'yea', 'ya', 'ye']:
            clear()
            print('\n'*100)

            print('Okay, program will shut down now...')
            t = 5
            print(t)
            # Sleep timer starting
            time.sleep(5)
            print(t - 1)
            print(t - 2)
            print(t - 3)
            print("*********************************")
            print('THE PROGRAM HAS SHUT DOWN')
            print('*********************************')
        else:
            rules = input("Do you want the rules again?")
            if rules.lower() in ['yes', 'y', 'yea', 'ya', 'ye']:
                board_test()
                confirm()
            else:
                clear()
                print('\n'*100)

                print('Okay, program will shut down now...')
                t = 5
                print(t)
                #Sleep timer starting
                time.sleep(5)
                print(t - 1)
                print(t - 2)
                print(t - 3)
                print("*********************************")
                print('THE PROGRAM HAS SHUT DOWN')
                print('*********************************')
    else:
        clear()
        print('\n'*100)
        print("Sorry, I don't understand. Try again?")
        confirm()


def retry():
    global e_board
    '''
    Confirmation to Retry the game
    '''
    retry_cont = input('\nWanna retry?')
    clear()
    print('\n' * 100)
    if retry_cont.lower() in ['end']:
        confirm()
    if retry_cont.lower() in ['yes', 'y', 'yea', 'ya', 'ye']:
        clear()
        print('\n'*100)
        e_board = [' '] * 10
        confirm()
        #retry()
    elif retry_cont.lower() in ['no', 'nah', 'nope', 'n', 'na']:
        clear()
        print('\n'*100)

        print('Okay, program will shut down now...')
        t = 5
        print(t)
        # Sleep timer starting
        time.sleep(5)
        print(t - 1)
        print(t - 2)
        print(t - 3)
        print("*********************************")
        print('THE PROGRAM HAS SHUT DOWN')
        print('*********************************')
    elif retry_cont.isdigit():
        print("Sorry, I don't understand.")
        retry()
    else:
        print("Sorry, I don't understand.")
        retry()


if __name__ == "__main__":
    """
    This bit of code will always execute first,
    contains the order of execution of all functions
    """
    e_board = [' '] * 10
    game_rule()
    marker_assign()
    board_test()
    confirm()
    retry()
# ___________________________________________________________________________________________________
