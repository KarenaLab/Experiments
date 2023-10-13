# Auto Sudoku [P091] ---------------------------------------------------
# Solves Sudoku with use of restraints and probability, NO bactracking.

# Versions
# 01 - Ago 15th, 2023 - Starter
# 02 - Sep 08th, 2023 - Probabilities lines


# Insights, improvements and bugfix
# Add a debug move (more detailed than verbose)
# Change the initial matrix 0 for "." (need to change all algorithm seq)
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


def print_board(board, title="Board", zero_print=" "):
    """
    Prints/shows the board in a better away :)

    """
    print(f"\n {title}")

    for i in range(0, 9):
        # Horizontal division for cells
        if(i % 3 == 0):
            print(" " + ("-" * 25))

        # Row with numbers and Vertical division for cells
        col = " "
        for j in range(0, 9):
            if(j % 3 == 0):
                col = col + "| "

            cell = str(board[i][j])
            if(cell == "0"):
                cell = zero_print

            col = col + cell + " "

        col = col + "| "
        print(col)

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
    i_offset, j_offset = _cell_offset(cell)

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


def priority_sequence(board):
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
    for i in range(0, 9):
        if(counter[i] == 9):
            numbers[i] = "."
            counter[i] = "."        
              
    counter = [i for i in counter if i != "."]
    numbers = [i for i in numbers if i != "."]

    
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
    data = [i for i in array if i != 0]
    

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
    Returns the filled **board** after the turn and the number of
    **solutions** found.

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

                # Get all numbers (exclusion) for the point
                point = outer_join(row, col)
                point = outer_join(point, cell)
                point = inverse(point)

                # IF the point is unique, it is the solution
                if(len(point) == 1):
                    board_shadow[i][j] = point[0]
                    solutions = solutions + 1

                    if(verbose == True):
                        print(f" > Position[{i}][{j}]: {point[0]} - Exclusion")


    return board_shadow, solutions
   
    
def probability_board(board, number):
    """
    Creates a probability board considering the **board** and the
    desired **number**.

    """
    prob_board = [[0 for col in range(0, 9)] for row in range(0, 9)]

    for i in range(0, 9):
        for j in range(0, 9):
            pos = board[i][j]

            # IF the position has a number, its position prob is one.
            if(pos == number):
                prob_board[i][j] = 1

                # Row, Col and Cell of position with probability zero.
                prob_board = _prob_row(prob_board, i, j)
                prob_board = _prob_col(prob_board, i, j)
                prob_board = _prob_cell(prob_board, i, j)

            # Positions already filled, probability is zero (too).                               
            elif(pos > 0):
                prob_board[i][j] = "."


    return prob_board


def solution_by_prob_cell(board, sequence=None, verbose=True):
    """
    Calculates the probability of the cells.

    """
    solutions = 0
    board_shadow = board[:]

    # Optimizing the probability of finding for solutions.
    # Using the sequence from most used numbers to less used.
    if(sequence == None):
        sequence = priority_sequence(board_shadow)

    for number in sequence:
        prob_board = probability_board(board_shadow, number)

        # Looking for unique cell with probalility 
        for cell in range(0, 9):
            prob = get_cell(prob_board, cell).count(0)

            if(prob == 1):
                i, j = find_value_in_cell(prob_board, cell, 0)
                board_shadow[i][j] = number
                solutions = solutions + 1

                if(verbose == True):
                    print(f" > Position[{i}][{j}]: {number} - Prob Cell")

        
    return board_shadow, solutions


def solution_by_lines(board, verbose=True):
    """
    Calculates the probability of the line (row and col).

    """
    # Improvements for the algorithm:
    # 1- Priorize line (row and col) with number of appearing.
    # 2- Transform the col and row to a variable and use code once.
    # 3- Pack some sequence into functions.
    #
    
    solutions = 0
    board_shadow = board[:]
    
    # Looking for solutions in ROWS (i)
    for i in range(0, 9):
        prob_line = _all_line_possibilities()
        line = get_row(board_shadow, i)

        # Remove all values already known 
        for j in range(0, 9):
            if(line[j] != 0):
                prob_line[j] = []

        # Remove all present values in the row in its adjacent positions
        for j in range(0, 9):
            pos = line[j]
            if(pos != 0):
                for x in range(0, 9):
                    if(prob_line[x] != []):
                        prob_line[x].remove(pos)

        # Remove all **perpendicular (col)** values
        for j in range(0, 9):
            prob = prob_line[j]
            if(prob != []):
                col = set(remove_zeros(get_col(board_shadow, j)))
                prob = set(prob)
                prob = list(prob - col)

                prob_line[j] = prob

        # Remove all cell values
        for j in range(0, 9):
            prob = prob_line[j]
            if(prob != []):
                cell = set(remove_zeros(get_cell(board_shadow, find_cell(i, j))))
                prob = set(prob)
                prob = list(prob - cell)

                prob_line[j] = prob

        # Find a single value
        for j in range(0, 9):
            if(len(prob_line[j]) == 1):
                board_shadow[i][j] = prob_line[j][0]
                solutions = solutions + 1

                if(verbose == True):
                    print(f" > Position[{i}][{j}]: {prob_line[j][0]} - Prob Line")

        # Find a unique value
        prob_line_flatten = [x for sublist in prob_line for x in sublist]

        for x in range(1, 10):
            counter = prob_line_flatten.count(x)
            if(counter == 1):
                for j in range(0, 9):
                    if(prob_line[j].count(x) == 1):
                        board_shadow[i][j] = x
                        solutions = solutions + 1

                        if(verbose == True):
                            print(f" > Position[{i}][{j}]: {x} - Prob Line Unique")

                                            
    # Looking for solutions in COLS (j)
    for j in range(0, 9):
        prob_line = _all_line_possibilities()
        line = get_col(board_shadow, j)

        # Remove all values already known 
        for i in range(0, 9):
            if(line[i] != 0):
                prob_line[i] = []

        # Remove all present values in the col in its adjacent positions
        for i in range(0, 9):
            pos = line[i]
            if(pos != 0):
                for y in range(0, 9):
                    if(prob_line[y] != []):
                        prob_line[y].remove(pos)

        # Remove all **perpendicular (row)** values
        for i in range(0, 9):
            prob = prob_line[i]
            if(prob != []):
                col = set(remove_zeros(get_row(board_shadow, i)))
                prob = set(prob)
                prob = list(prob - col)

                prob_line[i] = prob

        # Remove all cell values
        for i in range(0, 9):
            prob = prob_line[i]
            if(prob != []):
                cell = set(remove_zeros(get_cell(board_shadow, find_cell(i, j))))
                prob = set(prob)
                prob = list(prob - cell)

                prob_line[i] = prob

        # Find a single value
        for i in range(0, 9):
            if(len(prob_line[i]) == 1):
                board_shadow[i][j] = prob_line[i][0]
                solutions = solutions + 1

                if(verbose == True):
                    print(f" > Position[{i}][{j}]: {prob_line[i][0]} - Prob Line Single")

        # Find a unique value
        prob_line_flatten = [x for sublist in prob_line for x in sublist]

        for x in range(1, 10):
            counter = prob_line_flatten.count(x)
            if(counter == 1):
                for i in range(0, 9):
                    if(prob_line[i].count(x) == 1):
                        board_shadow[i][j] = x
                        solutions = solutions + 1

                        if(verbose == True):
                            print(f" > Position[{i}][{j}]: {x} - Prob Line Unique")

                        
    return board_shadow, solutions


def find_value_in_cell(board, cell, value):
    """
    Find the position specific **value** in a **cell** of a
    given **board**

    Returns its position i (row) and j (col).

    """
    i_offset, j_offset = _cell_offset(cell)

    for i in range(i_offset, i_offset+3):
        for j in range(j_offset, j_offset+3):
            if(board[i][j] == value):
                pos_i = i
                pos_j = j

    # Could add a **break** after the finding of the position
    #    but will be without just to test a bug with two positions


    return pos_i, pos_j


def remove_zeros(array):
    """
    Removes all zeros from a given list.

    """
    new_array = [i for i in array if i != 0]


    return new_array
    

def _cell_offset(cell):
    """
    Gets a specific cell (0~8) from board [3x3] and
    returns the offset of its initial position (upper left).

    """
    i_offset = (cell // 3) * 3
    j_offset = (cell % 3) * 3


    return i_offset, j_offset  

                        
def _prob_row(prob_board, row, col):
    """
    Gets a given position **row** and **col** and fills all
    other row positions with "." (No probability).

    """
    line = [i for i in range(0, 9)]
    line.remove(col)

    for j in line:
        prob_board[row][j] = "."


    return prob_board


def _prob_col(prob_board, row, col):
    """
    Gets a given position **row** and **col** and fills all
    other col positions with "." (No probability).

    """
    line = [i for i in range(0, 9)]
    line.remove(row)

    for i in line:
        prob_board[i][col] = "."


    return prob_board


def _prob_cell(prob_board, row, col):
    """
    Gets a given position **row** and **col** and fills all
    other cell positions with "." (No probability).

    """
    i_offset, j_offset = _cell_offset(find_cell(row, col))

    for i in range(i_offset, i_offset+3):
        for j in range(j_offset, j_offset+3):
            prob_board[i][j] = "."

    prob_board[row][col] = 1
        
            
    return prob_board


def _all_line_possibilities():
    """
    Creates a list with 9 position and all positions with all 9
    numbers possibilities.

    Used for col and row possibilities.
    (IF wish to use for cells, need to change for a matrix).

    """
    line = [[i for i in range(1, 10)] for j in range(0, 9)]


    return line


def check_solution(board):
    """
    Check the solution.

    Sequence of check:
    1- Number of filled positions = 81,
    2- Rows = No repeated number in the row,
    3- Cols = No repeated number in the column.

    If solution has a problem, will print a log with the
    errors found

    """
    # Check for empty values
    counter = count_empty(board)
    log = " **** Error: "
    if(counter > 0):
        log = log + f"c_{counter}"

    # Check singularity in rows
    for i in range(0, 9):
        row = get_row(board, i)
        row = sorted(row)
        if(row != [1, 2, 3, 4, 5, 6, 7, 8, 9]):
            log = log + "row_{i}"

    # Check singularity in cols
    for j in range(0, 9):
        col = get_col(board, j)
        col = sorted(col)
        if(col != [1, 2, 3, 4, 5, 6, 7, 8, 9]):
            log = log + "col_{j}"


    if(log != " **** Error: "):
        print(log + " ****")


    return None
    

# Program --------------------------------------------------------------
#board_list = get_all_boards(extension=".txt")
#board_list = ["sudoku_medium_01.txt"]
#board_list = ["sudoku_hard_01.txt"]
board_list = ["sudoku_veryhard_01.txt"]

for b in board_list:
    print(f" ****  Solving '{b}'  ****")    
    board = read_board(b)
    print_board(board, title="Board - Initial")

    turn = 0   
    while(True):
        turn = turn + 1
        
        board, sol_excl = solution_by_exclusion(board, verbose=True)
        board, sol_cell = solution_by_prob_cell(board, verbose=True)
        board, sol_line = solution_by_lines(board, verbose=True)

        solutions = sol_excl + sol_cell + sol_line
        
        if(solutions > 0):
            print(f" > Solutions found: {solutions}")
            print_board(board, title=f"Board - Turn {turn}")

        elif(count_fill(board) == 81):
            check_solution(board)
            break

        else:
            print(f" > Empty cells: {count_empty(board)}")
            break


    print(" " + 70 * "-" + "\n")


# end
