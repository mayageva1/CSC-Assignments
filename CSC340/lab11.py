def solve_maze(maze, x, y, visited=None):
    if visited is None:
        visited = set()

    #Check bounds and if the cell is already visited or is a wall
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == "1" or (x, y) in visited:
        return False

    #If we reach the goal
    if maze[x][y] == "G":
        return True

    #Mark the cell as visited
    visited.add((x, y))

    #Recursively explore neighbors with 4 function calls (up, down, left, right)
    #TODO: Fill in the UP or DOWN or LEFT or RIGHT
    if (solve_maze(maze, x - 1, y, visited) or  # Up
        solve_maze(maze, x + 1, y, visited) or  # Down
        solve_maze(maze, x, y - 1, visited) or  # Left
        solve_maze(maze, x, y + 1, visited)):   # Right):
        return True

    #Backtrack:unmark this cell
    visited.remove((x, y))

    return False

#Example call
maze = [
    ["S", "0", "1", "1"],
    ["1", "0", "1", "G"],
    ["1", "0", "0", "0"],
    ["1", "1", "0", "1"]
]

start_x, start_y = 0, 0  # Coordinates of 'S'
result = solve_maze(maze, start_x, start_y)
print("Maze solvable:", result)


from sympy import * 
#Print the general solution to 
#a second order linear homogeneous recurrence relation
def solveSecondOrderRelation(c1, c2):
    #a represents alpha 
    a = Symbol('a')
    #Solve for alpha using c1 and c2

    solution = solve(a**2 - c1*a - c2, a)
    #TODO: Use the solve function from Sympy to solve for p1 and p2
    #https://docs.sympy.org/latest/modules/solvers/solvers.html
    #Check how many possible solutions there are (repeated roots)
    if(len(solution)==1):
        p1 = solution
        #repeated root case so need special form of the equation
        print("General Solution is: a_n="+"A1*"+"("+str(p1)+")^n+"+"A2*n*"+"("+str(p1)+")^n")
    else: #not repeated root case
        #TODO get the values of p1 and p2
        p1 = solution[0]
        p2 = solution[1]
        #TODO replace the print statement in the next line with a print statement for the
        #general recurrence relation solution
        print("General Solution is: a_n="+"A1*"+"("+str(p1)+")^n+"+"A2*"+"("+str(p2)+")^n")
#First test
c1 = 3
c2 = 4
print("Solution for c1=", c1,"c2=",c2)
solveSecondOrderRelation(c1, c2)
#Second test
c1 = 4
c2 = -4
print("Solution for c1=", c1,"c2=",c2)
solveSecondOrderRelation(c1, c2)