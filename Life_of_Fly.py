import time

def diag():
    """
    The description for the program.
    :return:
    """
    print("\tThis is a programme to Calculate the Age Of A HouseFly")
    print("\nIt's a simple code, that multiplies the user input with 24 x 60 x 60")
    print("to accurately determine the age of the fly in seconds,")
    print("from the number of days it has lived.")

def confirm():
    """
    The confirmation function to start
    :return:
    """
    user_confirm = input(f"Would you life to give it a try?(Y/N) ")
    if user_confirm.lower() in ['y', 'yes', 'yeap', 'yep', 'yeah']:
        print("Okay!")
        age_input()
    elif user_confirm.lower() in ['n', 'no', 'nope', 'nah', 'na']:
        print("\n\nOh, I'm sorry to see you leave")
        print("Bye")
        time.sleep(3)
    else:
        print("Sorry, I didn't understand")
        print("Please try again.")
        confirm()

def age_input():
    """
    The input for the user to write the days
    :return:
    """
    global age
    age = input("Input the number of days, the housefly has lived(>0): ")
    #try:
    #I tried, didn't have much time to add error handling
    if not age.isdigit():
        print("Sorry! Please type in positive integer only.")
        age_input()
        pass
    elif age.isdigit() and int(age)<0:
        age = -1*age
        calc()
    else:
        age = int(age)
        calc()
    #except:
    #ignore

def calc():
    """
        The calculator, and checker for integers
        :return:
    """
    global age
    age = int(age)
    print('\n'*5)
    print("We multiply the age with 24 x 60 x 60 (86,400) to get the")
    print("age of the housefly in seconds.")
    print('\n')
    print(f"This is the age of the housefly: {age}")
    print(f"{age} x 86400 =")
    print(f"\t{age*86400}")
    print(f"That housefly has lived {age*86400} seconds!")
    print("Thanks for using!")
    print("\tMade by Pranjal Pratosh(21BCE3291)")
    print("Bye!")
    time.sleep(12)

if __name__ == '__main__':
    """
    This is where the program STARTS!
    """
    diag()
    confirm()

