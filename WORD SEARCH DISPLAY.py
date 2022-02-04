# WORD SEARCH DISPLAY ##
import numpy as np
import enchant

word_search = input('\nLetters (NO SPACES)(--Across-->): ')  # letters seperated by a space
x, y = int(input('Rows: ')), int(input('Columns: '))  # 12 rows and 18 columns
length = True
wsl = [i for i in word_search]
l1 = []

while length:
    print("\nType '3' for words of three letters and longer"
          "\n\t '4' for four letters or longer ... etc"
          "\n Type 'end' to finish")
    length = input('\t : ')
    if length.isdigit():
        length = int(length)
    elif length.lower() == 'end':
        break


    def ch4w(word):  # Check 4 Word
        eng_dict = enchant.Dict("en_US")
        if len(word) >= 3:
            for k in range(length - 3, len(word)):
                for i in range(len(word) - k - 2):
                    if eng_dict.check(word[i:i + 3 + k]):  # enchant.dict_exists(word[i:i + 3])
                        print(word[i:i + 3 + k], '\t', i + 1, i + k + 3)
        pass


    for i in range(x):
        l1.append(wsl[i * y:(i + 1) * y])
    matrix = np.array(l1)

    print("\n  The numbers are the 'start:end' of that row/column/diagonal, as per the direction.")
    print('\n\t', 'Diagonal SW - NE (Starting Top Left)')

    # Diagonal SW - NE ##
    diags = [matrix[::-1, :].diagonal(i) for i in range(-x + 1, y)]
    for n in diags:
        ch4w(''.join(n.tolist()))

    print('\t', 'Diagonal NW - SE (Starting Top Right)')

    # Diagonal NW - SE ##
    diags2 = [matrix.diagonal(i) for i in range(y - 1, -x, -1)]
    for m in diags2:
        ch4w(''.join(m.tolist()))

    print('\n\t', 'Top - Bottom')

    # ndArray[start_row_index : end_row_index , start_column_index : end_column_index]
    # ndArray[start_index: end_index ,  :]
    columns = [matrix[:, :]]

    # Top - Bottom ##
    for j in range(y):
        l2 = []
        for i in range(x):
            l2.append(l1[i][j])
        ch4w(''.join(l2))

    print('\n\t', 'Left - Right')

    # Left - Right ##
    for i in range(x):
        l3 = []
        for j in range(y):
            l3.append(l1[i][j])
        ch4w(''.join(l3))

    print('\n\t', 'Right - Left')

    # Right - Left ##
    for i in range(x):
        l4 = []
        for j in range(y):
            l4.append(l1[i][y - j - 1])
        ch4w(''.join(l4))

    print('\n\t', 'Bottom - Top')

    # Bottom - Top ##
    for j in range(y):
        l5 = []
        for i in range(x):
            l5.append(l1[x - i - 1][j])
        ch4w(''.join(l5))

    print("\n  The numbers are the 'start:end' of that row/column/diagonal, as per the direction.")
    print(
        "\n\tYou can use this link: https://wordsearch.lukasjoswiak.com/ if you didn't understand the numbers ;)\n")
    for n in range(y):
        print(f"\t{' '.join(wsl[y * n:(n + 1) * y])}")
    pass
