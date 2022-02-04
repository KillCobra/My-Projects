num_search = input('\nEnter numbers across, with <space> for blank boxes: ').replace(' ', '0')
nsl = [int(i) for i in num_search]
l1 = [nsl[9*i:(i+1)*9] for i in range(9)]
l2 = [[k for k in num_search][9*i:(i+1)*9] for i in range(9)]


def puzzle(a):
    print()
    for i in range(9):
        for j in range(9):
            print(a[i][j], end=" ")
        print()
    print()
    for i in range(9):
        for j in range(9):
            if a[i][j] == int(l2[i][j]):
                a[i][j] = '-'
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def sudoku(grid, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)
    for num in range(1, 10, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


if sudoku(l1, 0, 0):
    puzzle(l1)
else:
    print("Solution does not exist :(")

input()
