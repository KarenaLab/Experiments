def find_neighbours(row, col, n):
    """


    """
    # Preparation
    next_steps = list()

    # Movement check (ascendent order of priority)
    # Up
    if(col - 1 > 0):
        next_steps.append([row, col-1])

    # Left
    if(row - 1 > 0):
        next_steps.append([row-1, col])

    # Down
    if(col + 1 < n):
        next_steps.append([row, col+1])

    # Right
    if(row + 1 < n):
        next_steps.append([row+1, col])


    return next_steps


# Program --------------------------------------------------------------
n = 5
visited = [[False for col in range(0, n)] for row in range(0, n)]


queue =[[0, 0]]     # Initial position

while(len(queue) > 0):
    print(queue)    
    row, col = queue.pop(0)

    visited[row][col] = True

    steps = find_neighbours(row, col, n)

    if(len(steps) > 0):
        for i in steps:
            row, col = i
            if(queue.count([row, col]) == 0 and visited[row][col] == False):
                queue.append(i)


