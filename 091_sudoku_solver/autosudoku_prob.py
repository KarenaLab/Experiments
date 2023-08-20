# Auto Sudoku [P091] ---------------------------------------------------
# Solves Sudoku with use of restraints and probability, NO bactracking.

# Versions
# 01 - Ago 15th, 2023 - Starter
# 02


# Insights, improvements and bugfix
# Add a debug move (more detailed than verbose)
#


# Libraries
import os

# Functions
def get_all_boards(extension=".txt"):
    """
    Get all files with given **extension** from current folder.

    """
    extension = extension.lower()
    extension = extension.replace(".", "")
    
    all_items = os.listdir()

    wish_list = list()
    for f in all_items:
        if(os.path.isfile(f) == True):
            name, ext = f.split(".")
            if(extension == ext):
                wish_list.append(f)


    return wish_list    


def read_board(filename):
    """
    Reads a .txt file with the Sudoku game

    """
    file = open(filename, mode="r")

    board = list()
    while(True):
        line = file.readline()

        if(len(line) > 0):
            line = line.replace("\n", "")
            line = line.split(" ")
            line = list(map(int, line))
            board.append(line)

        else:
            file.close()
            break

                
    return board


def print_board(board, title="Board", zero_print=" ", na_print="."):
    """
    Prints/shows the board in a better away :)

    """
    print(f" {title}")
    i = 0
    for i in range(0, 9):
        # Horizontal division for cells
        if(i % 3 == 0): print(" " + ("-" * 25))

        j = 0
        col = " "
        for j in range(0, 9):
            if(j % 3 == 0): col = col + "| "

            cell = str(board[i][j])
            if(cell == "0"):
                cell = zero_print
                
            elif(cell == "NA"):
                cell = na_print

            col = col + cell + " "
            j = j + 1

        col = col + "| "
        print(col)
        i = i + 1

    print(" " + ("-" * 25) + "\n")


    return None


def get_pos(board, row, col):
    """
    Returns the value in the given **row** and **col** from the
    **board**.

    """
    pos = board[row][col]


    return pos


def get_row(board, row):
    """
    Get a specific row (0~8) from board.
    Horizontal line.

    """
    data = list()    
    for i in range(0, 9):
        data.append(board[row][i])


    return data


def get_col(board, col):
    """
    Get a specific column (0~8) from board.
    Vertical line.

    """
    data = list()
    for i in range(0, 9):
        data.append(board[i][col])


    return data


def get_cell(board, cell):
    """
    Get a specific cell (0~8) from board [3x3].
    Returns a flatten list of the box selected.

    """
    # Calculate the initial position (upper/left) of the cell 
    i_offset = (cell // 3) * 3
    j_offset = (cell % 3) * 3

    data = list()
    for i in range(i_offset, i_offset+3):
        for j in range(j_offset, j_offset+3):
            data.append(board[i][j])
            
            
    return data


def count_number(board, number):
    """
    Returns the quantity of the **number** in the board.
    (0 <= x <= 9).

    """
    count = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if(board[i][j] == number):
                count = count + 1


    return count


def count_fill(board):
    """
    Returns the quantity of all filled cells in the board.
    (0 <= x <= 81).

    """
    count = 0
    for i in range(1, 10):
        count = count + count_number(board, i)


    return count


def count_empty(board):
    """
    Returns the quantity of empty cells in the board.
    (0 <= x <= 81).

    """
    count = count_number(board, 0)


    return count


def filled_sequence(board):
    """
    Returns a list with priorities to find (to be used at probability)
    in a reverse mode.

    """
    numbers = [i for i in range(1, 10)]
    counter = list()

    # Get the number of filled items by number
    for i in numbers:
        count = count_number(board, i)
        counter.append(count)

    # Remove items with count = 9 (not need to be analized).
    _counter = counter[:]
    for i in _counter:
        if(i == 9):
            numbers.pop(i)
            counter.pop(i)

    # Sort the numbers by the reverse order of appearing items.
    numbers = [i for _, i in sorted(zip(counter, numbers), reverse=True)]   


    return numbers

    
def find_cell(row, col):
    """
    Returns the cell (0~8) by an address of **row** and **col**.

    """
    row_index = row // 3
    col_index = col // 3

    cell = (row_index * 3) + col_index


    return cell


def remove_zero(array):
    """
    Remove zeros from the list.

    """
    data = list()
    
    for i in range(0, len(array)):
        if(array[i] != 0):
            data.append(array[i])


    return data


def outer_join(left, right, zero_off=True):
    """
    Performs the FULL OUTER JOIN between two lists and returns
    the unique values.
    Returns the unique values of the two merged lists.
    
    """
    outer_join = list(set(left + right))

    if(zero_off == True):
        outer_join = remove_zero(outer_join)


    return outer_join


def inverse(array):
    """
    Inverts the values of the list.
    Returns the number (1~9) that are NOT in the list.
    
    """
    inverse = list()
    for i in range(1, 10):
        if(array.count(i) == 0):
            inverse.append(i)


    return inverse


def solution_by_exclusion(board, verbose=True):
    """
    Performs one full turn of finding solution by exclusion (easy level)
    Returns the filled board after the turn and the number of solutions
    found.

    """
    board_shadow = board[:]
    solutions = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if(get_pos(board, i, j) == 0):
                # Get col, row and cell filled numbers
                row = get_row(board, i)
                col = get_col(board, j)
                cell = get_cell(board, find_cell(i, j))

                point = outer_join(row, col)
                point = outer_join(point, cell)
                point = inverse(point)

                if(len(point) == 1):
                    board_shadow[i][j] = point[0]
                    solutions = solutions + 1

                    if(verbose == True):
                        print(f" > Position[{i}][{j}]: {point[0]}")


    if(verbose == True):
        print(f" > Total of solutions found: {solutions} \n")


    return board_shadow, solutions
                        
                
            
# Program --------------------------------------------------------------
board_list = get_all_boards(extension=".txt")

for b in board_list:
    print(f" ****  Solving '{b}'  **** \n")    
    board = read_board(b)
    print_board(board, title="Board - Initial")

    turn = 0
    while(True):
        board, solutions = solution_by_exclusion(board, verbose=True)
        turn = turn + 1
        
        if(solutions > 0):
            print_board(board, title=f"Board - Turn {turn}")

        else:
            break

