"""
A Hot or Cold game
"""
import time
from random import randint

win = int(randint(1, 101))

'''
Game Rules
'''
print("Pranjal's GuessoMania!")
print("\tThis game is a total nuisance")
print("\tBattle with the game to get an integer")
print("\tas close as possible to the Randomly generated Computer number.")
guesslist = [0]

def main():
    while True:
        user_Guess = int(input("Enter an integer here(1~100): "))
        # we can copy the code from above to take an input

        if user_Guess < 1 or user_Guess > 100:
            print('OUT OF BOUNDS')
            continue
        if user_Guess == win:
            print(f"Yay, you guessed the number in {len(guesslist)} guesses!")
            quit_option = input("Do you want to quit the game? (Y/N) ")
            if quit_option.lower() in ['y']:
                    break
            elif quit_option.lower() in ['n']:
                retry = input("Do you want to replay? (Y/N) ")
                if retry.lower() in ['y']:
                    clear()
                    main()
                else:
                    print("You have to quit then... The game will quit in ")
                    a = 5
                    print(a)
                    time.sleep(5)
                    print(a - 1)
                    break
            else:
                print("I don't understand what you mean.")
                clear()

            #time.sleep(5)

        guesslist.append(user_Guess)
        if guesslist[-2]:
            if abs(user_Guess-win) < abs(guesslist[-2]-win):
                print("\nWARMER!\n")
            else:
                print("\nCOLDER!\n")
        else:
            if abs(user_Guess-win) <= 10:
                print("\nWARM!\n")
            else:
                print("\nCOLD!\n")
    pass
pass

if __name__ == '__main__':
    main()