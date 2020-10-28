'''
Rat in a Maze
'''

def solve_maze(current_position, maze, end_position, solution):
    size = len(maze)
    x, y = current_position
    if current_position == end_position:
        solution[x][y] = 1
        return True
    
    neighbours = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
    for v in neighbours:
        i, j = v
        if 0 <= i < size and 0 <=j < size and solution[i][j] == 0:
            if maze[i][j] == 0:
                continue
            solution[i][j] = 1
            if solve_maze(v, maze, end_position, solution):
                return True
            solution[i][j] = 0
    return False


Maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]]

solution = [[0 for x in range(len(Maze[0]))] for y in range(len(Maze))]

solve_maze([0, 0], Maze, [4, 4], solution)
solution[0][0] = 1

print(solution)