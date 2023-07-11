# Rate in a Maze (Backtracking) (P352) ---------------------------------
# 

# Libraries
import time


# Functions
def read_input(filename="input.txt"):
    """
    Read a .txt file with the maze.

    """
    file = open(filename, mode="r")

    board = []
    for line in file:
        data = line.replace("\n", "")
        data = data.split(" ")
        data = list(map(int, data))

        board.append(data)

    file.close()

    size = len(board)

    return board, size


def print_board(board):
    """
    Prints the board for better vizualization

    """
    for line in board:
        for i in line:
            print(i, end=" ")

        print("")

    print("")
    
    return None


def move_up(board, pos_x, pos_y, size):
    """
    Check if move up is available.

    """
    if(pos_x - 1 >= 0):
        pos_x = pos_x - 1

        if(board[pos_x][pos_y] == 0):
            move = [pos_x, pos_y]

        else:
            move = []

    else:
        move = []

    return move


def move_down(board, pos_x, pos_y, size):
    """
    Check if move down is available.

    """
    if(pos_x + 1 < size):
        pos_x = pos_x + 1

        if(board[pos_x][pos_y] == 0):
            move = [pos_x, pos_y]

        else:
            move = []

    else:
        move = []

    return move


def move_left(board, pos_x, pos_y, size):
    """
    Check if move left is available.

    """
    if(pos_y - 1 >= 0):
        pos_y = pos_y - 1

        if(board[pos_x][pos_y] == 0):
            move = [pos_x, pos_y]

        else:
            move = []

    else:
        move = []

    return move


def move_right(board, pos_x, pos_y, size):
    """
    Check if move down is available.

    """
    if(pos_y + 1 < size):
        pos_y = pos_y + 1

        if(board[pos_x][pos_y] == 0):
            move = [pos_x, pos_y]

        else:
            move = []

    else:
        move = []

    return move


def walk(board, pos_x, pos_y, size):
    """
    Checks the next moves in the maze.

    """
    moves = []

    # Sequence of moves, from behind to beginning priority, priority
    # for the diagonal down/right.
    for function in [move_up, move_left, move_down, move_right]:
        get = function(board, pos_x, pos_y, size)

        if(get != []):
            moves.append(get)

    board[pos_x][pos_y] = 9

    return board, moves


# Program --------------------------------------------------------------
board, size = read_input()
move_list = [[0, 0]]    # Starting point

while(True):
    print(f"Backlog of moves: {move_list[0:-1]}")
    print(f"Next move: {move_list[-1]}")

    [pos_x, pos_y] = move_list.pop(-1)

    # Exit clausule (positive)
    if([pos_x, pos_y] == [size-1, size-1]):
        print(" > Exit found")
        break

    board, moves = walk(board, pos_x, pos_y, size)

    for i in moves:
        move_list.append(i)

    print_board(board)
    time.sleep(0.25)

    # Exit clausule (negative)
    if(len(move_list) == 0):
        print(" > Exit NOT found")
        break
    
# end

