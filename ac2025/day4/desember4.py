with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]
    
    total = 0
    rows = len(grid)
    cols = len(grid[0])
    
    while True:
        new_grid = []
        round_total = 0
        for i in range(rows):
            new_row = []
            for j in range(cols):
                adjacent_amount = 0
                if grid[i][j] == "@":
                    adjacent_amount += 1 if j > 0 and grid[i][j-1] == "@" else 0 # venstre
                    adjacent_amount += 1 if j < cols - 1 and grid[i][j + 1] == "@" else 0 # høyre
                    adjacent_amount += 1 if i > 0 and grid[i - 1][j] == "@" else 0 # over
                    adjacent_amount += 1 if i < rows - 1 and grid[i + 1][j] == "@" else 0 # under
                    adjacent_amount += 1 if i > 0 and j < cols - 1 and grid[i-1][j+1] == "@" else 0 # oppe høyre
                    adjacent_amount += 1 if i > 0 and j > 0 and grid[i-1][j-1] == "@" else 0 # oppe venstre
                    adjacent_amount += 1 if i < rows - 1 and j > 0 and grid[i+1][j-1] == "@" else 0 # nede venstre
                    adjacent_amount += 1 if i < rows - 1 and j < cols - 1 and grid[i+1][j+1] == "@" else 0 # nede høyre
                    
                    if(adjacent_amount < 4):
                        new_row.append("x")
                        round_total += 1
                    else:
                        new_row.append("@")
                else:
                    new_row.append(".")
            new_grid.append(new_row)
        
        if new_grid == grid:
            break
        
        grid = new_grid
        total += round_total
    print(total)
                    
               
               
               
               
