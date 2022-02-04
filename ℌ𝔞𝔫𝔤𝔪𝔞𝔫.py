# Have different topics, Like: Movies, Drama, Anime, Music, World, Science etc..
# Counter for number of wrongs (Looks like health bar)
# Show WRONG in big figures
# Print the already guessed words
# Use Dictionary for Words
# Extra letter/ Hint available
# typewriter design with matrix codes falling
# Big X for wrong answers, and wait 1 sec . contd
# time 0.5 sec, drop down square to add graphics
# press enter to start
# encrypt the data
# two while statements, one for hint, other for user input
# > 3 second letter, then two letters apart, and then three letter etc
# THE END, YOU WIN titles, and high score as well
# create new .txt file and store high score
# DO NOT RUN IN EDITOR,just double-click the .py file ##########
import random
import time
import string


def loader():
    brace_l, brace_r = "[ ", " ]"
    for num in range(0, 60):
        if num == 1:
            print("\n" * 29)
            pass
        print("  DO NOT CLICK THE SCREEN - Use the tab strip to bring to focus.")
        print("\n  DO NOT RESIZE THE WINDOW, there is no 'Fullscreen' experience.")
        print("\n       Yes, the text will be glitchy. I haven't used animators")
        print("\n\n  Let me know of any abrupt crashes ~ WhatsApp No. : +91 72078 85530")
        if num % 4 == 1:
            a = ""
        elif num % 4 == 2:
            a = "."
        elif num % 4 == 3:
            a = ". ."
        elif num % 4 == 0:
            a = ". . ."
        print(f"\n  Loading {a}" + " " + f"{round(num * (5 / 3) + 2)}%")
        print("\n")
        if 1 < num < 59:
            henge = "▓" * num * 2  # Symbol of Loading Bar
            space = " " * (116 - len(henge) - 1)
            print(brace_l + henge + space + brace_r)
            time.sleep(0.5)  # Change this time.sleep() to change loader's speed (Less is Faster)
            print("\n" * 29)
        elif num == 59:
            print(brace_l + henge + space + brace_r)
            time.sleep(2)  # End stay time of loader
        pass
    pass


def home():
    print("\n" * 27)
    for p in range(0, 2):
        time.sleep(0.5)
        print("/" * 120)
    print(
        "=====....=====......======~......=====....=====,....========+......======....======........=======......=====+....=====."
        "=====....=====.....========.....,======...=====,..+============....======...=======........========.....=======...=====."
        "=====....=====.....========+....,=======..=====,.=============....,=======..=======.......=========.....========..=====."
        "==============....=====:====....,========.=====,.=====............+=======.========:......====,=====....========+.=====."
        "==============....====:.=====...,====.====.====,======..=========.==================.....=====.:====....===============."
        "==============...=====..+====,..,=====.========,.=====..========:.====~:======.=====.....=====..=====...=====.~========."
        "=====....=====..==============..,=====..=======,.=======.,======.:====..======.=====....==============..=====..========."
        "=====....=====..===============..=====...======,..+============..=====..~====..~====~..~==============..=====...=======."
        "=====....=====.======....~=====.,=====....=====,....=+=======....=====...====...=====..======....======.=====....~=====."
    )
    for p in range(0, 2):
        time.sleep(0.5)
        print("\\" * 120)
    print(
        "                                                                                                                © 2021")
    print("\n" * 3 + "                                                  PRESS ENTER TO START")
    input("\n" * 3)
    pass


def word(num, letter, n):
    blank = {'a': {1: '      ', 2: '      ', 3: '      ', 4: '      ', 5: '      ', 6: '      ', 7: '      ',
                   8: '      ', 9: '      ', 10: '      ', 11: '      ', 12: '      ', 13: '      ',
                   14: '      ', 15: '      ', 16: '      ', 17: '      '},
             'b': {1: '      ', 2: '      ', 3: '      ', 4: '      ', 5: '      ', 6: '      ',
                   7: '      ', 8: '      ', 9: '      ', 10: '      ', 11: '      ', 12: '      ',
                   13: '      ', 14: '      ', 15: '      ', 16: '      ', 17: '      '},
             'c': {1: '      ', 2: '      ', 3: '      ', 4: '      ', 5: '      ', 6: '      ',
                   7: '      ', 8: '      ', 9: '      ', 10: '      ', 11: '      ', 12: '      ',
                   13: '      ', 14: '      ', 15: '      ', 16: '      ', 17: '      '},
             'd': {1: '      ', 2: '      ', 3: '      ', 4: '      ', 5: '      ', 6: '      ',
                   7: '      ', 8: '      ', 9: '      ', 10: '      ', 11: '      ', 12: '      ',
                   13: '      ', 14: '      ', 15: '      ', 16: '      ', 17: '      '},
             'e': {1: '▄▄▄▄▄▄', 2: '▄▄▄▄▄▄', 3: '▄▄▄▄▄▄', 4: '▄▄▄▄▄▄', 5: '▄▄▄▄▄▄', 6: '▄▄▄▄▄▄',
                   7: '▄▄▄▄▄▄', 8: '▄▄▄▄▄▄', 9: '▄▄▄▄▄▄', 10: '▄▄▄▄▄▄', 11: '▄▄▄▄▄▄', 12: '▄▄▄▄▄▄',
                   13: '▄▄▄▄▄▄', 14: '▄▄▄▄▄▄', 15: '▄▄▄▄▄▄', 16: '▄▄▄▄▄▄', 17: '▄▄▄▄▄▄'}
             }

    blank2 = {'a': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
                    7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
                    },
              'b': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
                    7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
                    },
              'c': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
                    7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
                    },
              'd': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
                    7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
                    },
              'e': {1: '▄▄▄▄▄▄▄▄▄', 2: '▄▄▄▄▄▄▄▄▄', 3: '▄▄▄▄▄▄▄▄▄', 4: '▄▄▄▄▄▄▄▄▄', 5: '▄▄▄▄▄▄▄▄▄', 6: '▄▄▄▄▄▄▄▄▄',
                    7: '▄▄▄▄▄▄▄▄▄', 8: '▄▄▄▄▄▄▄▄▄', 9: '▄▄▄▄▄▄▄▄▄', 10: '▄▄▄▄▄▄▄▄▄', 11: '▄▄▄▄▄▄▄▄▄', 12: '▄▄▄▄▄▄▄▄▄'
                    }
              }

    alpha_dict = {'A': ['   ███   ', '  █   █  ', '  █████  ', '  █   █  ', '  █   █  '],
                  'B': ['  ████   ', '  █   █  ', '  ████   ', '  █   █  ', '  ████   '],
                  'C': ['   ████  ', '  █      ', '  █      ', '  █      ', '   ████  '],
                  'D': ['  ████   ', '  █   █  ', '  █   █  ', '  █   █  ', '  ████   '],
                  'E': ['  █████  ', '  █      ', '  ███    ', '  █      ', '  █████  '],
                  'F': ['  █████  ', '  █      ', '  ███    ', '  █      ', '  █      '],
                  'G': ['   ███   ', '  █      ', '  █  ██  ', '  █   █  ', '   ███   '],
                  'H': ['  █   █  ', '  █   █  ', '  █████  ', '  █   █  ', '  █   █  '],
                  'I': ['   ███   ', '    █    ', '    █    ', '    █    ', '   ███   '],
                  'J': ['   ███   ', '    █    ', '    █    ', '  █ █    ', '   ██    '],
                  'K': ['  █  █   ', '  █ █    ', '  ██     ', '  █ █    ', '  █  █   '],
                  'L': ['   █     ', '   █     ', '   █     ', '   █     ', '   ████  '],
                  'M': [' ██   ██ ', ' █ █ █ █ ', ' █  █  █ ', ' █     █ ', ' █     █ '],
                  'N': [' ██    █ ', ' █ █   █ ', ' █  █  █ ', ' █   █ █ ', ' █    ██ '],
                  'O': ['  █████  ', ' █     █ ', ' █     █ ', ' █     █ ', '  █████  '],
                  'P': ['  █████  ', '  █    █ ', '  █████  ', '  █      ', '  █      '],
                  'Q': ['  █████  ', ' █     █ ', ' █     █ ', ' █   █ █ ', '  ██  █  '],
                  'R': ['  ████   ', '  █   █  ', '  ████   ', '  █   █  ', '  █   █  '],
                  'S': ['   ████  ', '  █      ', '   ███   ', '      █  ', '  ████   '],
                  'T': [' ███████ ', '    █    ', '    █    ', '    █    ', '    █    '],
                  'U': ['  █   █  ', '  █   █  ', '  █   █  ', '  █   █  ', '   ███   '],
                  'V': ['  █   █  ', '  █   █  ', '  █   █  ', '   █ █   ', '    █    '],
                  'W': ['█       █', '█       █', '█   █   █', ' █ █ █ █ ', '  █   █  '],
                  'X': ['  █   █  ', '   █ █   ', '    █    ', '   █ █   ', '  █   █  '],
                  'Y': ['  █   █  ', '   █ █   ', '    █    ', '    █    ', '    █    '],
                  'Z': ['   ████  ', '      █  ', '    █    ', '   █     ', '   ████  '],
                  ' ': ['         ', '         ', '         ', '         ', '         '],
                  "'": ['     ██  ', '      █  ', '         ', '         ', '         '],
                  ',': ['         ', '         ', '         ', '    ██   ', '    ▄█   ']

                  }
    if n == '':
        n = blank2
    else:
        pass

    #   Write error handling!!
    lst = ['a', 'b', 'c', 'd', 'e']
    for j in range(len(lst)):
        for k in alpha_dict[letter]:
            n[lst[j]][num] = alpha_dict[letter][j]
            pass
    my_str = ''
    for j in range(len(lst)):
        for i in range(1, 13):
            my_str += ' ' + n[lst[j]][i]
    pass
    return n, my_str


class Topic:
    def __init__(self):
        pass

    '''
    1. India               

    2. World               

    3. Politics            

    4. Sports              

    5. Money & Finance     

    6. Science & Technology

    7. Celebrity           

    8. TV & Movies         

    9. Anime               

    10. Books              
    '''

    def decrypt(self, encoded):
        decrypt_dict = {'a!': 'A', 'b!': 'Q', 'a@': 'Z', 'b@': 'V',
                        'c!': 'M', 'd!': 'I', 'c@': 'R', 'd@': 'N',
                        'e!': 'E', 'a#': 'F', 'e@': 'J', 'a$': 'K',
                        'b#': 'G', 'c#': 'W', 'b$': 'L', 'c$': 'H',
                        'd#': 'X', 'e#': 'T', 'd$': 'S', 'e$': 'O',
                        'a%': 'U', 'a^': 'P', 'b%': 'B', 'c%': 'C',
                        'd%': 'D', 'e%': 'Y', 'b^': "'", 'c^': ',', 'd^': ' '
                        }

        decrypt_word = ""
        for i in range(0, len(encoded), 2):
            decrypt_word += decrypt_dict[encoded[i:i + 2]]
        return decrypt_word
        pass

    def india(self):
        india_dict = ['d@e!c#d^d%e!b$c$d!', 'b%a!d@b#a!b$e$c@e!', 'd!d@d%d!a!d@', 'c%c$e!d@d@a!d!', 'c$d!d@d%a%d!d$c!',
                      'b%d!c$a!c@', 'c$d!c!a!b$a!e%a!d$', 'b%c$a!c@a!e#',
                      'a$e$b$a$a!e#a!',
                      'e#a!c!d!b$d^d@a!d%a%', 'a^e$a^a%b$a!e#d!e$d@', 'a!e%a%c@b@e!d%a!',
                      'd@e$d@d^b@d!e$b$a!d@c%e!', 'd!d@d%d!a!', 'c!a%c!b%a!d!', 'a^a%d@e@a!b%', 'b#a%e@a!c@a!e#',
                      'a!d$d!a!', 'b#a!d@b#e!d$', 'c$d!d@d%d!', 'e@a!d!a^a%c@', 'd!d@d%e$c@e!d^', 'b%d!c@e%a!d@d!',
                      'c%c@d!c%a$e!e#', 'a^a!e#e!b$', 'a^e!a!c%e$c%a$', 'e@a!c#a!d@', 'a!c$d!c!d$a!',
                      'c!a!d@d!a^a%c@', 'b#a%c@b#a!e$d@', 'c!a%b#c$a!b$', 'a$c@d!d$c$d@a!', 'd%e!c%c%a!d@',
                      'd%e!c!e$c%c@a!c%e%', 'b#a%c#a!c$a!e#d!', 'a!d$c$e$a$a!']
        return random.choice(india_dict)
        pass

    def world(self):
        world_dict = ['e!a!c@e#c$', 'c#e$c@b$d%c#d!d%e!', 'b#b$e$b%a!b$', 'b#b$e$b%e!', 'a^b$a!d@e!e#',
                      'd!d@e#e!c@d@a!e#d!e$d@a!b$', 'c$a%c!a!d@d!e#e%', 'd@a!e#d!e$d@', 'e!a%c@e$a^e!',
                      'a!c!e!c@d!c%a!',
                      'a!d$d!a!', 'a!a%d$e#c@a!b$d!a!', 'a!a#c@d!c%a!', 'a!d@e#a!c@c%e#d!c%a!', 'd@a!e#a%c@e!',
                      'c%e$a%d@e#c@e%', 'a%d@d!e#e!d%', 'c$e!a!b@e!d@b$e%d^b%e$d%e%', 'c$e$c!e!', 'd$a^c$e!c@e!',
                      'c$d!d$e#e$c@e%', 'b#b$e$b%a!b$d!a@a!e#d!e$d@', 'c%e$d@e#d!d@e!d@e#', 'c%d!b@d!b$d!a@a!e#d!e$d@',
                      'c%b$d!c!a!e#e!', 'a^e$a^a%b$a!e#d!e$d@', 'b#e!e$b#c@a!a^c$e%', 'b#e!e$d$a^c$e!c@e!',
                      'd$e$b$a!c@d^d$e%d$e#e!c!', 'e#e!c@c@a!', 'e#e!c@c@e!d$e#c@d!a!b$',
                      'd%e$c!a!d!d@', 'b#a!e!a!', 'e#e!c@c@a!a#e$c@c!', 'c$a%c!a!d@', 'e#e!b$b$a%c@d!a!d@',
                      'd$e!d!d$c!d!c%', 'd$e$c%d!e!e#e%'
                      ]
        return random.choice(world_dict)
        pass

    def politics(self):
        pass

    def sport(self):
        sport_dict = ['a!e#c$b$e!e#d!c%d$', 'd$e$c%c%e!c@', 'c@a!c%d!d@b#', 'a#e$e$e#b%a!b$b$', 'e#e!d@d@d!d$',
                      'c@a%b#b%e%',
                      'd$a$d!', 'b%a!d$a$e!e#b%a!b$b$', 'c%e$a!c%c$', 'c@d!d%d!d@b#', 'e#e$a%c@d@a!c!e!d@e#',
                      'b#e$b$a#',
                      'd@a!d$c%a!c@', 'e$b$e%c!a^d!c%d$', 'c@a%d@d@d!d@b#', 'a#e$e$e#b%a!b$b$e!c@', 'b%e$c#b$d!d@b#',
                      'd%c@d!b@d!d@b#', 'a^b$a!e%e!c@d$', 'b#e$a!b$', 'c#c@e!d$e#b$d!d@b#', 'e@e$b#',
                      'a^a!c@a!b$e%c!a^d!c%d$',
                      'c!e$e#e$c@c%e%c%b$d!d@b#', 'c@e$b$b$e!c@d^d$a$a!e#e!'
                      ]
        return random.choice(sport_dict)

    def money(self):
        money_dict = ['c!e$d@e!e%', 'b$e$a!d@', 'a#a%d@d%d$', 'e#a!d#', 'd!d@b@e!d$e#', 'c#e!a!b$e#c$',
                      'a#d!d@a!d@c%e!',
                      'b%a!d@a$', 'b#e$b$d%d^c%e$d!d@', 'c@e!b@e!d@a%e!', 'a!c%c%e$a%d@e#', 'a^a!d!d%',
                      'b%a!d@a$d@e$e#e!d$',
                      'e#a!d#a^a!e%e!c@d$', 'd%e!b%e#', 'a!a^a^c@e$a^c@d!a!e#d!e$d@', 'c!e$d@e!e#a!c@e%d^d$e%d$e#e!c!',
                      'd$a!b@d!d@b#d$d^a!c%c%e$a%d@e#'
                      ]
        return random.choice(money_dict)


def extract_n_check(ni, check):
    # change key of dict, and then find a way to cross check n_temp
    alpha_dict = {'A': ['   ███   ', '  █   █  ', '  █████  ', '  █   █  ', '  █   █  '],
                  'B': ['  ████   ', '  █   █  ', '  ████   ', '  █   █  ', '  ████   '],
                  'C': ['   ████  ', '  █      ', '  █      ', '  █      ', '   ████  '],
                  'D': ['  ████   ', '  █   █  ', '  █   █  ', '  █   █  ', '  ████   '],
                  'E': ['  █████  ', '  █      ', '  ███    ', '  █      ', '  █████  '],
                  'F': ['  █████  ', '  █      ', '  ███    ', '  █      ', '  █      '],
                  'G': ['   ███   ', '  █      ', '  █  ██  ', '  █   █  ', '   ███   '],
                  'H': ['  █   █  ', '  █   █  ', '  █████  ', '  █   █  ', '  █   █  '],
                  'I': ['   ███   ', '    █    ', '    █    ', '    █    ', '   ███   '],
                  'J': ['   ███   ', '    █    ', '    █    ', '  █ █    ', '   ██    '],
                  'K': ['  █  █   ', '  █ █    ', '  ██     ', '  █ █    ', '  █  █   '],
                  'L': ['   █     ', '   █     ', '   █     ', '   █     ', '   ████  '],
                  'M': [' ██   ██ ', ' █ █ █ █ ', ' █  █  █ ', ' █     █ ', ' █     █ '],
                  'N': [' ██    █ ', ' █ █   █ ', ' █  █  █ ', ' █   █ █ ', ' █    ██ '],
                  'O': ['  █████  ', ' █     █ ', ' █     █ ', ' █     █ ', '  █████  '],
                  'P': ['  █████  ', '  █    █ ', '  █████  ', '  █      ', '  █      '],
                  'Q': ['  █████  ', ' █     █ ', ' █     █ ', ' █   █ █ ', '  ██  █  '],
                  'R': ['  ████   ', '  █   █  ', '  ████   ', '  █   █  ', '  █   █  '],
                  'S': ['   ████  ', '  █      ', '   ███   ', '      █  ', '  ████   '],
                  'T': [' ███████ ', '    █    ', '    █    ', '    █    ', '    █    '],
                  'U': ['  █   █  ', '  █   █  ', '  █   █  ', '  █   █  ', '   ███   '],
                  'V': ['  █   █  ', '  █   █  ', '  █   █  ', '   █ █   ', '    █    '],
                  'W': ['█       █', '█       █', '█   █   █', ' █ █ █ █ ', '  █   █  '],
                  'X': ['  █   █  ', '   █ █   ', '    █    ', '   █ █   ', '  █   █  '],
                  'Y': ['  █   █  ', '   █ █   ', '    █    ', '    █    ', '    █    '],
                  'Z': ['   ████  ', '      █  ', '    █    ', '   █     ', '   ████  '],
                  ' ': ['         ', '         ', '         ', '         ', '         '],
                  "'": ['     ██  ', '      █  ', '         ', '         ', '         '],
                  ',': ['         ', '         ', '         ', '    ██   ', '    ▄█   ']

                  }

    lst = ['a', 'b', 'c', 'd', 'e']
    n_temp = []
    str_temp = ''
    for i in range(1, 13):
        for j in range(len(lst)):
            n_temp.append(ni[lst[j]][i])
            if len(n_temp) // 5 in range(1, 13) and len(n_temp) % 5 == 0:
                k = i - 1
                for a in list(string.ascii_uppercase):
                    if n_temp[5 * k: 5 * (k + 1)] == alpha_dict[a]:
                        str_temp += a
                        pass
                # if n_temp[5 * k: 5 * (k+1)] == ['         ', '         ', '         ', '         ', '         ']:
                #     str_temp += '-'
                #     pass
                if n_temp[5 * k: 5 * (k + 1)] == ['     ██  ', '      █  ', '         ', '         ', '         ']:
                    str_temp += "'"
                    pass
                elif n_temp[5 * k: 5 * (k + 1)] == ['         ', '         ', '         ', '    ██   ', '    ▄█   ']:
                    str_temp += ','
                    pass
                elif n_temp[5 * k: 5 * (k + 1)] == ['         ', '         ', '         ', '         ', '▄▄▄▄▄▄▄▄▄']:
                    str_temp += ' '
                    pass
                pass
            pass
        pass
    if str(str_temp).upper() == check:
        return True
    else:
        return False
        pass
        # n_temp is a single line list, for checking with alpha_dict


def call_game(title):
    new_var = T.decrypt(title)
    n = {'a': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
               7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
               },
         'b': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
               7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
               },
         'c': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
               7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
               },
         'd': {1: '         ', 2: '         ', 3: '         ', 4: '         ', 5: '         ', 6: '         ',
               7: '         ', 8: '         ', 9: '         ', 10: '         ', 11: '         ', 12: '         '
               },
         'e': {1: '▄▄▄▄▄▄▄▄▄', 2: '▄▄▄▄▄▄▄▄▄', 3: '▄▄▄▄▄▄▄▄▄', 4: '▄▄▄▄▄▄▄▄▄', 5: '▄▄▄▄▄▄▄▄▄', 6: '▄▄▄▄▄▄▄▄▄',
               7: '▄▄▄▄▄▄▄▄▄', 8: '▄▄▄▄▄▄▄▄▄', 9: '▄▄▄▄▄▄▄▄▄', 10: '▄▄▄▄▄▄▄▄▄', 11: '▄▄▄▄▄▄▄▄▄', 12: '▄▄▄▄▄▄▄▄▄'
               }
         }
    # WORD HINT
    word_list = list(new_var)
    try:
        print('\n' * 29)
        for p in range(len(word_list)):
            if word_list[p] == ' ':
                n, f_str = word(p + 1, ' ', n)
                n = n
        for j in range(len(word_list) + 1, 13):
            n, f_str = word(j, ' ', n)
            n = n
        if len(new_var) > 8:
            for k in [0, 2, 3]:
                item = word_list[2 ** k]
                if item in word_list:
                    n, f_str = word(2 ** k + 1, str(item.upper()), n)
                    n = n
                    for i in range(len(word_list)):
                        if word_list[i] == item:
                            n, f_str = word(i + 1, item.upper(), n)
                            n = n
                            pass
                        pass
                else:
                    n, f_str = word(2 ** k + 1, item.upper(), n)
                    n = n
                pass
        elif 8 >= len(new_var) > 4:
            for k in [0, 2]:
                item = word_list[2 ** k]
                if item in word_list:
                    n, f_str = word(2 ** k + 1, item.upper(), n)
                    n = n
                    for i in range(len(word_list)):
                        if word_list[i] == item:
                            n, f_str = word(i + 1, item.upper(), n)
                            n = n
                            pass
                        pass
                else:
                    n, f_str = word(2 ** k + 1, item.upper(), n)
                    n = n
                pass
        else:
            for k in [0]:
                item = word_list[2 ** k]
                if item in word_list:
                    n, f_str = word(2 ** k + 1, item.upper(), n)
                    n = n
                    for i in range(len(word_list)):
                        if word_list[i] == item:
                            n, f_str = word(i + 1, item.upper(), n)
                            n = n
                            pass
                        pass
                else:
                    n, f_str = word(2 ** k + 1, item.upper(), n)
                    n = n
                pass
            pass
    except:
        print(f'Error in {new_var}')
        raise
    finally:
        game_status = True
        guess_list = []
        incr_list = []
        while game_status:
            try:
                if len(incr_list) == 0:
                    health_bar = '[ █ █ █ █ █ █ ]'
                    hangman = "\t\t\t\t\t\t\t\t                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    "
                elif len(incr_list) == 1:
                    health_bar = '[ █ █ █ █ █   ]'
                    hangman = "\t\t\t\t\t\t\t\t                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "___|___             "
                elif len(incr_list) == 2:
                    health_bar = '[ █ █ █ █     ]'
                    hangman = "\t\t\t\t\t\t\t\t                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "___|___             "
                elif len(incr_list) == 3:
                    health_bar = '[ █ █ █       ]'
                    hangman = "\t\t\t\t\t\t\t\t                    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   | /              " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |/               " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "___|___             "
                elif len(incr_list) == 4:
                    health_bar = '[ █ █         ]'
                    hangman = "\t\t\t\t\t\t\t\t   __________       " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   | /              " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |/               " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "___|___             "
                elif len(incr_list) == 5:
                    health_bar = '[ █           ]'
                    hangman = "\t\t\t\t\t\t\t\t   __________       " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   | /      |       " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |/               " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "___|___             "
                elif len(incr_list) == 6:
                    health_bar = '[             ]'
                    hangman = "\t\t\t\t\t\t\t\t   __________       " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   | /      |       " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |/      _|_      " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |      |   |     " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |       ¯T¯      " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |    ____|____   " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |        |       " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |        |       " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |       / \      " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |      /   \     " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |     /     \    " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "   |                " \
                              "\n\t\t\t\t\t\t\t\t" \
                              "___|___             "
                print(f_str, '\n' * 2, ' ' * 100, health_bar, '\n', hangman, 'LETTERS ALREADY GUESSED:', ' ' * 90,
                      guess_list if (guess_list != []) else print('\t'), '\n' * 6)
                user_letter = input("\tEnter your guess letter/word here: ")
                if len(user_letter) == 1:
                    if user_letter.upper() in word_list:
                        if user_letter.upper() not in guess_list:
                            guess_list.append(user_letter.upper())
                            for i in range(len(new_var)):
                                if word_list[i] == user_letter.upper():
                                    n, f_str = word(i + 1, user_letter.upper(), n)
                                    n = n
                                    if extract_n_check(n, new_var):  # Use extract_n_check() to check and output results
                                        print('\n' * 22, f_str,)
                                        win_screen(len(guess_list))
                                        game_status = False
                                    else:
                                        pass
                                pass
                        elif user_letter.upper() in guess_list:
                            print("\nSorry, you have already used this letter. Please try another one")
                            time.sleep(3)
                            pass
                        pass
                    elif user_letter.upper() not in list(string.ascii_uppercase):
                        print("\nSorry, this is an INVALID INPUT. Please type in an Alphabet.")
                        time.sleep(3)
                        pass
                    elif user_letter.upper() not in word_list:
                        if user_letter.upper() not in guess_list:
                            guess_list.append(user_letter.upper())
                            incr_list.append(user_letter.upper())
                            pass
                        elif user_letter.upper() in guess_list:
                            print("\nSorry, you have already used this letter. Please try another one")
                            time.sleep(3)
                            pass
                        pass
                    pass
                elif len(user_letter) > 1:
                    if user_letter.upper() == new_var:
                        for i in range(len(new_var)):
                            n, f_str = word(i + 1, new_var[i], n)
                            n = n
                            pass
                        print('\n' * 22, f_str, '\n' * 17,
                              f"Yayy! Well Done! You've guessed the word correctly! It took you {len(guess_list)} tries.")
                        game_status = False
                    elif user_letter.upper() == new_var.replace(' ', ''):
                        pass
                    pass
                print('\n')
            except TypeError:
                raise
                print("\nIt seems you haven't typed a valid character, please use only Alphabets.")
                break
            pass
        pass
    pass


def win_screen(g_len):
    print("..................................................,.::=?7Z$ZZZZ$ZOZ?Z,7$$IZ$ZZ$ZZ77I+~~:.,......,.,.:~~+7?$ZZZZ$$ZZ=$..."
          "....ZZZ$$Z$Z+Z$$ZZZZZZZ,Z7I?=::,.,....,..,.,:~+~$7$ZI?IZZZZZZZZZ=ZZ,=Z$I?+~:,,,...,................................IZ..."
          "....=$OZ$7?=~:,,,..................................................................................................7$..."
          "....ZZ.....................................,............,.::=ZZZ$$?.....:ZZZZZ..ZZ,ZZZ$..ZZZ7ZZ...ZZZZ$I.$ZZ:......$Z..."
          "....$Z.ZZZZZZ.ZZZI.,OZ,ZZ+..:ZZZZZ..ZZZ?.ZZZ=..ZZZZ$,.ZZ7.ZZZZ,,ZZ=......77ZZZ.IOZ,.Z~.+ZZZ..ZZZ~..7ZZZZ:.Z+.......Z$..."
          "....ZZ.?ZZZZ7..Z:.$OZZ.+$ZZ..7Z$Z$...Z...$ZZ7...ZZ$Z,.ZZ..$~ZZ:..Z,.......OZZZ.$ZZ$.Z..ZZZZ..ZZZO..$=ZZZZ,$I.......ZZ..."
          "....IZ..ZZZZZ.Z$.?ZZZZ.7ZZZZ.7ZZZZ. .Z....Z$....7ZZZZ.$,..$ZZZ:~Z.........ZZZZ$ZZZZ,Z..ZZZZ..ZZZZ..Z.7ZZZZ,$.......ZZ..."
          "....?Z...$ZZZZ$..ZZZZZ.+ZZZZ.+ZZZZ...Z...........ZZZZ.Z...$ZZZ?$Z..........ZZZ$,ZZZZ...ZZZZ..ZZZZ..Z:.7$ZZZ,.......ZZ..."
          "....ZZ...,ZZZZ+..ZZZZZ.:ZZZZ.~ZZZZ...Z...........~ZZZ$....?ZZZ?.$.:........$ZZZ.ZZZZ...ZZZZ..OZZZ..$=..?ZZZZ.......$$..."
          "....Z7....ZZZZ=..~ZZZZ.,ZZZ$.,ZZZZ...Z............ZZZZ....~ZZZ$..ZZ.........ZZZ.,ZZ$....ZZZ..ZZZ...ZZ...$Z$$.......$Z..."
          "....ZI....ZZZZ$...7ZZ$.,ZZ$...$ZZZ..7Z............+ZZZ....ZZZZZZZZ? ........ZZI..ZZ.......7$Z$.. ..................$Z..."
          "....Z=...OZZZZZI....ZZZZZ:.....,ZZZZ?..............................................................................~Z..."
          "....=:,............................................................................,:~=+?$,ZZ$ZZZZZ7.$ZZ$$$ZZ$ZZ$$I+7..."
          "....Z,~............,..,:~+I7$$ZZ7Z,Z~ZZZ$$ZIZZZZ$$Z$?++~:,.,..........:~+?7$$Z7ZZZZZ7=Z7$Z$ZZ$~ZZ$77?=~:,..............."
          "....=.......:,:=+77$ZOZ$Z$ZZZZ$ZZZ7IOZZZ7$7I+=:,........................................................................")
    print(f"\n\tYayy! Well Done! You've guessed the word correctly! It took you {g_len} tries.")
    pass


def lose_screen():
    pass


def game():
    time.sleep(0.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                     ________                                                           "
          "                                                     |/    _|_                                                          "
          "                                                     |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "                                                     |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(1.5)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                     ________                                                           "
          "                                                     |/    _|_                                                          "
          "                                                     |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "                                                     |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.5)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                     ________                                                           "
          "                                                     |/    _|_                                                          "
          "                                                     |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "                                                     |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                     ________                                                           "
          "                                                     |/    _|_                                                          "
          "                                                     |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "                                                     |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "                                                     ________                                                           "
          "                                                     |/    _|_                                                          "
          "                                                     |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "                                                     |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "                                                     |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "                                                     |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "                                                     |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                                                              "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                                                              "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                                                                           "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________                                                           "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________               14. Style & Beauty                          "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|                                                         "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________               14. Style & Beauty                          "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|             15. Home & Garden                           "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |                                                           "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________               14. Style & Beauty                          "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|             15. Home & Garden                           "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |               16. Food                                    "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                                                                          "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________               14. Style & Beauty                          "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|             15. Home & Garden                           "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |               16. Food                                    "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                              17. Health & Fitness                        "
          "                                                                                                                        "
          "  8. TV & Movies                                                                                                        "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________               14. Style & Beauty                          "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|             15. Home & Garden                           "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |               16. Food                                    "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                              17. Health & Fitness                        "
          "                                                                                                                        "
          "  8. TV & Movies                                                            18. Automobiles & Machines                  "
          "                                                                                                                        "
          "  9. Anime                                                                                                              "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________               14. Style & Beauty                          "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|             15. Home & Garden                           "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |               16. Food                                    "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                              17. Health & Fitness                        "
          "                                                                                                                        "
          "  8. TV & Movies                                                            18. Automobiles & Machines                  "
          "                                                                                                                        "
          "  9. Anime                                                                  19. Travel & Environment                    "
          "                                                                                                                        "
          "  10. Books                                                                                                             "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    time.sleep(0.1)
    print("\n" * 29)
    print("\n"
          " CHOOSE A TOPIC :-                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          "  1. India                                                                  11. Music                                   "
          "                                                                                                                        "
          "  2. World                                                                  12. Gaming                                  "
          "                                                                                                                        "
          "  3. Politics                                                               13. Sports                                  "
          "                                                                                                                        "
          "  4. Sports                                          ________               14. Style & Beauty                          "
          "                                                     |/    _|_                                                          "
          "  5. Money & Finance                                 |    |_ _|             15. Home & Garden                           "
          "                                                     |    __|__                                                         "
          "  6. Science & Technology                            |      |               16. Food                                    "
          "                                                   __|__   / \                                                          "
          "  7. Celebrity                                                              17. Health & Fitness                        "
          "                                                                                                                        "
          "  8. TV & Movies                                                            18. Automobiles & Machines                  "
          "                                                                                                                        "
          "  9. Anime                                                                  19. Travel & Environment                    "
          "                                                                                                                        "
          "  10. Books                                                                 20. (NEW!) Make your Own                    "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                 Made by Pranjal Pratosh"
          )
    select = input("\t\t (1~20) :")  # Ask the option which they chose
    try:
        if select == '1':
            call_game(T.india())
            pass
        elif select == '2':
            call_game(T.world())
            pass
        elif select == '3':
            pass
        elif select == '4':
            pass
        elif select == '5':
            pass
        elif select == '6':
            pass
        elif select == '7':
            pass
        elif select == '8':
            pass
        elif select == '9':
            pass
        elif select == '10':
            pass
        elif select == '11':
            pass
        elif select == '12':
            pass
        elif select == '13':
            pass
        elif select == '14':
            pass
        elif select == '15':
            pass
        elif select == '16':
            pass
        elif select == '17':
            pass
        elif select == '18':
            pass
        elif select == '19':
            pass
        elif select == '20':
            print("\n" * 29)
            print("Sorry this mode is NOT AVAILABLE yet. It will come in a later version. Stay tuned!")
            time.sleep(5)
            game()
            pass
        else:
            print("\n" * 29)
            print(
                "Sorry, One/More characters are incomprehensible. Please type an integer between 1 & 20 (both inclusive)")
            time.sleep(5)
            game()
    except:
        print("\n" * 29)
        print(
            "Sorry, One/More characters are incomprehensible. Please type an integer between 1 & 20 (both inclusive)")
        time.sleep(5)
        game()
    pass


def instr():
    t1 = 1  # Change this to change the speed of the Tutorial.
    print("\n"  # ©pranjal_pratosh
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "        __________                                                                                                      "
          "        |/      _|_                                                                                                     "
          "        |      |   |                                                                                                    "
          "        |       ¯T¯                                                                                                     "
          "        |    ____|____                                                                                                  "
          "        |        |                                                                                                      "
          "        |        |                                                                                                      "
          "        |       / \                                                                                                     "
          "      __|___   /   \                                                                                                    "
          )
    time.sleep(t1 / 2)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "           __________                                                                                                   "
          "           |/      _|_                                                                                                  "
          "           |      |   |                                                                                                 "
          "           |       ¯T¯                                                                                                  "
          "           |    ____|____                                                                                               "
          "           |        |                                                                                                   "
          "           |        |                                                                                                   "
          "           |       / \                                                                                                  "
          "         __|___   /   \                                                                                                 "
          "                                                                                                                        "
          )
    time.sleep(t1 / 2)
    print("\n" * 29)
    print("\n"  # ©pranjal_pratosh
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "              __________                                                                                                "
          "              |/      _|_                                                                                               "
          "              |      |   |                                                                                              "
          "              |       ¯T¯                                                                                               "
          "              |    ____|____                                                                                            "
          "              |        |                                                                                                "
          "              |        |                                                                                                "
          "              |       / \                                                                                               "
          "              |      /   \                                                                                              "
          "            __|___                                                                                                      "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 / 2)
    print("\n" * 29)
    print("\n"  # WELCOME TO HANGMAN
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                      __________                                                                                        "
          "                      | /      |                                                                                        "
          "                      |/      _|_                                                                                       "
          "                      |      |   |                                                                                      "
          "                      |       ¯T¯                                                                                       "
          "                      |    ____|____                                                                                    "
          "                      |        |                                                                                        "
          "                      |        |                                                                                        "
          "                      |       / \                                                                                       "
          "                      |      /   \                                                                                      "
          "                    __|___                                                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 / 2)
    print("\n" * 29)
    print("\n"  # ©pranjal_pratosh
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                  __________                                                                            "
          "                                  | /      |                                                                            "
          "                                  |/      _|_                                                                           "
          "                                  |      |   |                                                                          "
          "                                  |       ¯T¯                                                                           "
          "                                  |    ____|____                                                                        "
          "                                  |        |                                                                            "
          "                                  |        |                                                                            "
          "                                  |       / \                                                                           "
          "                                  |      /   \                                                                          "
          "                                  |     /     \                                                                         "
          "                                __|___                                                                                  "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 / 2)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                   This is the Hangman                                                                                  "
          "                                            __________                                                                  "
          "                                            | /      |                                                                  "
          "                                            |/      _|_                                                                 "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 3)
    print("\n" * 29)
    print("\n"
          "                   This is the Hangman                                                                                  "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_                                                                 "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 2)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 4)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 4)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 2.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      ___               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"  # ©pranjal_pratosh
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/                        And this is your health bar                       "
          "                                            |       ___                                                                 "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/                        And this is your health bar                       "
          "                                            |                                                                           "
          "                                            |        ___                                                                "
          "                                            |       |   |                                                               "
          "                                            |        ¯T¯                                                                "
          "                                            |     ____|____                                                             "
          "                                            |         |                                                                 "
          "                                            |         |                                                                 "
          "                                            |        / \                                                                "
          "                                            |       /   \                                                               "
          "                                         ___|___   /     \                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/                        And this is your health bar                       "
          "                                            |                                                                           "
          "                                            |        ___                                                                "
          "                                            |       |   |                                                               "
          "                                            |     \  ¯T¯  /                                                             "
          "                                            |      \__|__/                                                              "
          "                                            |         |                                                                 "
          "                                            |         |                                                                 "
          "                                            |        / \                                                                "
          "                                            |       /   \                                                               "
          "                                         ___|___   /     \                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 4)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 4)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 2)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                                                                  "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                                                                  "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █ █ ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █   ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                  This is the Hangman                                                                                   "
          "                                            __________                  [ █ █ █ █ █   ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_               And this is your health bar                       "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                                                                 "
          "                                            |    ____|____                                                              "
          "                                            |        |                                                                  "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                 You will be given a word to guess.                                                                     "
          "                                                                                                                        "
          "                              Guess it right, and you WIN.                                                              "
          "                                                                                                                        "
          "                                       However, guess even ONE letter WRONG...                                          "
          "                                                                                                                        "
          "                                                  You lose a life !                                                     "
          "                                                                                                                        "
          "                                        PRESS ENTER TO CONTINUE                                                         "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    input()
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                                                        [ █ █ █ █ █ █ ]                                 "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                           For every wrong word / letter                "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 4)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                                                        [ █ █ █ █ █ █ ]                                 "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                           For every wrong word / letter                "
          "                                                                                                                        "
          "                                                                                     Your Gallows will build itself     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                                                        [ █ █ █ █ █   ]                                 "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                           For every wrong word / letter                "
          "                                                                                                                        "
          "                                                                                     Your Gallows will build itself     "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                                                        [ █ █ █ █     ]                                 "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                                                        [ █ █ █       ]                                 "
          "                                            | /                                                                         "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                  [ █ █         ]                                 "
          "                                            | /                                                                         "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                  [ █           ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                  [ █           ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                          At last, you'll be HANGED !                      "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 4)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                                                                  "
          "                                            | /      |                                                                  "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                          At last, you'll be HANGED !                      "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                  [ █           ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                          At last, you'll be HANGED !                      "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                                                                  "
          "                                            | /      |                                                                  "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                          At last, you'll be HANGED !                      "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 0.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                  [ █           ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/                                                                          "
          "                                            |                                                                           "
          "                                            |                              For every wrong word / letter                "
          "                                            |                                                                           "
          "                                            |                                        Your Gallows will build itself     "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                                                                           "
          "                                            |                          At last, you'll be HANGED !                      "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                  [             ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_                                                                 "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                    For every wrong word / letter                "
          "                                            |    ____|____                                                              "
          "                                            |        |                               Your Gallows will build itself     "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                          At last, you'll be HANGED !                      "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )
    time.sleep(t1 * 1.5)
    print("\n" * 29)
    print("\n"
          "                                                                                                                        "
          "                                            __________                  [             ]                                 "
          "                                            | /      |                                                                  "
          "                                            |/      _|_                                                                 "
          "                                            |      |   |                                                                "
          "                                            |       ¯T¯                    For every wrong word / letter                "
          "                                            |    ____|____                                                              "
          "                                            |        |                               Your Gallows will build itself     "
          "                                            |        |                                                                  "
          "                                            |       / \                                                                 "
          "                                            |      /   \                                                                "
          "                                            |     /     \                                                               "
          "                                            |                          At last, you'll be HANGED !                      "
          "                                         ___|___                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          "                   ARE YOU READY TO BEGIN ? (Y/N)                                                                       "
          "                                                                                                                        "
          "                                                                                                                        "
          "                                                                                                                        "
          )

    conf = input("\t\t")

    # if yes, put different animation
    if conf.upper() == 'Y':
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          At last, you'll be HANGED !                      "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          █At last, you'll be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Ma█ last, you'll be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made█ast, you'll be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made b█t, you'll be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by █ you'll be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pr█ou'll be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pran█'ll be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranja█l be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranjal █be HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranjal Pr█ HANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranjal Prat█ANGED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranjal Pratos█GED !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranjal Pratosh █D !                     "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.25)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranjal Pratosh   █                      "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.5)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |      /   \                                                                "
              "                                            |     /     \                                                               "
              "                                            |                          Made by Pranjal Pratosh                          "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.5)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                            __________                                                                  "
              "                                            | /      |                                                                  "
              "                                            |/      _|_                                                                 "
              "                                            |      |   |                                                                "
              "                                            |       ¯T¯                                                                 "
              "                                            |    ____|____                                                              "
              "                                            |        |                                                                  "
              "                                            |        |                                                                  "
              "                                            |       / \                                                                 "
              "                                            |     /     \                                                               "
              "                                         ___|___                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                         Made by Pranjal Pratosh                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.5)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                   __________                                                           "
              "                                                   |/      _|_                                                          "
              "                                                   |      |   |                                                         "
              "                                                   |       ¯T¯                                                          "
              "                                                   |     ___|___                                                        "
              "                                                   |        |                                                           "
              "                                                   |       / \                                                          "
              "                                                 __|__                                                                  "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                Made by Pranjal Pratosh                 "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(t1 * 0.5)
        print("\n" * 29)
        print("\n"  # ©pranjal_pratosh
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                     ________                                                           "
              "                                                     |/    _|_                                                          "
              "                                                     |    |   |                                                         "
              "                                                     |     ¯T¯                                                          "
              "                                                     |    __|__                                                         "
              "                                                     |      |                                                           "
              "                                                   __|__   / \                                                          "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                               Made by Pranjal Pratosh  "
              "                                                                                                                        "
              )
        game()
    elif conf.upper() == 'N':
        print("\n" * 29)
        time.sleep(1)
        print(" Game will close in 5.. ")
        time.sleep(1)
        print("\n" * 29)
        print(" Game will close in 5..  4..")
        time.sleep(1)
        print("\n" * 29)
        print(" Game will close in 5..  4..  3..")
        time.sleep(1)
        print("\n" * 29)
        print(" Game will close in 5..  4..  3..  2..")
        time.sleep(1)
        print("\n" * 29)
        print(" Game will close in 5..  4..  3..  2..  1..")
        time.sleep(1)
    pass


def anim():
    t = 0.2  # Change this to change the speed of the animation
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                  ___         "
          "        |                                                                                                  |   |        "
          "        |                                                                                                   ¯T¯         "
          "        |                                                                                                  __|__        "
          "        |                                                                                                /   |   \      "
          "        |                                                                                               /    |    \     "
          "        |                                                                                               |    |     |    "
          "        |                                                                                                   / \         "
          "        |                                                                                                  /   \        "
          "        |                                                                                                  |    |       "
          "     ___|___                                                                                              _|    |_      "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                  ___         "
          "        |                                                                                                  |   |        "
          "        |                                                                                                   ¯T¯         "
          "        |                                                                                                  __|__        "
          "        |                                                                                                /   |   \      "
          "        |                                                                                               /    |    \     "
          "        |                                                                                              /     |     |    "
          "        |                                                                                                   / \         "
          "        |                                                                                                  /   \        "
          "        |                                                                                                  |    |       "
          "     ___|___                                                                                              _|   _|       "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                  ___         "
          "        |                                                                                                  |   |        "
          "        |                                                                                                   ¯T¯         "
          "        |                                                                                                  __|__        "
          "        |                                                                                                /   |   \      "
          "        |                                                                                               /    |    \     "
          "        |                                                                                            ¯¯¯     |    /     "
          "        |                                                                                                   / \         "
          "        |                                                                                                  /   \        "
          "        |                                                                                                  |    |       "
          "     ___|___                                                                                              _|   _|       "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                  ___         "
          "        |                                                                                                  |   |        "
          "        |                                                                                                   ¯T¯         "
          "        |                                                                                                  __|__        "
          "        |                                                                                             \  /   |   \      "
          "        |                                                                                              ¯¯    |    \     "
          "        |                                                                                                    |     \    "
          "        |                                                                                                   / \         "
          "        |                                                                                                  /   \        "
          "        |                                                                                                  |    |       "
          "     ___|___                                                                                              _|   _|       "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                  ___         "
          "        |                                                                                                  |   |        "
          "        |                                                                                                   ¯T¯         "
          "        |                                                                                                  __|__        "
          "        |                                                                                              \ /   |   \      "
          "        |                                                                                               ¯    |    \     "
          "        |                                                                                                    |     \    "
          "        |                                                                                                   / \         "
          "        |                                                                                                  /   \        "
          "        |                                                                                                  |    \       "
          "     ___|___                                                                                              _|    _\      "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                  ___         "
          "        |                                                                                                  |   |        "
          "        |                                                                                                   ¯T¯         "
          "        |                                                                                             \    __|__        "
          "        |                                                                                              \ /   |   \      "
          "        |                                                                                               ¯    |    \     "
          "        |                                                                                                    |     \    "
          "        |                                                                                                   / \         "
          "        |                                                                                                  /   \        "
          "        |                                                                                                  |    \__     "
          "     ___|___                                                                                              _|       |    "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                  ___         "
          "        |                                                                                             \    |   |        "
          "        |                                                                                              \    ¯T¯         "
          "        |                                                                                               \ ___|__        "
          "        |                                                                                                    |  \       "
          "        |                                                                                                    |   \      "
          "        |                                                                                                    |   _\     "
          "        |                                                                                                   / \         "
          "        |                                                                                                  /   \        "
          "        |                                                                                                 |     \___    "
          "     ___|___                                                                                             _|         |   "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                                ___           "
          "        |                                                                                            \   |   |          "
          "        |                                                                                             \   ¯T¯           "
          "        |                                                                                              \___|__          "
          "        |                                                                                                  |  \         "
          "        |                                                                                                  |   \        "
          "        |                                                                                                  |    \_      "
          "        |                                                                                                 / \           "
          "        |                                                                                                /   \          "
          "        |                                                                                               |     \___      "
          "     ___|___                                                                                           _|         |     "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                         ___                  "
          "        |                                                                                         |   |                 "
          "        |                                                                                          ¯T¯                  "
          "        |                                                                                     ______|_____              "
          "        |                                                                                           |                   "
          "        |                                                                                           |                   "
          "        |                                                                                           |                   "
          "        |                                                                                          / \                  "
          "        |                                                                                         /   \                 "
          "        |                                                                                        |     \___             "
          "     ___|___                                                                                    _|         |            "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                                ___                           "
          "        |                                                                            \   |   |                          "
          "        |                                                                             \   ¯T¯                           "
          "        |                                                                              \___|__                          "
          "        |                                                                                  |  \                         "
          "        |                                                                                  |   \                        "
          "        |                                                                                  |    \_                      "
          "        |                                                                                 / \                           "
          "        |                                                                                /   \                          "
          "        |                                                                               |     \___                      "
          "     ___|___                                                                           _|         |                     "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                                     ___                                      "
          "        |                                                                     |   |                                     "
          "        |                                                                      ¯T¯                                      "
          "        |                                                                 ______|_____                                  "
          "        |                                                                       |                                       "
          "        |                                                                       |                                       "
          "        |                                                                       |                                       "
          "        |                                                                      / \                                      "
          "        |                                                                     /   \                                     "
          "        |                                                                    |     \___                                 "
          "     ___|___                                                                _|         |                                "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                                       ___                                                    "
          "        |                                                   \   |   |                                                   "
          "        |                                                    \   ¯T¯                                                    "
          "        |                                                     \___|__                                                   "
          "        |                                                         |  \                                                  "
          "        |                                                         |   \                                                 "
          "        |                                                         |    \_                                               "
          "        |                                                        / \                                                    "
          "        |                                                       /   \                                                   "
          "        |                                                      |     \___                                               "
          "     ___|___                                                  _|         |                                              "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                                         ___                                                                  "
          "        |                                         |   |                                                                 "
          "        |                                          ¯T¯                                                                  "
          "        |                                     ______|_____                                                              "
          "        |                                           |                                                                   "
          "        |                                           |                                                                   "
          "        |                                           |                                                                   "
          "        |                                          / \                                                                  "
          "        |                                         /   \                                                                 "
          "        |                                        |     \___                                                             "
          "     ___|___                                    _|         |                                                            "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/                             ___                                                                              "
          "        |                         \   |   |                                                                             "
          "        |                          \   ¯T¯                                                                              "
          "        |                           \___|__                                                                             "
          "        |                               |  \                                                                            "
          "        |                               |   \                                                                           "
          "        |                               |    \_                                                                         "
          "        |                              / \                                                                              "
          "        |                             /   \                                                                             "
          "        |                            |     \___                                                                         "
          "     ___|___                        _|         |                                                                        "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/               ___                                                                                            "
          "        |               |   |                                                                                           "
          "        |                ¯T¯                                                                                            "
          "        |           ______|_____                                                                                        "
          "        |                 |                                                                                             "
          "        |                 |                                                                                             "
          "        |                 |                                                                                             "
          "        |                / \                                                                                            "
          "        |               /   \                                                                                           "
          "        |              |     \___                                                                                       "
          "     ___|___          _|         |                                                                                      "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/        ___                                                                                                   "
          "        |        |   |                                                                                                  "
          "        |         ¯T¯                                                                                                   "
          "        |        __|__                                                                                                  "
          "        |    \ /   |   \                                                                                                "
          "        |     ¯    |    \                                                                                               "
          "        |          |     \                                                                                              "
          "        |         / \                                                                                                   "
          "        |        /   \                                                                                                  "
          "        |        |    \                                                                                                 "
          "     ___|___    _|    _\                                                                                                "
          )
    time.sleep(t)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/       ___                                                                                                    "
          "        |       |   |                                                                                                   "
          "        |        ¯T¯                                                                                                    "
          "        |       __|__                                                                                                   "
          "        |     /   |   \                                                                                                 "
          "        |    /    |    \                                                                                                "
          "        |   /     |     |                                                                                               "
          "        |        / \                                                                                                    "
          "        |       /   \                                                                                                   "
          "        |       |    |                                                                                                  "
          "     ___|___   _|   _|                                                                                                  "
          )
    time.sleep(t * 0.5)
    print("\n" * 29)
    print("\n"
          "        __________                                                                                                      "
          "        | /      |                                                                                                      "
          "        |/      _|_                                                                                                     "
          "        |      |   |                                                                                                    "
          "        |       ¯T¯                                                                                                     "
          "        |    ____|____                                                                                                  "
          "        |        |                                                                                                      "
          "        |        |                                                                                                      "
          "        |       / \                                                                                                     "
          "        |      /   \                                                                                                    "
          "        |     /     \                                                                                                   "
          "        |                                                                                                               "
          "     ___|___                                                                                                            "
          )
    time.sleep(2)
    print("\n" * 29)
    print("\n"  # WELCOME TO HANGMAN
          "       777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777..777777..7777777777777.777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777..777777.7777777777777..777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777.777777..777.....77777..77777777I.....7777.....777.....7...777,.....7777777777777777777777777777777           "
          "       777.77.. 7.77=.7777..7777.77777777..7777777I.7777=.77..77..7..77..7777.7777777777777777777777777777777           "
          "       77+.7.=.7I.77.......7777..7777777..77777777.=77777.77.=7..77.77.......+7777777777777777777777777777777           "
          "       77....7.7.?77.7777777777..7777777..77777777.77777..7I.77.~77.77..7777777777777777777777777777777777777           "
          "       77.=.77...777..777777777..777:777..7777 777..777..77..77.77..77..7777777777777777777777777777777777777           "
          "       77..777~..7777.....?77777....777777....77777....7777.77:.77.7777=.....77777777777777777777777777777777           "
          "       777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777777.777777777777777777777777777..7777+.777777777777777777777777777777777777777777777777777777777777           "
          "       777........7777 ...  7777777777777.77777..7777,..,:777.?7~..777777+...+.7?.7..77.I7777I...?.77..77..77           "
          "       77777..7777777..777..777777777777..77777.+77..777=.777.=.77..777..7777.77...7..~?.77..I777.777...?77.7           "
          "       77777.7777777.=7777..777777777777........77..7777..777..777..77..7777..77..77.~7..7?.7777+.777..7777.7           "
          "       77777.777777,.77777..777777777777.77777..77.77777.777.. 777.,77.,7777..77.77..77.77..7777..777.7777..7           "
          "       7777..777777..7777..777777777777..77777.=77.7777..777.,7777.777.:777..77?.77.=77.77..777..:77..7777.,7           "
          "       77777....= 77......7777777777777..77777.777.....I.777.7777..777,......77..77.77..777....7.777..7777.77           "
          "       77777777777777777777777777777777777777777777777777777777777777777777..77777777777777777777777777777777           "
          "       777777777777777777777777777777777777777777777777777777777777777......777777777777777777777777777777777           "
          "       7__________7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "        |/      _|_                                                                                                     "
          "        |      |   |                                                                                                    "
          "        |       ¯T¯                                                                                                     "
          "        |    ____|____                                                                                                  "
          "        |        |                                                                                                      "
          "        |        |                                                                                                      "
          "        |       / \                                                                                                     "
          "      __|___   /   \                                                                                                    "
          )
    time.sleep(2)
    print("\n" * 29)
    print("\n"  # WELCOME TO HANGMAN
          "       777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777..777777..7777777777777.777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777..777777.7777777777777..777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777.777777..777.....77777..77777777I.....7777.....777.....7...777,.....7777777777777777777777777777777           "
          "       777.77.. 7.77=.7777..7777.77777777..7777777I.7777=.77..77..7..77..7777.7777777777777777777777777777777           "
          "       77+.7.=.7I.77.......7777..7777777..77777777.=77777.77.=7..77.77.......+7777777777777777777777777777777           "
          "       77....7.7.?77.7777777777..7777777..77777777.77777..7I.77.~77.77..7777777777777777777777777777777777777           "
          "       77.=.77...777..777777777..777:777..7777 777..777..77..77.77..77..7777777777777777777777777777777777777           "
          "       77..777~..7777.....?77777....777777....77777....7777.77:.77.7777=.....77777777777777777777777777777777           "
          "       777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "       777777.777777777777777777777777777..7777+.777777777777777777777777777777777777777777777777777777777777           "
          "       777........7777 ...  7777777777777.77777..7777,..,:777.?7~..777777+...+.7?.7..77.I7777I...?.77..77..77           "
          "       77777..7777777..777..777777777777..77777.+77..777=.777.=.77..777..7777.77...7..~?.77..I777.777...?77.7           "
          "       77777.7777777.=7777..777777777777........77..7777..777..777..77..7777..77..77.~7..7?.7777+.777..7777.7           "
          "       77777.777777,.77777..777777777777.77777..77.77777.777.. 777.,77.,7777..77.77..77.77..7777..777.7777..7           "
          "       7777..777777..7777..777777777777..77777.=77.7777..777.,7777.777.:777..77?.77.=77.77..777..:77..7777.,7           "
          "       77777....= 77......7777777777777..77777.777.....I.777.7777..777,......77..77.77..777....7.777..7777.77           "
          "       77777777777777777777777777777777777777777777777777777777777777777777..77777777777777777777777777777777           "
          "       777777777777777777777777777777777777777777777777777777777777777......777777777777777777777777777777777           "
          "       7__________7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777           "
          "        |/      _|_                                                                                                     "
          "        |      |   |                                                                   Made by Pranjal Pratosh          "
          "        |       ¯T¯                                                                                                     "
          "        |    ____|____                                                                                                  "
          "        |        |                           TYPE 'T' TO BEGIN TUTORIAL                                                 "
          "        |        |                           TYPE 'S' TO START GAME                                                     "
          "        |       / \                          (THEN PRESS ENTER)                                                         "
          "      __|___   /   \                                                                                                    "
          )

    tutorial = input()
    if tutorial.upper() == 'T':
        instr()
    elif tutorial.upper() == "S":
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "        __________                                                                                                      "
              "        |/      _|_                                                                                                     "
              "        |      |   |                                                                   Made by Pranjal Pratosh          "
              "        |       ¯T¯                                                                                                     "
              "        |    ____|____                                                                                                  "
              "        |        |                                                                                                      "
              "        |        |                                                                                                      "
              "        |       / \                                                                                                     "
              "      __|___   /   \                                                                                                    "
              )
        time.sleep(1)
        print("\n" * 29)
        print("\n"
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "          __________                                                                                                    "
              "          |/      _|_                                                                                                   "
              "          |      |   |                                                                                                  "
              "          |       ¯T¯                                                                                                   "
              "          |    ____|____                                                                                                "
              "          |        |                                                                    Made by Pranjal Pratosh         "
              "          |        |                                                                                                    "
              "          |       / \                                                                                                   "
              "        __|___   /   \                                                                                                  "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(0.5)
        print("\n" * 29)
        print("\n"  # ©pranjal_pratosh
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                     ________                                                                           "
              "                                     |/    _|_                                                                          "
              "                                     |    |   |                                                                         "
              "                                     |     ¯T¯                                                                          "
              "                                     |  ____|____                                                                       "
              "                                     |      |                                                                           "
              "                                     |     / \                                                                          "
              "                                   __|__  /   \                                                                         "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                           Made by Pranjal Pratosh      "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              )
        time.sleep(0.5)
        print("\n" * 29)
        print("\n"  # ©pranjal_pratosh
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                     ________                                                           "
              "                                                     |/    _|_                                                          "
              "                                                     |    |   |                                                         "
              "                                                     |     ¯T¯                                                          "
              "                                                     |    __|__                                                         "
              "                                                     |      |                                                           "
              "                                                   __|__   / \                                                          "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                                                        "
              "                                                                                               Made by Pranjal Pratosh  "
              "                                                                                                                        "
              )
        game()
        pass

    pass


if __name__ == '__main__':
    T = Topic()
    # extract_n_check(n, '')
    # call_game(T.india())
    loader()
    home()
    anim()
    input()
