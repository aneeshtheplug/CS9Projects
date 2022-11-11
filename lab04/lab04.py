from Stack import Stack
def solveMaze(maze, startX, startY):
    new_stack = Stack()
    new_stack.push([startX, startY])
    counter = 1
    maze[startX][startY] = counter
    while new_stack.isEmpty() == False:
        guess = new_stack.peek()
        x = guess[0]
        y = guess[1]
        if maze[x-1][y] == "G":
            return True
        elif maze[x-1][y] == ' ':
            counter+=1
            x-=1
            maze[x][y] = counter
            new_stack.push([x,y])
            continue
        
        elif maze[x][y-1] == "G":
            return True
        elif maze[x][y-1] == ' ':
            counter+=1
            y-=1
            maze[x][y] = counter
            new_stack.push([x,y])
            continue

        elif maze[x+1][y] == "G":
            return True
        elif maze[x+1][y] == ' ':
            counter+=1
            x+=1
            new_stack.push([x,y])
            maze[x][y] = counter
            continue

        elif maze[x][y+1] == "G":
            return True
        elif maze[x][y+1] == ' ':
            counter+=1
            y+=1
            new_stack.push([x,y])
            maze[x][y] = counter
            continue

        else:
            if str(maze[x-1][y]).isdigit() == True and maze[x-1][y] < maze[x][y]:
                new_stack.pop()
            elif str(maze[x][y-1]).isdigit() == True and maze[x][y-1] < maze[x][y]:
                new_stack.pop()
            elif str(maze[x+1][y]).isdigit() == True and maze[x+1][y] < maze[x][y]:
                new_stack.pop()
            elif str(maze[x][y+1]).isdigit() == True and maze[x][y+1] < maze[x][y]:
                new_stack.pop()
            elif new_stack.size() == 1:
                new_stack.pop()
            else:
                continue
    return False