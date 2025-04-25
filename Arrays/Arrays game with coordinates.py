grid = [["0","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
for i in range(6):
    for j in range(4):
        print(grid[i][j], end=" ")
    print() 
row = int(input("Enter a row coordinate to move to (1-4) "))
column = int(input("Enter a column coordinate to move to (1-6) "))
grid[0][0] = "X"
grid[column-1][row-1] = "O"
for i in range(6):
    for j in range(4):
        print(grid[i][j], end=" ")
    print() 