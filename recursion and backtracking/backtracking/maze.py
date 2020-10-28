def solve_maze(current_position, maze, visited, end_position):
    x, y = current_position
    if current_position == end_position:
        maze[x][y] = 10
        return True
    maze[x][y] = 10
    neighbours = [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]
    for v in neighbours:
        i, j = v
        if 0 <= i < len(maze) and 0 <=j < len(maze[0]) and maze[i][j] != 0:
            if tuple(v) in visited:
                continue
            visited.add(tuple(v))
            if solve_maze(v, maze, visited, end_position):
                return True
            maze[i][j] = 1
    return False

Maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]]

visited = set([0, 0])
solve_maze([0, 0], Maze, visited, [4, 4])
print(Maze)